# SESSION_LOG.md — Journal du pipeline

> Créé automatiquement par le premier agent lancé sur le projet.
> Mis à jour à chaque étape.
> Évite aux agents de relire tous les fichiers en détail.

---

## Statut du pipeline

```
/idea-finder       : ⏭️ Skip (offre déjà signée commercialement, traction empirique OCI)
/offer-cadrage     : ✅ 2026-05-05 (verdict : GO conditionnel)
/persona           : ✅ 2026-05-05 (2 personas : Stéphane Maréchal + Pascal Dubreuil)
/market-research   : ✅ 2026-05-05 (verdict GO ferme avec focus sélectif)
/competitive-intel : ✅ 2026-05-05 (différenciation MOYENNE-FORTE, pas de PIVOT)
/pricing           : ✅ 2026-05-05 (architecture hybride finalisée, LTV/CAC 5,97x)
/offer-final       : ✅ 2026-05-05 (verdict VIABLE SOUS CONDITIONS)
/study-website     : ✅ 2026-05-05 (8 pages générées, charte Mintizy, mobile-first, interactivité validée)
```

---

## Décisions clés

*(Format : [DATE] [AGENT] — [décision] — [output])*

- 2026-05-05 — /offer-project-manager — Création du projet `mintizy` — `.active-project` basculé depuis `uccello-hub`
- 2026-05-05 — Setup — Cadrage initial : objet du projet = packager le portail client Mintizy comme produit revendu via intégrateurs ERP français (modèle OCI). Pas de R&D produit. Pas de connecteur ERP côté UCCELLO. Marque Mintizy par défaut (white-label optionnel). Objectif 12 mois : 5-7 revendeurs, 60-120k€ ARR. — `PROJECT_CONTEXT.md` rempli
- 2026-05-05 — /offer-orchestrator — Démarrage pipeline mode C autonome, périmètre core + study-website, 2 personas — plan validé
- 2026-05-05 — /offer-cadrage — Verdict **GO conditionnel**. Validation empirique forte (4 facturés OCI + 15 pipeline). 3 hypothèses critiques à valider en aval : (1) volumétrie intégrateurs ERP capables de dev une passerelle, (2) coexistence Mintizy/Praxedo dans le bundle, (3) sourcing intégrateurs ERP sans réseau préexistant. Score douleur 7/10. — `OFFER_BRIEF.md` v1.0
- 2026-05-05 — /offer-persona — 2 personas produits. ACHETEUR : Stéphane Maréchal, 49 ans, Directeur Associé cabinet Sage X3 + Cegid XRP Flex 35 personnes Lyon. Score prospectabilité 7/10. UTILISATEUR : Pascal Dubreuil, 52 ans, dirigeant frigoriste cuisine pro 35 techniciens Bordeaux. WTP 250-500€/mois. Adressé via revendeur (canal indirect by design). — `PERSONA_ACHETEUR.md` + `PERSONA_UTILISATEUR.md` v1.0
- 2026-05-05 — /offer-market-research — Verdict **GO ferme avec focus sélectif**. Source SIRENE via API recherche-entreprises.api.gouv.fr. Univers amont qualifié 50-100 cabinets prioritaires (NAF 62.02A 10-249 sal. = 3 156 ESN totales). Univers aval 3 550 PME maintenance technique (43.22B = 2 404 frigo/CVC + 93.11Z = 712 sportives + 33.20D + 33.14Z + 33.19Z). TAM 8,1M€ / SAM 2,3-4,1M€ / SOM 3 ans 114-205k€. Focus année 1 : Cegid XRP Flex + Sage X3. Profil prioritaire 15/20. Risque rouge : Praxedo a déjà un "Portail donneur d'ordres". — `MARKET_RESEARCH.md` v1.0 + enrichissement OFFER_BRIEF
- 2026-05-05 — /offer-competitive-intel — Verdict différenciation **MOYENNE-FORTE**, pas de PIVOT. Frontière Mintizy / Praxedo identifiée : Praxedo Portail donneur d'ordres = portail B2B sous-traitance, Mintizy = portail B2B2C exposition client final. 5 battlecards rédigées (Praxedo, Microsoft D365 FS, Sage X3 SAV+Weblinks, Synchroteam, "ne rien faire"). Phrase de positionnement préemptant la catégorie "portail client B2B2C". **Précision utilisateur** : le bundle OCI Praxedo+Mintizy+Flex est un cas parmi d'autres, pas un modèle imposé ; Mintizy peut être complément OU alternative selon le contexte du revendeur. Brief corrigé en conséquence. — `COMPETITIVE_BRIEF.md` v1.0
- 2026-05-05 — /offer-pricing — Architecture tarifaire hybride finalisée. Grid OCI promu en grille publique Mintizy (Starter/Business/Scale/Enterprise palier client final). Setup fee 990€ HT one-shot par client final perçu par revendeur **identifié comme CRITIQUE** : sans lui, ROI passerelle revendeur 4 ans 7 mois ; avec, 14 mois. Option Quick-Start Passerelle UCCELLO 14 900€ HT (ouvre marché de 50-100 à 150-200 cabinets). Option White-label +50€/mois ou 4 900€ one-shot. Engagement client 12 mois min. Exclusivité territoriale dès 3 clients/18 mois. LTV/CAC revendeur 5,97x sain. — `PRICING_BRIEF.md` v1.0
- 2026-05-05 — /offer-final — Verdict global **VIABLE SOUS CONDITIONS**. 3 critères ✅ (douleur 7/10, prospectabilité 7/10, marché prêt). 4 conditions critiques pour passer à VIABLE FERME : (1) setup fee 990€ intégré dès le 1er contrat hors OCI, (2) Quick-Start Passerelle Sage X3 livré M+6, (3) sourcing structuré dès M+1, (4) 1 deuxième revendeur signé sous 6 mois. Plan 12 mois en 4 trimestres documenté. Cible : 5-7 revendeurs / 25-50 clients finaux / 60-120k€ ARR. — `OFFER_FINAL.md` v1.0
- 2026-05-05 — /offer-study-website — Site interne multi-pages généré dans `website/`. 8 pages (index + offre + persona + marche + concurrence + pricing + viabilite + contact). Charte Mintizy fidèle (turquoise sarcelle #2FB293 + cyan accent + Inter, radius 12px, gradients, glassmorphism nav). HTML/CSS/JS pur, mobile-first responsive, hamburger menu, tabs interactifs (persona), accordions (objections), battlecards dépliables. Hébergement sur preview server localhost:8795. Validation : rendu hero conforme, tabs Stéphane/Pascal fonctionnels, mobile 375px OK. — `website/` v1.0
- 2026-05-05 — /offer-orchestrator — **Pipeline complet terminé** en mode C autonome. 6 agents lancés (cadrage, persona, market, competitive, pricing, final, study-website), 7 fichiers MD + 1 site web 8 pages produits. Verdict cumulé : VIABLE SOUS CONDITIONS, ARR cible 60-120k€/12 mois. Pas de boucle de retour rencontrée. 1 correction utilisateur intégrée (bundle Praxedo non imposé : alternative ou complément selon contexte revendeur).
- 2026-05-05 — /offer-prospection-list — Segment : intégrateurs / ESN adressables (NAF 62.02A, effectifs 10 à 249, sièges prioritaires villes persona : 69, 75, 77, 78, 91 à 95, 31, 33, 44, 59, 67). Volume : 100. Niveau : 1 prévu mais livré socle RAW (sans GMB/Google : pas de batch Places dans ce passage). Complétude : 0 % téléphone, 100 % siège géographiquement aligné filtres, 67 % bloc dirigeant renseigné (API recherche entreprises api.gouv). → `PROSPECTS_2026-05-05_integrateurs-erp-naf6202a.csv`. /offer-prospection-list : ✅ 2026-05-05 (vague 1).
- 2026-05-05 — Enrichissement Places : `scripts/enrich_prospects_gmaps.py`. Sortie `PROSPECTS_2026-05-05_integrateurs-erp-naf6202a_v2.csv` (tél ~88 %, site ~87 %, URL Maps ~98 %).
- 2026-05-05 — Qualification web Cegid : script `scripts/qualify_cegid_integrators_web.py` (annuaire partenaires cegid.com + scan HTML `Site_web`). Sortie `PROSPECTS_2026-05-05_integrateurs-erp-naf6202a_v3.csv`. Signaux forts : Inetum + CGI (liste officielle), SRA (mention XRP Flex sur site groupe). 97 lignes non inferees automatiquement : home souvent sans SEO Cegid alors que pratique existe.
- 2026-05-05 — Listing ciblé **Cegid XRP Flex** : script `scripts/build_cegid_xrp_flex_listing.py` (sources annuaire cegid.com + presse ChannelNews + fiche directory LCS), hydratation `recherche-entreprises.api.gouv.fr`. 30 raisons sociales uniques. Colonnes `Niveau_preuve_Flex` (A/B/C), `Source_Flex_preuve`, `URL_preuve_Flex`. → `PROSPECTS_2026-05-05_cegid-xrp-flex-annuaire-presse.csv`. Enrichissement Places : `enrich_prospects_gmaps.py` → `PROSPECTS_2026-05-05_cegid-xrp-flex-annuaire-presse_gmaps.csv` (tél ~93 %, site ~93 %, URL Maps 100 %).

---

## Versions des fichiers

| Fichier | Version actuelle | Date | Changement |
|---------|-----------------|------|------------|
| IDEA_BRIEF.md | — | — | — |
| OFFER_BRIEF.md | — | — | — |
| PERSONA_ACHETEUR.md | — | — | — |
| PERSONA_UTILISATEUR.md | — | — | — |
| COMPETITIVE_BRIEF.md | — | — | — |
| PRICING_BRIEF.md | — | — | — |
| OFFER_FINAL.md | — | — | — |
| PITCH_DECK.pptx | — | — | — |

---

## Apprentissages terrain

> Rempli par l'utilisateur après tests, interviews ou retours prospects.
> Format : `[DATE] — [source] — [apprentissage] — [agent impacté]`
>
> Exemple : `2026-05-12 — Interview ESN X — Budget max 500€/mois, pas 2000€ — /pricing à revoir`

---

## Points de blocage / décisions en suspens

> Les agents notent ici ce qui nécessite une validation humaine avant de continuer.
