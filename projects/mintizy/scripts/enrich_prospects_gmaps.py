#!/usr/bin/env python3
"""
Enrichit un CSV prospects (Mintizy) avec téléphone, site web et lien Maps
via Places API (New), avec biais géographique depuis l'API Recherche d'entreprises.

Usage:
  export GOOGLE_MAPS_API_KEY=...
  python3 enrich_prospects_gmaps.py \
    --input ../PROSPECTS_2026-05-05_integrateurs-erp-naf6202a.csv \
    --output ../PROSPECTS_2026-05-05_integrateurs-erp-naf6202a_v2.csv

Dépendances : urllib (stdlib), pas de pip.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

ENTREPRISES_SEARCH = "https://recherche-entreprises.api.gouv.fr/search"
PLACES_SEARCH_TEXT = "https://places.googleapis.com/v1/places:searchText"


def extract_postal(addr: str) -> str | None:
    m = re.search(r"\b(\d{5})\b", addr or "")
    return m.group(1) if m else None


def fetch_siege_coords(siren: str) -> tuple[float | None, float | None]:
    q = urllib.parse.urlencode({"q": siren, "per_page": "1"})
    req = urllib.request.Request(
        f"{ENTREPRISES_SEARCH}?{q}",
        headers={"User-Agent": "mintizy-prospect-enrich/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode())
    except (urllib.error.URLError, json.JSONDecodeError, KeyError):
        return None, None
    results = data.get("results") or []
    if not results:
        return None, None
    siege = results[0].get("siege") or {}
    try:
        lat = float(siege.get("latitude"))
        lng = float(siege.get("longitude"))
        return lat, lng
    except (TypeError, ValueError):
        return None, None


def places_search_text(
    api_key: str,
    text_query: str,
    lat: float | None,
    lng: float | None,
    radius_m: int = 4000,
) -> list[dict[str, Any]]:
    body: dict[str, Any] = {
        "textQuery": text_query,
        "languageCode": "fr",
        "maxResultCount": 10,
    }
    if lat is not None and lng is not None:
        body["locationBias"] = {
            "circle": {
                "center": {"latitude": lat, "longitude": lng},
                "radius": min(radius_m, 50000),
            }
        }
    req = urllib.request.Request(
        PLACES_SEARCH_TEXT,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": (
                "places.id,places.displayName,places.formattedAddress,"
                "places.location,places.googleMapsUri"
            ),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")
        print(f"searchText HTTP {e.code}: {err[:300]}", file=sys.stderr)
        return []
    except urllib.error.URLError as e:
        print(f"searchText error: {e}", file=sys.stderr)
        return []
    return data.get("places") or []


def place_details(api_key: str, place_id: str) -> dict[str, Any] | None:
    raw = str(place_id).removeprefix("places/")
    url = f"https://places.googleapis.com/v1/places/{urllib.parse.quote(raw, safe='')}"
    req = urllib.request.Request(
        url,
        method="GET",
        headers={
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": (
                "id,internationalPhoneNumber,nationalPhoneNumber,"
                "websiteUri,googleMapsUri,formattedAddress,displayName"
            ),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")
        print(f"details HTTP {e.code}: {err[:300]}", file=sys.stderr)
        return None
    except urllib.error.URLError as e:
        print(f"details error: {e}", file=sys.stderr)
        return None


def normalize_tokens(s: str) -> set[str]:
    s = re.sub(r"[^\w\s]", " ", (s or "").lower())
    noise = {"sas", "sarl", "sa", "eurl", "sca", "sasu", "ses", "de", "la", "le", "les"}
    return {w for w in s.split() if len(w) > 2 and w not in noise}


def pick_place(
    places: list[dict[str, Any]],
    denomination: str,
    expected_cp: str | None,
) -> tuple[dict[str, Any] | None, str]:
    if not places:
        return None, "Faible"
    denom_toks = normalize_tokens(denomination)

    def score(p: dict[str, Any]) -> float:
        fa = (p.get("formattedAddress") or "").upper()
        name = ""
        dn = p.get("displayName") or {}
        if isinstance(dn, dict):
            name = (dn.get("text") or "").upper()
        s = 0.0
        if expected_cp and expected_cp in fa:
            s += 50
        toks_in_name = denom_toks & normalize_tokens(name)
        if toks_in_name:
            s += 10 * len(toks_in_name)
        loc = p.get("location") or {}
        if loc.get("latitude") is not None:
            s += 1
        return s

    ranked = sorted(places, key=score, reverse=True)
    best = ranked[0]
    sc = score(best)
    fa = (best.get("formattedAddress") or "")
    cp_ok = expected_cp and expected_cp in fa
    if sc >= 50 and cp_ok:
        conf = "Haute"
    elif sc >= 30 or cp_ok:
        conf = "Moyenne"
    else:
        conf = "Faible"
    return best, conf


def phone_from_details(details: dict[str, Any]) -> str:
    phone = (
        details.get("internationalPhoneNumber")
        or details.get("nationalPhoneNumber")
        or ""
    )
    return phone.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--sleep", type=float, default=0.2, help="pause entre lignes")
    ap.add_argument("--radius", type=int, default=4000)
    ap.add_argument("--limit", type=int, default=0, help="traiter seulement N premières lignes (0 = tout)")
    args = ap.parse_args()

    api_key = (os.getenv("GOOGLE_MAPS_API_KEY") or "").strip()
    if not api_key:
        print("Missing GOOGLE_MAPS_API_KEY", file=sys.stderr)
        return 1

    with open(args.input, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if args.limit and args.limit > 0:
        rows = rows[: args.limit]
    fieldnames = list(rows[0].keys()) if rows else []

    extra = []
    for c in ["Confiance_match_GMaps", "Nom_lieu_Google"]:
        if c not in fieldnames:
            fieldnames.append(c)
            extra.append(c)

    phone_hits = 0
    site_hits = 0
    map_hits = 0

    for i, row in enumerate(rows):
        if extra:
            for c in extra:
                row.setdefault(c, "")

        siren = (row.get("SIREN") or "").strip()
        den = (row.get("Dénomination") or "").strip()
        addr = (row.get("Adresse_siege") or "").strip()
        expected_cp = extract_postal(addr)

        lat, lng = fetch_siege_coords(siren)
        time.sleep(args.sleep)

        text_query = f"{den} {addr}".strip()
        if not text_query:
            row["Google_Maps_URL"] = row.get("Google_Maps_URL") or "Fiche GMB absente"
            continue

        places = places_search_text(api_key, text_query, lat, lng, args.radius)
        time.sleep(args.sleep)

        picked, conf = pick_place(places, den, expected_cp)
        row["Confiance_match_GMaps"] = conf

        if not picked:
            row["Google_Maps_URL"] = "Fiche GMB absente"
            row["Nom_lieu_Google"] = ""
            time.sleep(args.sleep)
            continue

        pid = picked.get("id")
        dn = picked.get("displayName") or {}
        row["Nom_lieu_Google"] = dn.get("text", "") if isinstance(dn, dict) else ""

        details = place_details(api_key, pid) if pid else None
        time.sleep(args.sleep)

        if details:
            ph = phone_from_details(details)
            row["Téléphone"] = ph
            if ph:
                phone_hits += 1
            site = (details.get("websiteUri") or "").strip()
            if site:
                row["Site_web"] = site
                site_hits += 1
            gmu = (details.get("googleMapsUri") or picked.get("googleMapsUri") or "").strip()
            if gmu:
                row["Google_Maps_URL"] = gmu
                map_hits += 1
        else:
            gmu = (picked.get("googleMapsUri") or "").strip()
            if gmu:
                row["Google_Maps_URL"] = gmu
                map_hits += 1

        row["Statut_enrichissement"] = (
            "LEVEL_1"
            if (row.get("Téléphone") or row.get("Site_web"))
            else "INCOMPLETE"
        )

        if (i + 1) % 25 == 0:
            print(f"... {i + 1}/{len(rows)}", file=sys.stderr)

    with open(args.output, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)

    n = len(rows)
    print(
        json.dumps(
            {
                "rows": n,
                "phone_rate": round(100 * phone_hits / n, 1) if n else 0,
                "site_rate": round(100 * site_hits / n, 1) if n else 0,
                "maps_url_rate": round(100 * map_hits / n, 1) if n else 0,
                "output": args.output,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
