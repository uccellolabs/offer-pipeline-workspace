# OFFER_BRIEF.md
- Date : 2026-04-25 | Version : 1.6 | Agents : offer-cadrage, market-research, competitive-intel, pricing, persona v2 | Statut : GO (réserves)

## PIPELINE SUMMARY
Idée        : Axell — alimentation automatique du CRM depuis les canaux de com’ (LinkedIn, WhatsApp, Instagram ; email + visio sous ~1 mois ; présentiel via dictaphone à terme), détection des signaux (contact, chaleur, opportunités, tâches) + digest matinal des actions.
Cible       : PME — **acheteur 90j** : **Marc** (DG fondateur, 47 ans, 10–35 sal., décide seul) ; **acheteur 6–12 mois** : **Frédéric** (DG structuré, 51 ans, 80–150 sal., multi-décideurs) ; **utilisateur** : commercial terrain — voir `PERSONA_*.md`.
Problème    : ~20 % du temps commercial perdu à saisir / maintenir le CRM ; CRM perçu sans valeur par les vendeurs ; charge mentale ; opportunités perdues dans les messageries.
Valeur      : Récupération de temps commercial + réduction des opportunités perdues + visibilité pipeline pour la direction.
Canal       : **A direct** (privilégié, 90 j, cold LinkedIn DG 10–35 sal.) + **C apporteurs** (6–12 mois, zéro réseau actuellement — nécessite refs terrain d’abord) ; bootstrapped ; ~1,5 j/sem vente.
Concurrent  : **Principaux** : **HubSpot** (WhatsApp **Business** + inbox) ; **LinkedIn Sales Navigator Advanced Plus** + CRM sync natif ; **SyncIn** (WhatsApp perso → HubSpot) ; **extensions LinkedIn** (**LeadCRM**, **LinkMatch**, etc.) ; **iPaaS** ; **ne rien faire**. Voir `COMPETITIVE_BRIEF.md` — revendication **« seul »** : **à retirer** (preuves marché).
Prix cible  : **Par canal** (non siège) — Starter **59 €** (3 canaux) ; **Growth ⭐ 89 €** (8 canaux) ; Scale **169 €** (18 canaux) ; Enterprise **299 €** (35 canaux). Canal + : **14 €/mois**. Recharge : 5 000 cr. → 79 €. Voir `PRICING_BRIEF_v2.md`.
Verdict     : GO
Pipeline    : Cadrage ✅ | Persona ✅ | Market ✅ | Competitive ✅ | Pricing ✅ | Final ✅ | Deck ⬜ (v1 existant, à refaire avec Marc)

## 1. Idée en une phrase
Axell aide les **PME dont le dirigeant / CFO veut un pipe fiable** à **récupérer du temps commercial et moins rater des deals**, en **remplissant le CRM automatiquement** depuis les **canaux de conversation** (LinkedIn, WhatsApp, Instagram, bientôt email & visio) **sans saisie manuelle**, avec **priorisation** et **digest quotidien** des actions.

## 2. Problème résolu
**Principal** — Saisie CRM lourde (~20 % du temps vendeur), perçue comme sans valeur par les commerciaux ; charge mentale ; relances et petits deals oubliés.

**Sans cette offre** — CRM / Excel / Notion + discipline + « tout dans la tête » ; dette cognitive et trous dans le pipeline.

**Qui souffre le plus** — Commerciaux au quotidien ; **dirigeant / CFO** sur le manque de visibilité et le coût d’opportunité.

## 3. Cible
**Acheteur** — Dirigeant / **CFO** (signature budget).

**Utilisateur final** — Commerciaux (équipe vente).

**Intermédiaire** — Head of sales : **influence possible**, rôle exact sur la signature **non tranché** (à clarifier en /persona selon taille PME).

## 4. Valeur
**Acheteur** — Moins de temps « non-vendeur » ; moins d’opportunités perdues ; meilleure lecture du pipe (à chiffrer : équivalent jour/semaine, % deals rattrapés, etc. — hypothèses).

