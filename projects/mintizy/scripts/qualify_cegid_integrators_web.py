#!/usr/bin/env python3
"""
Qualifie Cegid / XRP Flex depuis l'annuaire partenaires (extraits textuels)
et un crawl léger des colonnes Site_web.

  python3 qualify_cegid_integrators_web.py \\
    --input ../PROSPECTS_2026-05-05_integrateurs-erp-naf6202a_v2.csv \\
    --output ../PROSPECTS_2026-05-05_integrateurs-erp-naf6202a_v3.csv
"""
from __future__ import annotations

import argparse
import csv
import html
import re
import ssl
import sys
import time
import urllib.error
import urllib.request

CEGID_PARTENAIRES_URL = "https://www.cegid.com/fr/partenaires-integrateurs/"

# Fragments à matcher sur Dénomination (ordre : plus long d'abord lors du tri dans le code).
# « note » = formulation prudente avec URL de preuve (page annuaire officielle).
DENOM_FRAGMENTS: list[tuple[str, str]] = [
    ("LEBEL TECHNOLOGIES", "Carte annuaire Cegid : mention XRP Flex : " + CEGID_PARTENAIRES_URL),
    ("INFOGESTION CONSULTING", "Carte annuaire : Infogestion Consulting, XRPU/XRP : " + CEGID_PARTENAIRES_URL),
    ("SYXPERIANE", "Carte annuaire : expertise XRP Flex et XRP Ultimate : " + CEGID_PARTENAIRES_URL),
    ("CS INFO", "Carte annuaire : intégrateur Cegid XRP Flex (Nantes) : " + CEGID_PARTENAIRES_URL),
    ("CGI FRANCE", "Partenaire listé dans l'annuaire Cegid : " + CEGID_PARTENAIRES_URL),
    ("CAPGEMINI", "Partenaire listé dans l'annuaire Cegid : " + CEGID_PARTENAIRES_URL),
    ("ACCENTURE", "Partenaire listé dans l'annuaire Cegid : " + CEGID_PARTENAIRES_URL),
    ("BEARINGPOINT", "Partenaire listé dans l'annuaire Cegid : " + CEGID_PARTENAIRES_URL),
    ("SOPRA STERIA", "Partenaire listé dans l'annuaire Cegid : " + CEGID_PARTENAIRES_URL),
    ("AMARIS", "Partenaire listé dans l'annuaire Cegid : " + CEGID_PARTENAIRES_URL),
    ("HR PATH", "Partenaire listé RH : " + CEGID_PARTENAIRES_URL),
    ("TIMSOFT", "Partenaire listé Retail Cegid : " + CEGID_PARTENAIRES_URL),
    ("VISEO", "Partenaire listé Retail ORLI/Y2 : " + CEGID_PARTENAIRES_URL),
    ("TERENSYS", "Partenaire listé ERP Cegid : " + CEGID_PARTENAIRES_URL),
    ("LUCEM", "Partenaire listé ERP Cegid : " + CEGID_PARTENAIRES_URL),
    ("ALCYIA", "Partenaire listé : " + CEGID_PARTENAIRES_URL),
    ("COD4IS", "Partenaire listé Retail : " + CEGID_PARTENAIRES_URL),
    ("ENGINEERING", "Partenaire listé mode/fashion : " + CEGID_PARTENAIRES_URL),
    ("FORTIFY", "Partenaire listé annuaire Cegid : " + CEGID_PARTENAIRES_URL),
    ("BPAP", "Carte annuaire : BPAP centree XRP Ultimate (pas Flex dans l'extrait court) : " + CEGID_PARTENAIRES_URL),
    ("EURYALE", "Carte annuaire : XRP Ultimate : " + CEGID_PARTENAIRES_URL),
    ("INETUM", "Partenaire ERP listé dans l'annuaire Cegid (non détail Flex sur la carte résumée) : " + CEGID_PARTENAIRES_URL),
    ("CGI ", "Partenaire listé annuaire Cegid : " + CEGID_PARTENAIRES_URL),
]


def norm_denom(s: str) -> str:
    s = (s or "").upper()
    s = re.sub(r"[.,\"'´`()«»]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def match_annuaire(denom: str) -> tuple[str, str] | tuple[None, None]:
    d = norm_denom(denom)
    for frag, note in DENOM_FRAGMENTS:
        if frag.upper() in d:
            return frag, note
    return None, None


def fetch_text(url: str, max_bytes: int = 350_000) -> str:
    if not url or not url.startswith(("http://", "https://")):
        return ""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "mintizy-qualif-cegid/1.0"},
        method="GET",
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
            raw = resp.read(max_bytes + 1)[:max_bytes]
    except (urllib.error.URLError, OSError, ValueError):
        return ""
    text = raw.decode("utf-8", errors="ignore")
    text = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", text)
    text = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    return text.lower()


