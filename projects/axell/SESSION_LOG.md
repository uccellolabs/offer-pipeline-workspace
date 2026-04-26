# SESSION_LOG.md — Journal du pipeline

> Créé automatiquement par le premier agent lancé sur le projet.
> Mis à jour à chaque étape.
> Évite aux agents de relire tous les fichiers en détail.

---

## Statut du pipeline

```
/idea-finder       : ✅ 2026-04-24
/offer-cadrage     : ✅ 2026-04-24
/persona           : ✅ 2026-04-24
/market-research   : ✅ 2026-04-24 + ✅ 2026-04-25 (v1.1)
/competitive-intel : ✅ 2026-04-24
/pricing           : ✅ 2026-04-24
/offer-final       : ✅ 2026-04-24
/pitch-deck        : ✅ 2026-04-24
```

---

## Décisions clés

*(Format : [DATE] [AGENT] — [décision] — [output])*

- [2026-04-24] [project-manager] — Projet multi `axell` créé, `.active-project` défini — `projects/axell/PROJECT_CONTEXT.md` initialisé (compétences + orientations renseignées).
- [2026-04-24] /idea-finder — Sources : 8+ | Plaintes : 40+ (patterns) | Shortlist : 4 (scores 24–28/30) ; priorité 1 : suivi prospection multi-canal / anti app-switching — `IDEA_BRIEF.md` créé.
- [2026-04-24] /offer-cadrage — Verdict **GO** (réserves : « seul » non prouvé, why now à valider, ICP secteur ouvert) — Axell : CRM auto depuis canaux, acheteur CFO/dirigeant — `OFFER_BRIEF.md` v1.0 (`projects/axell/OFFER_BRIEF.md`, issu du cadrage racine).
- [2026-04-24] /persona — Avatars : **Émilie Rousseau** (acheteuse DAFG, prospectabilité **8/10**) + **Thomas Garnier** (commercial, **10/10**) ; budget acheteur indicatif **200–800 €/mois** stack commerciale, pilote **< 300 €/mois** acceptable — `PERSONA_ACHETEUR.md` + `PERSONA_UTILISATEUR.md` v1.0.
- [2026-04-25] /persona v2 — Avatars recalés : **Marc** (DG fondateur 10–35 sal., **9/10**) + **Frédéric** (DG structuré 80–150 sal., **6/10**) ; budget Marc **100–250 €/mois** (solo, décide seul) ; Frédéric **300–800 €/mois** (business case requis) — `PERSONA_ACHETEUR_MARC_v2.md` + `PERSONA_ACHETEUR_FREDERIC_v2.md` créés.
- [2026-04-24] /market-research — Canal **D (mixte)** : **90 j** = levier **intégrateurs / apporteurs** + pilotes **directs** DAFG ; ICP prioritaire **PME B2B 35–80 sal.** (**16/20**) ; viabilité 3 **⚠️** (budget ligne + pédagogie auto-alim. CRM) ; MCP SIRENE **non** — `OFFER_BRIEF.md` **v1.1** (bloc *MARKET RESEARCH UPDATE*).
- [2026-04-25] /market-research v1.1 — Canal **A direct** (privilégié) + **C zéro réseau** (6–12 mois) ; SAM affiné **5 000–7 500 PME** (INSEE + filtre B2B) ; profil A1 DAFG **15/20**, A2 DG **13/20** ; avantage pricing structurel (Axell = 5–15 % budget CRM ICP) ; SOM 12 mois réaliste **15–30 clients** — `OFFER_BRIEF.md` enrichi.
- [2026-04-25] /market-research v1.2 — Personas recalés : **Marc** (DG fondateur 10–35 sal., **17/20**) + **Frédéric** (DG structuré 80–150 sal., **11/20**) ; SAM bimodal **12 000–16 000** PME ; SOM 12 mois **20–40 clients Marc** (1 600–3 200 € MRR) ; Frédéric **❌ prématuré** sans canal C ; tension pricing par équipe vs par siège identifiée — `OFFER_BRIEF.md` **v1.6**.
- [2026-04-24] /competitive-intel — Concurrent principal **catégorie** : **HubSpot + Sales Nav / extensions** ; **invalidation** revendication **« seul »** ; différenciation : **multi-canal complément CRM** + **digest** — `COMPETITIVE_BRIEF.md` v1.0.
- [2026-04-25] /competitive-intel v2 — Concurrents recadrés sur **Marc** : **SyncIn** (plus proche, sync pur HubSpot) ; **Surfe** ($17–49/seat, LinkedIn only) ; **TimelinesAI** ($8–20/seat, WA only) ; argument prix : Axell Growth 89€ < Surfe seul $196 pour 4 users ; positionnement : **multi-canal + intelligence vs. mono-canal + sync** — `COMPETITIVE_BRIEF_v2.md` ; `OFFER_BRIEF` **v1.7**.
- [2026-04-24] /pricing — Modèle **SaaS** **packs** + **19 € HT/canal** à la carte ; **tier cible** **49 € HT/mois** (3 canaux) ; **revendeur** **~40 %+** / **remise ~35 %** ; **value-based** vs **persona** **OK** — `PRICING_BRIEF.md` v1.0 ; `OFFER_BRIEF.md` **v1.3** (*PRICING UPDATE*).
- [2026-04-24] /pricing — **Ajustement** coûts **Unipile 5 €/canal** + **crédits 0,02 €** ; formule **500+350×N** ; packs **49/69/109 € HT** ; canal **+22 €** ; **recharges** ; `PRICING_BRIEF.md` **v1.1** ; `OFFER_BRIEF` **v1.4** ; `PROJECT_CONTEXT` offre Axell.
- [2026-04-24] pricing — **Veille web** concurrents → packs **59/79/119 € HT**, canal +24 €, recharges — `PRICING_BRIEF` **v1.2**, `OFFER_BRIEF` **v1.5**.
- [2026-04-25] /pricing v2 — Unité recalée : **CANAL** (non siège) ; 10 users → 15–20 canaux ; tiers **59/89/169/299 €** (3/8/18/35 canaux) ; canal + **14 €** ; valeur Marc ~28k€/an → Growth 89€ = 64% sous value-based ; Frédéric Enterprise 299€ < budget max ; revendeur 40% — `PRICING_BRIEF_v2.md` ; `OFFER_BRIEF` **v1.7**.
- [2026-04-25] /pricing v3 — **3 anomalies corrigées** : (1) coût crédits Growth sous-estimé (5€ → 16€ réel) ; (2) **recharges v2 toutes en dessous du coût** (5k cr à 79€ vs coût 100€ → corrigé 119€) ; (3) **remise revendeur 40% non viable** (Growth à 53€ revendeur < coût 56€ → ramenée à 25%) — Scale relevé **179€**, Enterprise **349€** — marges corrigées : Starter 64%, Growth 37%, Scale/Enterprise 30% — `PRICING_BRIEF_v3.md` créé.
- [2026-04-24] /offer-final — Destinataire : **client final PME** — Format : **one-pager / support démo** — `OFFER_FINAL.md` **v1.0** créé.
- [2026-04-25] /offer-final v2 — Destinataire : **C (client final Marc + revendeur intégrateur CRM)** — Format : **2 one-pagers** — Viabilité : **⚠️ viable sous conditions** (DPA WhatsApp, 0 ref externe, pilote 30j) — `OFFER_FINAL_v2.md` + `OFFER_FINAL_REVENDEUR_v2.md` créés.
- [2026-04-24] /pitch-deck — Destinataire : **client final** — Contexte : **hybride** (15 min) — Thème : **charte Uccello** (navy `#1a1d2e`, accent `#79d374`) — `PITCH_DECK.pptx` + `PITCH_DECK_PLAN.json` + `generate_pitch_deck.py` (python-pptx ; skill `/mnt/skills/public/pptx` absent localement).