**Utilisateur** — Moins de saisie ; actions priorisées ; moins d’oublis.

**Quantifiable estimée** — **À valider** (base actuelle : 20 % temps sur CRM = ancrage de travail, pas encore une mesure terrain).

## 5. Verdict Devil's Advocate
✅ **Ce qui tient** — Douleur CRM / charge mentale très lisible ; séparation acheteur / utilisateur cohérente ; produit **déjà prêt** sur le cœur ; email + visio annoncés **≤ ~1 mois** (indispensable déclaré).

❌ **Ce qui ne tient pas encore** — Revendication **« seul »** sur le marché : **non prouvée** ; **déclencheur « pourquoi maintenant »** **inconnu** (risque cycles longs sans trigger).

⚠️ **Hypothèses non vérifiées** — Secteur PME prioritaire **non choisi** ; conformité / confiance **multi-canal** (données, accès) non explorée ici ; messaging CFO vs adoption terrain.

🚧 **Contraintes projet** — Bootstrapped ; faible budget acquisition ; **1,5 j/sem** vente ; roadmap large (multi-canal + dictaphone) = **besoin de périmètre V1 commercial** clair pour le pricing.

## 6. Direction recommandée
[x] GO  [ ] NO-GO  [ ] PIVOT

**Justification** : Poursuite du pipeline **justifiée** : problème et promesse **alignés** avec les ressources et l’état produit. **Pas de NO-GO** : pas d’incohérence bloquante avec le PROJECT_CONTEXT. Les réserves (**« seul »**, **why now**, **ICP sectoriel**, **preuve valeur/prix**) sont des **travaux** pour **persona**, **market-research**, **competitive-intel**, **pricing** — pas des stoppeurs à ce stade.

## 7. Questions prioritaires pour /persona
1. Quels **signaux** font dire **oui** à un **CFO / dirigeant** PME pour un outil qui touche **WhatsApp / messageries** (risque, conformité, gouvernance) ?
2. **Profil PME** le plus rentable en **bootstrapped** + **~1,5 j/sem** vente : taille équipe commerciale, maturité CRM, secteur ?
3. **Objections** des **commerciaux** (« encore un outil », confiance dans l’auto-tagging, peur du contrôle) et **levier d’adoption** minimal ?
4. **Head of sales** : dans quelles tailles de PME devient-il **acheteur** ou **gatekeeper** réel ?
5. **Déclencheurs** plausibles à tester en interview (croissance équipe commerciale, échec précédent CRM, board / objectifs CA, remplacement d’un outil) : lesquels **prioriser** ?

## Prochaine étape : itération terrain

- **Offre rédigée** : `OFFER_FINAL.md` v1.0 (2026-04-24).
- **Support commercial** : `PITCH_DECK.pptx` (2026-04-24) — généré via `generate_pitch_deck.py` ; plan JSON `PITCH_DECK_PLAN.json`.

---

## MARKET RESEARCH UPDATE v1.2

- **Date** : 2026-04-25 | **Canal** : **A — Direct** (privilégié, cold LinkedIn DG 10–35 sal.) + **C — Apporteurs** (zéro réseau → horizon 6–12 mois après refs terrain) | **MCP SIRENE** : **Non** | **Personas** : Marc (DG 10–35) + Frédéric (DG 80–150)

### Qualification canal
- **A direct = seul levier activable 90 jours** — décideur unique (Marc), cycle 2–6 semaines
- **C apporteurs** = nécessite références terrain d’abord — pas activable à froid

### Volume & SAM par profil (sourcé / estimé)

Base INSEE : ~159 000–172 500 PME hors micro (10–249 sal.), France