def niveau_site(t: str) -> tuple[list[str], str]:
    """Retourne (tags, brute phrase courte)."""
    tags: list[str] = []
    if re.search(r"\bcegid\b", t):
        tags.append("mot_Cegid")
    if re.search(r"xrp\s+flex|\bxrp\s*flex\b|\bcegid\s+xrp\s+flex\b", t):
        tags.append("mention_XRP_Flex")
    if "cegid" in t and re.search(r"xrp\s*(ultimate|u\b)", t):
        tags.append("mention_XRP_Ultimate")
    if "cegid" in t and re.search(r"\bsprint\b|\bflex\b", t):
        tags.append("possible_Sprint_Ou_Flex_legacy")
    if "cegid" in t and re.search(r"\by2\b|\borli\b", t):
        tags.append("mention_retail_Y2_ORLI")
    brute = ";".join(tags) if tags else ""
    return tags, brute


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--sleep", type=float, default=0.35)
    args = ap.parse_args()

    with open(args.input, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("CSV vide", file=sys.stderr)
        return 1

    base_cols = list(rows[0].keys())
    extras = [
        "Match_annuaire_Cegid_fragment",
        "Note_source_annuaire_Cegid",
        "Site_scan_mots_cles",
        "Qualif_Cegid_XRP_Web",
        "Preuve_urls",
        "OCI_reference_note",
    ]
    fieldnames = base_cols[:]
    for c in extras:
        if c not in fieldnames:
            fieldnames.append(c)

    OCI_NOTE = (
        "OCI non present dans ce fichier NAF 62 02 A : integrateur historique cite Top 3 XRP Flex sur "
        "https://www.oci.fr/propulsez-vos-equipes/administratif-finance/cegid/ "
        "et repertoire partenaires https://partners.cegid.com/ (Mintizy deja distribue via OCI, cf. dossier projet)."
    )

    cache_fetch: dict[str, str] = {}

    for i, row in enumerate(rows):
        for k in extras:
            row.setdefault(k, "")

        denom = row.get("Dénomination", "")
        frag, note = match_annuaire(denom)
        row["Match_annuaire_Cegid_fragment"] = frag or ""
        row["Note_source_annuaire_Cegid"] = note if frag else ""

        url = (row.get("Site_web") or "").strip()
        if url:
            parsed = urllib.parse.urlparse(url)
            domain = parsed.netloc or url
            if domain not in cache_fetch:
                cache_fetch[domain] = fetch_text(url)
                time.sleep(args.sleep)
            thtml = cache_fetch[domain]
        else:
            thtml = ""

        tags, brute = niveau_site(thtml)
        row["Site_scan_mots_cles"] = brute

        preuves: list[str] = []
        if frag:
            preuves.append(CEGID_PARTENAIRES_URL)
        url_ok = url if url and url.startswith("http") else ""
        preuves.append(url_ok[:200])

        niveau = "Non_qualifie"
        if "mention_XRP_Flex" in tags:
            niveau = "Fort_Site_XRP_Flex"
        elif frag in ("SYXPERIANE", "CS INFO", "LEBEL TECHNOLOGIES"):
            niveau = "Fort_Annuaire_Cegid_citation_XRP_Flex"
        elif "mention_XRP_Ultimate" in tags:
            niveau = "Partiel_XRP_Ultimate_ou_bundle"
        elif frag == "INETUM":
            niveau = "Moderne_Annuaire_Cegid_Generic_Groupe"
        elif "mot_Cegid" in tags:
            niveau = "Faible_site_mentionne_Cegid"
        elif frag:
            niveau = "Liste_annuaire_Cegid_sans_scan_site_utile"

        row["Qualif_Cegid_XRP_Web"] = niveau
        row["Preuve_urls"] = " ; ".join(p for p in preuves if p)
        row["OCI_reference_note"] = OCI_NOTE if i == 0 else ""

    with open(args.output, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    counts: dict[str, int] = {}
    for row in rows:
        k = row.get("Qualif_Cegid_XRP_Web", "")
        counts[k] = counts.get(k, 0) + 1
    print("Qualification counts:", counts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