---

## Versions des fichiers

| Fichier | Version actuelle | Date | Changement |
|---------|-----------------|------|------------|
| IDEA_BRIEF.md | 1.0 | 2026-04-24 | Première shortlist |
| OFFER_BRIEF.md | 1.5 | 2026-04-24 | Pricing ajusté veille concurrents (v1.2) |
| PERSONA_ACHETEUR.md | 1.0 | 2026-04-24 | Émilie Rousseau (DAFG) — remplacé par v2 |
| PERSONA_ACHETEUR_MARC_v2.md | 2.0 | 2026-04-25 | Marc (DG fondateur 10–35 sal.) |
| PERSONA_ACHETEUR_FREDERIC_v2.md | 2.0 | 2026-04-25 | Frédéric (DG structuré 80–150 sal.) |
| PERSONA_UTILISATEUR.md | 1.0 | 2026-04-24 | Thomas Garnier (commercial) |
| COMPETITIVE_BRIEF.md | 1.0 | 2026-04-24 | HubSpot, SyncIn, extensions LI, battlecards |
| PRICING_BRIEF.md | 1.2 | 2026-04-24 | Veille SyncIn/Surfe/LeadCRM + grille 59/79/119 |
| PRICING_BRIEF_v2.md | 2.0 | 2026-04-25 | Unité canal, tiers 59/89/169/299€ — **anomalies coûts crédits + recharges** |
| PRICING_BRIEF_v3.md | 3.0 | 2026-04-25 | Coûts corrigés, recharges viables, Scale 179€, Enterprise 349€, revendeur 25% |
| OFFER_FINAL.md | 1.0 | 2026-04-24 | One-pager commercial + score viabilité |
| PITCH_DECK.pptx | 1.0 | 2026-04-24 | 12 slides commercial + notes |

---

## Apprentissages terrain

> Rempli par l'utilisateur après tests, interviews ou retours prospects.
> Format : `[DATE] — [source] — [apprentissage] — [agent impacté]`
>
> Exemple : `2026-05-12 — Interview ESN X — Budget max 500€/mois, pas 2000€ — /pricing à revoir`

---

## Points de blocage / décisions en suspens

> Les agents notent ici ce qui nécessite une validation humaine avant de continuer.

- Valider côté terrain : positionnement Axell plus « inbox unifiée » vs « CRM allégé » vs les deux (message unique) — à réconcilier avec le cadrage **CRM auto-alimenté**.
- Réserves cadrage : revendication « seul », why now, ICP sectoriel, preuve valeur/prix (voir OFFER_BRIEF §5–6).