| Profil | Tranche INSEE | Volume brut | Filtre B2B + vente | Filtre CRM actif | **SAM** |
|---|---|---|---|---|---|
| **Marc** (10–35 sal.) | 10–19 : ~97k + 20–35 : ~26k | ~123 000 | ~25 % | ~30 % | **9 000–12 000** |
| **Frédéric** (80–150 sal.) | Sous-tranche 50+ (~20k) | ~8 000–10 000 | ~35 % | ~40 % | **2 800–3 600** |
| **SAM total** | | | | | **~12 000–16 000** |

Statut : **estimé** — méthode transparente. SIRENE affinerait le filtre B2B.

Note : l’ancien ICP (35–80 sal.) n’est représenté par aucun des deux personas — segment intermédiaire à explorer si Marc + Frédéric déçoivent.

Adoption CRM 10+ sal. : **>90 %** (Capterra France 2025) — **sourcé**
Sous-alimentation CRM : **~60 % de l’ICP** (< 40 % atteignent >90 % adoption utilisateurs) — **sourcé**

### TAM / SAM / SOM

| Niveau | Périmètre | Estimation | Statut |
|---|---|---|---|
| **TAM** | CRM + productivité commerciale FR + francophonie | Multi-milliards € | Sourcé (agrégats marché) |
| **SAM** | PME B2B 10–35 + 80–150 sal., CRM actif, équipe vente | **12 000–16 000** FR | Estimé |
| **SOM 12 mois** | Direct A, 1,5 j/sem, profil Marc uniquement | **20–40 clients** | Estimé |
| **SOM 12 mois** | MRR à 79 €/mois moyen | **1 600–3 200 € MRR** | Estimé |

### Scores profils /20

| Profil | Volume /5 | Approche /5 | Alignement /5 | Cycle /5 | **Score** | Canal requis |
|---|---|---|---|---|---|---|
| **Marc** — DG fondateur 10–35 sal. | 4 | 4 | 5 | 4 | **17/20** | A direct ✅ |
| **Frédéric** — DG structuré 80–150 sal. | 3 | 2 | 4 | 2 | **11/20** | C intégrateurs ❌ |

**Profil prioritaire 90 jours : Marc — 17/20.**
Frédéric = cible de valeur, inaccessible en cold sans réseau. Activer après 3–5 références Marc.

### Checkpoint viabilité 3

```
┌── MARC (90 jours) ─────────────────────────────────┐
│ Budget dédié    : ✅ Décide seul < 300 €/mois       │
│ Budget moyen    : 100–250 €/mois (outil solo DG)    │
│ Maturité        : ⚠️ Conscient du problème,         │
│                    pas encore de solution connue      │
│ Décideurs       : 1                                  │
│ Cycle closing   : 2–6 semaines                      │
│ Signal global   : ✅ Prêt — frein = méfiance         │
│                    post-échec outil                   │
└────────────────────────────────────────────────────-┘

┌── FRÉDÉRIC (6–12 mois) ────────────────────────────┐
│ Budget dédié    : ⚠️ Business case requis            │
│ Budget moyen    : 300–800 €/mois équipe             │
│ Maturité        : ⚠️ Conscient mais sceptique        │
│ Décideurs       : 3–5 (DG + HoS + DAFG + RSSI)     │
│ Cycle closing   : 3–6 mois                          │
│ Signal global   : ❌ Prématuré sans réseau —         │
│                    activer après refs Marc            │
└─────────────────────────────────────────────────────┘
```

### Tension pricing à résoudre

Axell tarifé par équipe (59–119 €/mois). Pour Marc (3 commerciaux) = 20–40 €/commercial → très acceptable. Pour Frédéric (20 commerciaux) = 3–6 €/commercial → sous-valorisé, perception "outil TPE". Un tier "équipe élargie" ou tarif par siège au-delà de 10 commerciaux sera nécessaire pour adresser Frédéric.

### Recommandation 90 jours

