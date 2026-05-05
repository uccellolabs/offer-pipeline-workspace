#!/usr/bin/env python3
"""
Construit un CSV « intégrateurs Cegid XRP Flex » à partir :
- Sources web explicites (annuaire cegid.com, ChannelNews, annuaire partenaires Cegid)
- Hydratation siège / NAF / dirigeants / forme juridique : API recherche-entreprises (api.gouv.fr).

Usage :
  python3 build_cegid_xrp_flex_listing.py \\
    --output ../PROSPECTS_2026-05-05_cegid-xrp-flex-annuaire-presse.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from typing import Any

UA = "mintizy-build-cegid-flex/1.0"
SEARCH = "https://recherche-entreprises.api.gouv.fr/search"

NAF_LIBELLÉS: dict[str, str] = {
    "62.01Z": "Programmation informatique",
    "62.02A": "Conseil en systèmes et logiciels informatiques",
    "62.02B": "Tierce maintenance de systèmes et d’applications informatiques",
    "62.09Z": "Autres activités informatiques",
    "62.07Z": "Conseil informatique (NAF légué)",
    "70.22Z": "Conseil pour les affaires et autres conseils de gestion",
    "85.59A": "Formation continue pour adultes",
    "71.12B": "Ingénierie, études techniques",
    "68.20B": "Location et exploitation de biens immobiliers propres ou loués",
    "58.29A": "Édition de logiciels système et de réseau",
}

NATURE_LIB: dict[str, str] = {
    "5499": "SASU",
    "5498": "SARL",
    "5710": "SAS",
    "5599": "SA à directoire",
    "5570": "SA",
    "6540": "SNC",
}


def eff_tranche_human(code: str | None) -> str:
    m = {
        "NN": "",
        "00": "0 ou 1",
        "01": "1 à 2",
        "02": "3 à 5",
        "03": "6 à 9",
        "11": "10 à 19",
        "12": "20 à 49",
        "21": "50 à 99",
        "22": "100 à 199",
        "31": "200 à 249",
        "32": "250 à 499",
        "41": "500 à 999",
        "42": "1 000 à 1 999",
        "51": "2 000 à 4 999",
        "52": "5 000 à 9 999",
        "53": "10 000 et plus",
    }
    if not code:
        return ""
    return m.get(str(code), str(code))


def fetch_company(siren: str) -> dict[str, Any] | None:
    q = urllib.parse.urlencode({"q": siren, "per_page": "1"})
    last_err: Exception | None = None
    for attempt in range(4):
        req = urllib.request.Request(f"{SEARCH}?{q}", headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                data = json.loads(r.read().decode())
            results = data.get("results") or []
            return results[0] if results else None
        except (OSError, ValueError, json.JSONDecodeError, KeyError, TypeError) as e:
            last_err = e
            time.sleep(0.35 * (attempt + 1))
    if last_err:
        print(last_err, file=sys.stderr)
    return None


def first_pp_dirigeant(x: dict[str, Any]) -> tuple[str, str, str]:
    for d in x.get("dirigeants") or []:
        if d.get("type_dirigeant") != "personne physique":
            continue
        pr = (d.get("prenoms") or "").strip()
        no = (d.get("nom") or "").strip()
        ql = (d.get("qualite") or "").strip()
        if pr or no:
            return pr, no, ql
    return "", "", ""


# (SIREN, niveau preuve, description courte, URL preuve)
# niveau : A = mention explicite Flex (texte Cegid ou fiche directory Flex)
#          B = presse / annonce réseau XRP Flex (ChannelNews)
#          C = annuaire intégrateurs cegid.com (bloc ERP, pas détail Flex sur la carte)
ENTRIES: list[tuple[str, str, str, str]] = [
    ("825070121", "A", "Annuaire cegid.com : expert Cegid XRP Flex + XRP Ultimate", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("837998798", "A", "Annuaire cegid.com : intégrateur Cegid XRP Flex (Nantes)", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("909165466", "A", "Annuaire cegid.com : solutions Isie et XRP Flex", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("429370414", "A", "Directory partenaires Cegid : solution & services Cegid XRP Flex", "https://partners.cegid.com/French/directory/partner/1326662/lcs-group"),
    ("409070760", "B", "Presse ChannelNews : réseau partenaires XRP Flex (SRA cité)", "https://www.channelnews.fr/cegid-continue-dattirer-de-nouveaux-partenaires-pour-integrer-son-erp-xrp-flex-144410"),
    ("501170468", "B", "Presse ChannelNews : réseau Flex (Evogest cité)", "https://www.channelnews.fr/cegid-continue-dattirer-de-nouveaux-partenaires-pour-integrer-son-erp-xrp-flex-144410"),
    ("823103148", "B", "Presse ChannelNews : « RSM France » (entité opérationnelle SI à confirmer terrain)", "https://www.channelnews.fr/cegid-continue-dattirer-de-nouveaux-partenaires-pour-integrer-son-erp-xrp-flex-144410"),
    ("379019482", "B", "Presse ChannelNews : partenaires historiques recrutés sur la base du réseau Flex (Parthena)", "https://www.channelnews.fr/cegid-double-son-reseau-de-partenaires-xrp-flex-pour-faire-face-a-la-demande-124611"),
    ("439548199", "B", "Presse ChannelNews : idem (Althays / Groupe Althays)", "https://www.channelnews.fr/cegid-double-son-reseau-de-partenaires-xrp-flex-pour-faire-face-a-la-demande-124611"),
    ("433036407", "B", "Presse ChannelNews : idem (Alticap)", "https://www.channelnews.fr/cegid-double-son-reseau-de-partenaires-xrp-flex-pour-faire-face-a-la-demande-124611"),
    ("350066007", "B", "Presse ChannelNews : « Flex For You » / entité liée à Axe Informatique", "https://www.channelnews.fr/cegid-double-son-reseau-de-partenaires-xrp-flex-pour-faire-face-a-la-demande-124611"),
    ("482831732", "B", "Presse ChannelNews : derniers partenaires signés Flex (Aetia)", "https://www.channelnews.fr/cegid-double-son-reseau-de-partenaires-xrp-flex-pour-faire-face-a-la-demande-124611"),
    ("480307966", "B", "Site OCI : pratique Cegid / contexte XRP Flex (cabinet de référence)", "https://www.oci.fr/propulsez-vos-equipes/administratif-finance/cegid/"),
    ("507389260", "C", "Annuaire cegid.com : Infogestion Consulting (XRPU / intégration maîtrisée)", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("903502656", "C", "Annuaire cegid.com : Terensys (ERP & gestion financière)", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("852860360", "C", "Annuaire cegid.com : Lucem", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("409375359", "C", "Annuaire cegid.com : Timsoft (TIM SOFT, dénomination légale)", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("793288010", "C", "Annuaire cegid.com : Viseo (carte « Retail »)", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("829295286", "C", "Annuaire cegid.com : Cod4is", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("904911807", "C", "Annuaire cegid.com : Alcyia Advisory", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("445088057", "C", "Annuaire cegid.com : Accenture", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("443021241", "C", "Annuaire cegid.com : BearingPoint", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("511199226", "C", "Annuaire cegid.com : Amaris", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("328781786", "C", "Annuaire cegid.com : Capgemini", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("333455400", "C", "Annuaire cegid.com : CGI France Ingénierie", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("315930578", "C", "Annuaire cegid.com : Inetum", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("326820065", "C", "Annuaire cegid.com : « Sopra Steria Next » (nom commercial ; raison sociale groupe)", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("948880166", "C", "Annuaire cegid.com : Fortify (dénomination retenue pour « Groupe Fortify » dans l’annuaire — à croiser siège réel)", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("831894381", "C", "Annuaire cegid.com : HR Path → entité légale la plus plausible « HR PATH WD » (62.02A, Puteaux) ; groupe multi-filiales", "https://www.cegid.com/fr/partenaires-integrateurs"),
    ("848046330", "C", "Annuaire cegid.com : ACT-ON GROUP → rattachement hypothèse « ACT-ON TECHNOLOGY » (à confirmer avec groupe)", "https://www.cegid.com/fr/partenaires-integrateurs"),
]


CSV_FIELDS = [
    "SIREN",
    "Dénomination",
    "Forme_juridique",
    "NAF",
    "Libellé_NAF",
    "Effectif",
    "Ville",
    "Département",
    "Date_création",
    "Dirigeant_prénom",
    "Dirigeant_nom",
    "Dirigeant_poste",
    "Téléphone",
    "Email_direct",
    "Google_Maps_URL",
    "Site_web",
    "LinkedIn_entreprise",
    "LinkedIn_décideur",
    "Email_pattern_1",
    "Email_pattern_2",
    "Profil_DISC_estime",
    "Signaux_DISC",
    "Confiance_DISC",
    "Signal_business",
    "Score_pertinence",
    "Statut_enrichissement",
    "Date_génération",
    "Bonus_mots_cles_ERP",
    "Adresse_siege",
    "SIRET_siege",
    "Niveau_preuve_Flex",
    "Source_Flex_preuve",
    "URL_preuve_Flex",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--date", default="2026-05-05")
    args = ap.parse_args()

    seen: set[str] = set()
    rows: list[dict[str, str]] = []
    errs: list[str] = []

    for siren, niveau, desc, url in ENTRIES:
        siren = siren.strip()
        if siren in seen:
            continue
        seen.add(siren)

        co = fetch_company(siren)
        if not co:
            errs.append(siren)
            continue
        time.sleep(0.12)

        siege = co.get("siege") or {}
        naf = siege.get("activite_principale") or co.get("activite_principale") or ""
        adr = siege.get("adresse") or ""
        pr, no, ql = first_pp_dirigeant(co)
        nj = co.get("nature_juridique")
        fj = NATURE_LIB.get(str(nj), str(nj or ""))

        eff_code = siege.get("tranche_effectif_salarie") or co.get("tranche_effectif_salarie")
        bonus = (
            "9"
            if niveau == "A"
            else ("7" if niveau == "B" else ("5" if niveau == "C" else "3"))
        )

        rows.append(
            {
                "SIREN": siren,
                "Dénomination": (co.get("nom_raison_sociale") or co.get("nom_complet") or "").strip(),
                "Forme_juridique": fj,
                "NAF": naf,
                "Libellé_NAF": NAF_LIBELLÉS.get(str(naf), ""),
                "Effectif": eff_tranche_human(str(eff_code) if eff_code is not None else ""),
                "Ville": (siege.get("libelle_commune") or "").strip(),
                "Département": (siege.get("departement") or "").strip(),
                "Date_création": (co.get("date_creation") or "").strip(),
                "Dirigeant_prénom": pr,
                "Dirigeant_nom": no,
                "Dirigeant_poste": ql,
                "Téléphone": "",
                "Email_direct": "",
                "Google_Maps_URL": "",
                "Site_web": "",
                "LinkedIn_entreprise": "",
                "LinkedIn_décideur": "",
                "Email_pattern_1": "",
                "Email_pattern_2": "",
                "Profil_DISC_estime": "",
                "Signaux_DISC": "",
                "Confiance_DISC": "",
                "Signal_business": "Cegid_XRP_Flex",
                "Score_pertinence": bonus,
                "Statut_enrichissement": "RAW_DATAGOUV",
                "Date_génération": args.date,
                "Bonus_mots_cles_ERP": bonus,
                "Adresse_siege": adr,
                "SIRET_siege": (siege.get("siret") or "").strip(),
                "Niveau_preuve_Flex": niveau,
                "Source_Flex_preuve": desc,
                "URL_preuve_Flex": url,
            }
        )

    with open(args.output, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)

    print(
        json.dumps(
            {"written": len(rows), "missing_api": errs, "output": args.output},
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