1. Focus **Marc uniquement** — 1 vertical précis (ex. cabinets conseil / agences B2B) + 1 CRM (HubSpot ou Pipedrive)
2. Message : *« Arrête de perdre des deals dans tes messageries »* — pas de jargon IA
3. Objectif : **5 pilotes actifs** → 3 références → ouvre le canal C et l’accès à Frédéric

### Questions pour `/competitive-intel`
1. Quels joueurs adressent spécifiquement le **DG fondateur 10–35 sal.** (vs solutions enterprise) ? Angle tarif + onboarding solo
2. Comment les concurrents traitent-ils la **méfiance post-échec outil** — messaging, garanties, trials ?
3. Programme partenaire intégrateur HubSpot/Pipedrive accessible en bootstrap pour préparer le canal C à 6 mois ?

---

*Fin MARKET RESEARCH UPDATE v1.2*

---

## COMPETITIVE INTEL UPDATE v2

- **Date** : 2026-04-25 | Personas : Marc + Frédéric
- **Concurrents directs** : **SyncIn** (WA+LI→HubSpot, sync pur) ; **Surfe** (LinkedIn→CRM, $17–49/seat) ; **TimelinesAI** (WhatsApp→CRM, $8–20/seat) ; **LeadCRM** (LinkedIn→CRM, entrée de gamme)
- **Indirects** : HubSpot natif (Business API only) ; Lemlist (outbound séquences) ; Zapier/Make (DIY) ; Folk CRM (remplace CRM)
- **Zone de différenciation** : Seul outil **multi-canal** (WA perso + LI + Instagram) + **intelligence commerciale** (digest, signaux, priorisation) + **tarifé par canal** (pas par siège)
- **Phrase de positionnement** : *« Contrairement à empiler Surfe ($196/mois, LinkedIn seulement) + TimelinesAI ($80/mois, WhatsApp seulement) pour 4 commerciaux — Axell connecte tous tes canaux à ton CRM existant pour 89€/mois et te dit chaque matin quels deals relancer en premier. »*
- **Argument pricing clé** : 4 com × 2 canaux → Axell 89€ vs Surfe+TimelinesAI ~$276/mois
- **SyncIn** : concurrent le plus proche mais sync pur (pas d'intelligence) + HubSpot-centric + pricing opaque
- Voir `COMPETITIVE_BRIEF_v2.md` pour fiches complètes + battlecards

*Fin COMPETITIVE INTEL UPDATE v2*

---

## PRICING UPDATE v2

- **Date** : 2026-04-25 | **Type** : A (SaaS récurrent) | **Unité** : **CANAL** (non siège/utilisateur)
- **Clarification** : 10 utilisateurs → 15–20 canaux typiques (1,5–2 canaux/user)
- **Coûts internes** : Unipile ~5 €/canal/mois ; crédit 0,02 €

**Architecture de tiers (par canal) :**
| Tier | Canaux | Crédits/mois | Prix HT |
|---|---|---|---|
| Starter | 3 | 900 | **59 €** |
| Growth ⭐ | 8 | 2 400 | **89 €** |
| Scale | 18 | 5 400 | **169 €** |
| Enterprise | 35 | 10 500 | **299 €** |
| Canal + | +1 | +300 | **+14 €** |

- **Tier cible Marc** : Growth 89 € (3–4 com × 2 canaux = 6–8 canaux)
- **Tier cible Frédéric** : Scale/Enterprise 169–299 € (15–20 com × 1,5 canaux)
- **Recharges** : 5 000 cr. → 79 € | 15 000 cr. → 199 € | 50 000 cr. → 549 €
- **Revendeur actif** : -40 % → Growth à 53 €
- **Argument pricing** : Axell Growth 89€ < Surfe seul $196 (4 users, LinkedIn uniquement)
- **Valeur Marc** : ~28 000€/an → value-based 233–467€/mois → Growth 89€ = 64% sous plancher

Voir `PRICING_BRIEF_v2.md` pour détail complet + comparatif concurrents + objections.

*Fin PRICING UPDATE v2*
