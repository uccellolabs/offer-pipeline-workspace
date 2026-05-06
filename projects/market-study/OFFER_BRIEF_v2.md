# OFFER_BRIEF_v2.md
- Date : 2026-05-06 | Version : 2.0 | Agent : offer-cadrage (re-run)
- Statut : GO global (gamme à 3 portes, séquencement validé) | Conditions précisées
- Successeur de : OFFER_BRIEF.md v1.0 (2026-04-27)

---

## PIPELINE SUMMARY v2

```
Idée        : Gamme à 3 portes — DFY freelance + DIY freelance + DIY agence
Cibles      : (1) Julien — consultant freelance 30-42 ans (DFY)
              (2) Marc — consultant senior / power user IA (DIY freelance)
              (3) Hélène — Head of Strategy / Directeur cabinet 5-30 consultants (DIY agence)
Problèmes   : (1) Offre floue → pas de clients   (DFY)
              (2) Veut industrialiser sa pratique IA sans dépendre d'un SaaS  (DIY-S)
              (3) Veut un outil interne souverain pour ses missions clients (DIY-A)
Valeur      : (1) Livrable 48-72h    (2) Outil chez moi en 5j    (3) Stack interne en 4-8 sem
Canal       : (1) LinkedIn outbound + contenu  (2) Contenu expert + bouche-à-oreille
              (3) Vente consultative + réseau pro
Concurrent  : RESET / LiveMentor (DFY) — n8n/Make consultants (DIY-S) — Big4/IA cabinets (DIY-A)
Prix        : (1) 890-1490€  (2) 1990-2990€ + 590€/an support  (3) 6990-9990€ + custom + 1990€/an
Verdict     : GO global — séquencement DFY → DIY-A → DIY-S
Pipeline    : Idea ✅ | Cadrage ✅ v2 | Persona ⬜ v2 | Market ⬜ v2 | Comp ⬜ v2 | Price ⬜ v2 | Final ⬜ v2
Statut      : GAMME 3 PORTES VALIDÉE — passer au persona dual
```

---

## 1. Idée en une phrase

**"Offer Pipeline" devient une marque parapluie qui propose 3 portes d'entrée à un même backend
de pipeline IA propriétaire : un livrable clé-en-main pour le freelance pressé (Offer Clarity),
une installation chez le consultant senior qui veut son outil (Pipeline Solo), et un déploiement
custom + intégrations CRM chez les cabinets et agences (Pipeline Studio).**

---

## 2. Architecture commerciale validée

```
                        ┌─────────────────────────┐
                        │   PIPELINE OFFER (BACKEND) │
                        │  skills + agents Claude   │
                        │  (asset propriétaire)     │
                        └────────────┬─────────────┘
                                     │
              ┌──────────────────────┼─────────────────────────┐
              │                      │                         │
              ▼                      ▼                         ▼
     ┌────────────────┐    ┌──────────────────┐    ┌──────────────────────┐
     │  OFFER CLARITY │    │  PIPELINE SOLO   │    │   PIPELINE STUDIO    │
     │  DFY freelance │    │  DIY freelance   │    │   DIY agence/cabinet │
     │  Livrable 48h  │    │  Install 5 jours │    │  Setup 4-8 semaines  │
     │  890-1490€     │    │  1990-2990€      │    │  6990-9990€ + custom │
     │  Cycle 3-14j   │    │  Cycle 14-30j    │    │  Cycle 60-180j       │
     └────────────────┘    └──────────────────┘    └──────────────────────┘
            │                       │                        │
            ▼                       ▼                        ▼
        Volume                    Marge                  Ancrage long
       (proof of value)         (autonomie)            (revenus pros)
```

**Positionnement parapluie :** "Offer Pipeline — Le pipeline IA de création d'offres B2B,
disponible en livrable, en install, ou en stack interne."

---

## 3. Verdict Devil's Advocate (gamme entière)

### ✅ Ce qui tient

1. **Backend unique → coût marginal de complexité maîtrisé.** Les 3 produits exploitent
   le même asset (skills offer-pipeline). Pas de R&D parallèle, pas de tech debt explosée.

2. **Effet de gamme positif.** Le DFY génère des cas clients et du contenu LinkedIn qui
   nourrissent la légitimité pour le DIY. L'inverse aussi : un cas DIY agence prestigieux
   (ex : un cabinet connu) légitime tout l'écosystème.

3. **Anti-cannibalisation naturelle.** Les 3 segments achètent pour des raisons différentes :
   - Julien (DFY) n'a pas le temps ni l'envie d'installer un outil
   - Marc (DIY-S) refuse explicitement le DFY parce qu'il veut le contrôle
   - Hélène (DIY-A) ne peut pas acheter du DFY (volumétrie + souveraineté)
   → Un client n'arbitre quasiment jamais entre deux portes, il choisit la sienne.

4. **Conformité contrainte no-SaaS.** L'architecture en setup + custom + support optionnel
   respecte la directive Jonathan (aucune dépendance hébergement, client souverain).

5. **Casse le plafond de revenus.** Le DFY seul plafonne à ~70k€/an.
   La gamme entière ouvre 100-300k€/an.

### ❌ Ce qui ne tient pas (encore)

1. **Risque d'éparpillement Jonathan en solo.** 3 produits × 1 personne = recette pour brûler
   l'attention. **Condition non négociable :** séquencer le go-to-market, pas tout lancer en parallèle.

2. **DIY agence = cycle de vente long (3-6 mois).** Tant qu'aucun cabinet pilote n'a signé,
   c'est un pari. Risque de passer 6 mois sans CA en attendant.

3. **Branding flou si tout est lancé en même temps.** "Offer Clarity" / "Pipeline Solo" /
   "Pipeline Studio" sous 3 marques distinctes ou 1 marque parapluie ? Décision branding à figer.

4. **Dépendance Anthropic / Claude Code.** Le backend repose sur un acteur tiers dont les CGU,
   prix et roadmap peuvent évoluer. À mitiger par contrat client (clauses upgrade) et mention
   explicite dans les propositions commerciales.

5. **Risque "agence qui revend" sur le DIY.** Une agence qui achète Pipeline Studio peut
   théoriquement revendre du DFY à ses propres clients — concurrent direct potentiel.
   À cadrer contractuellement (licence non revendable ou commission de prescripteur).

### ⚠️ Hypothèses non vérifiées (à lever en `/persona v2` et `/competitive v2`)

1. Volume réel du segment DIY freelance (Marc) : 30k profils → combien réellement actifs sur
   un cycle 12 mois ? À trianguler avec entretiens informels.

2. Volume réel du segment DIY agence (Hélène) : 1 500 cabinets cibles FR → combien avec
   maturité IA + budget setup IA dédié ? À valider via entretiens / benchmarks Cigref.

3. Modèle de licence DIY : forfait perpétuel ? Licence 12 mois renouvelable ? À trancher
   en pricing v2 selon analogies marché (Make, n8n, Zapier consultants).

4. Concurrence directe DIY agence : qui en France propose un setup pipeline IA "création
   d'offres" pour cabinets ? À scanner en `/competitive v2`.

### 🚧 Contraintes projet (réalité ressources)

- **Solo bootstrappé** + Uccello Hub en parallèle → bande passante limitée
- **Pas de notoriété sur ce service** (pipeline jamais vendu en externe)
- **Budget acquisition zéro** → contenu organique + outbound manuel + réseau
- **Compétences vente B2B sénior** : ✅ pour DIY-A (consultative), ✅ pour DFY (court),
  ⚠️ pour DIY-S (cycle moyen, cible un peu plus tech)

---

## 4. Checkpoint viabilité 1 — Intensité de la douleur (par archétype)

| Archétype | Score douleur | Déjà dépensé pour résoudre | Signal |
|-----------|:-------------:|---|---|
| DFY freelance (Julien) | 8/10 | Coachs 300-3000€, formations 500-3000€ | ✅ Prioritaire |
| DIY freelance (Marc) | 6/10 | Setups custom 1500-5000€, formations IA 500-2500€ | ✅ Mais latente |
| DIY agence (Hélène) | 7/10 | Outils SaaS 5-20k€/an, intégrateurs Hubspot 8-25k€ | ✅ Stratégique |

**Signal global : ✅ trois douleurs réelles, scorées différemment mais toutes monétisables.**

---

## 5. Direction recommandée — GO + séquencement

**[x] GO** — gamme à 3 portes, **séquencée** sur 12 mois.

### Plan de séquencement go-to-market (12 mois)

```
Mois 1-3 : Lancement DFY (Offer Clarity) — produit d'appel
   → 2-3 missions pilotes 490€ pour témoignages
   → 5-10 clients payants au prix plein
   → Contenu LinkedIn organique sur la douleur "offre floue"
   → Objectif : preuve sociale + 1er CA + apprentissages terrain

Mois 3-6 : Ouverture DIY agence (Pipeline Studio) — vente consultative
   → Activation réseau pro de Jonathan + ciblage 20-40 cabinets
   → Discovery calls, proposition sur mesure
   → Objectif : 1-2 clients pilotes (ticket 6-10k€) qui deviennent références

Mois 6-12 : Ouverture DIY freelance (Pipeline Solo) — alimenté par contenu
   → Lancement public quand le DFY a 5+ témoignages publics
   → Cible : power users IA déjà clients DFY ou contacts forum / Indie Hackers
   → Objectif : 3-5 clients payants Pipeline Solo
```

### Conditions non négociables avant d'ouvrir une nouvelle porte

| Étape | Condition pour activer la suivante |
|-------|------------------------------------|
| DFY → DIY-A | Au moins 3 témoignages DFY publics + une page de vente fonctionnelle |
| DIY-A → DIY-S | Au moins 1 client DIY agence livré et facturé + retour d'expérience documenté |

### Justification du séquencement

1. **Le DFY génère du flux** (volumétrie + témoignages + contenu) à coût d'acquisition quasi-nul.
2. **Le DIY-A a le meilleur ratio CA/effort** mais demande une légitimité construite — d'où DFY d'abord.
3. **Le DIY-S est le plus exigeant en marketing** (positionnement power user) — pertinent quand
   la marque est posée.
4. **Risque éparpillement** : on travaille **une porte à la fois**, sans ouvrir la suivante avant
   d'avoir validé la précédente.

---

## 6. Branding — décision pré-cadrage

**Recommandation : 1 marque parapluie + 3 noms de produit.**

```
Marque parapluie : "Offer Pipeline" (ou "Offer Pipeline by Uccello Labs")
   ├─ Produit DFY  : Offer Clarity
   ├─ Produit DIY-S: Pipeline Solo
   └─ Produit DIY-A: Pipeline Studio
```

**Pourquoi pas 3 marques distinctes ?** Coût d'acquisition × 3, dilution effort marketing,
pas d'effet d'échelle.

**Pourquoi pas 1 seul nom et 3 plans ?** Mauvais signal au marché — les 3 segments achètent
pour des raisons différentes. Un consultant senior n'achètera pas un produit qui s'appelle
"Clarity" (perçu débutant). Un cabinet n'achètera pas un produit qui sonne freelance.

→ **À valider/affiner en `/offer-final v2`.**

---

## 7. Questions prioritaires pour `/persona v2`

1. **Persona DFY (Julien) — conservation** : la v1 tient, on garde tel quel ?
   → Réponse attendue : oui, la v1 est solide, on la verse dans `PERSONA_ACHETEUR_DFY.md`.

2. **Persona DIY** : on dual-persona-ize en 1 doc avec 2 archétypes (Marc + Hélène) ou
   on fait 2 personas distincts ?
   → Recommandation : **2 personas distincts** car les comportements d'achat divergent
   radicalement (consultant vs direction cabinet) — un message marketing pour Marc ne
   parle pas à Hélène et vice-versa. Mais on peut grouper dans `PERSONA_ACHETEUR_DIY.md`
   avec 2 sections claires (Partie A / Partie B).
   → **Décision retenue v2 : 1 fichier `PERSONA_ACHETEUR_DIY.md` avec 2 sous-personas explicites**
   (conformément à la demande utilisateur "2 personas acheteur").

3. **Pour Marc (DIY freelance)** : quel est le déclencheur d'achat ? Lassitude des SaaS qui
   changent les CGU ? Désir de monter un cabinet ? Quête de souveraineté data ?

4. **Pour Hélène (DIY agence)** : qui est le décideur réel ? Direction (CEO/COO) ?
   Direction Innovation ? Head of Consulting ? Et quel est le sponsor IT (CIO) qui peut bloquer ?

5. **Quelle objection pèse le plus** sur DIY-A ? "Et si Anthropic ferme demain ?" /
   "Pourquoi pas un cabinet IA Big4 ?" / "On peut le faire en interne avec notre dev senior" ?

---

## 8. Points spécifiques à instruire en /market-research v2

- TAM/SAM/SOM séparés pour les 3 archétypes (le SAM 50k freelance v1 ne couvre que le DFY)
- Triangulation segment DIY agence : Syntec + AFCM + Hubspot Solutions Partners FR
- Maturité IA cabinets/agences FR : sources CIGREF, France Stratégie, BCG 2025
- Canaux d'acquisition différenciés par archétype

## 9. Points spécifiques à instruire en /competitive v2

- DIY-S : ajouter n8n/Make consultants, formations IA "build your stack", Indie Hackers stacks
- DIY-A : ajouter Big4 IA (Capgemini Invent, Onepoint), intégrateurs Hubspot/Salesforce
- DIY-A : ajouter cabinets IA spécialisés FR (ex : Artefact, Hub Institute, Quantmetry)
- Vérifier qu'aucun acteur ne propose déjà un "pipeline IA création d'offres" packagé pour cabinet

## 10. Points spécifiques à instruire en /pricing v2

- **Pas de SaaS** (contrainte non négociable)
- Modèles à instruire : forfait setup + custom au temps + support annuel optionnel
- Triangulation : Make/n8n consultants 1.5-5k€, Hubspot integrators 8-25k€, formations IA cabinet 5-20k€
- Question licence : perpétuelle ou 12 mois renouvelable ?
- Question "fee de mise à jour" si Anthropic publie de nouvelles versions
- ROI à articuler par archétype (Julien = 2 jours mission ; Marc = 1 client revendu ;
  Hélène = 2 jours/consultant × 50 missions/an)

---

## Prochaine étape : `/offer-persona v2`

→ Garder Julien (DFY) tel quel dans `PERSONA_ACHETEUR_DFY.md` (renommage de PERSONA_ACHETEUR.md v1)
→ Créer `PERSONA_ACHETEUR_DIY.md` avec **2 sous-personas** (Marc + Hélène) suivant la structure
   en 14 parties du skill /offer-persona, adaptée au format dual.

---

## Lien avec v1

- ✅ Conservé v1 : analyse douleur freelance, persona Julien, positionnement vs RESET/LiveMentor,
  pricing 890€/1490€ pour le DFY
- 🔄 Remplacé : architecture mono-offre → gamme 3 portes
- 🔄 Élargi : verdict GO sous conditions de **packaging seul** → GO sous conditions de **séquencement
  + branding parapluie**
- ➕ Ajouté : 2 nouveaux archétypes (Marc DIY-S, Hélène DIY-A), modèle économique no-SaaS,
  plan de séquencement 12 mois

---

## MARKET RESEARCH UPDATE v2
- Date : 2026-05-06 | Canaux retenus par archétype | MCP SIRENE : non sollicité (cible mixte personnes physiques + cabinets)

### A. DFY freelance (Julien) — inchangé v1

- TAM 1,2M freelances FR · SAM avec WTP : 144 000 · SAM profil Julien : 50 000 · SOM 12m : 20-80 clients
- Canal : LinkedIn outbound + contenu organique
- Source : Malt 2024, INSEE, Eurostat — sources v1 conservées

### B. DIY freelance (Marc) — nouveau

| Périmètre | Volume | Source | Méthode |
|-----------|:------:|--------|---------|
| TAM — Freelances/consultants seniors FR (5+ ans XP, profil business) | ~150 000 | INSEE + Malt 2024 (segment senior) | Estimé |
| SAM — Sous-segment "AI-curious" (early adopters IA) | ~25 000-40 000 | Triangulation LinkedIn search + benchmarks Indie Hackers FR + audience newsletters IA FR | Estimé |
| SAM — Avec budget 2-5k€ pour outil pro | ~8 000-15 000 | Sous-ensemble = freelances 1k+ TJM | Estimé |
| SOM 12m (Pipeline Solo, ticket 2-3k€, vente directe) | 8-25 clients | Estimation conservative cycle 14-30j | Estimé |

**Canal retenu :** Direct — contenu LinkedIn expert long format (2-3 posts/semaine sur le pipeline,
souveraineté IA, retours d'expérience clients DFY) + bouche-à-oreille via communauté DFY +
ciblage Indie Hackers/NoCode FR.

**Signaux de croissance :**
- Marché des "AI consultants" / "AI builders" en croissance forte (LinkedIn FR : +180% en 24m)
- Communautés FR power users IA (NoCode FR, Indie Hackers FR) en croissance régulière
- Demande "outil souverain" en hausse (rapports CNIL/Cigref 2025 sur la souveraineté data)
- Multiplication des stack-customs documentés sur ProductHunt et Hacker News

### C. DIY agence (Hélène) — nouveau

| Périmètre | Volume | Source | Méthode |
|-----------|:------:|--------|---------|
| TAM — Cabinets conseil + agences strat 5-30 personnes FR | ~7 000 | Syntec (~1 500 cabinets conseil) + AFCM (~3 000 agences) + estim. studios produit (~500) + équipes innovation PME (~2 000) | Triangulé |
| SAM — Avec maturité IA + budget setup IA dédié | ~1 500-2 500 | McKinsey AI Survey 2025 (78% cabinets ont engagé un projet IA), filtre taille | Estimé |
| SAM — Avec besoin spécifique "AI for offer/strategy production" | ~600-1 000 | Sous-ensemble conseil/strat (vs design/communication pure) | Estimé |
| SOM 12m (Pipeline Studio, ticket 8-18k€, vente consultative) | 5-15 clients | Cycle 60-180j × bande passante Jonathan | Estimé |

**Canal retenu :** Vente consultative via réseau pro Jonathan + recommandations + événements
ciblés (Cigref, Big Data & AI Paris, Transform). **Pas de cold outbound** — cycle trop long
pour un solo bootstrappé sans légitimité préalable. Légitimité construite via DFY (témoignages
publics) + contenu LinkedIn expert.

**Signaux de croissance :**
- 78% des cabinets conseil ont engagé un projet IA (McKinsey 2025)
- Marché des intégrateurs Hubspot Solutions Partners FR : forte croissance, tickets 5-30k€
- Pénurie de profils "AI engineer" → cabinets achètent du "AI install service" plutôt que recruter
- Sensibilité forte à la souveraineté data (rapports Cigref, France Stratégie 2025)
- Big4 IA (Capgemini Invent, Onepoint) saturés et chers → opportunité pour acteur agile

### Hypothèses validées / à valider terrain v2

| Hypothèse | Statut | Source |
|-----------|--------|--------|
| Volume DIY freelance ~25-40k profils FR | ⚠️ À trianguler terrain (entretiens informels Indie Hackers) | LinkedIn search + benchmarks |
| Volume DIY agence cabinets cibles ~1500-2500 FR | ⚠️ À valider via Syntec / AFCM / Cigref | Triangulation 3 sources |
| WTP DIY freelance : 2-5k€ pour install | ⚠️ À valider sur 5 entretiens informels | Analogie n8n/Make consultants |
| WTP DIY agence : 12-22k€ pour setup + custom | ⚠️ À valider sur 3-5 discovery calls cabinets | Benchmark Hubspot integrators |
| Cycle vente DIY agence 60-180j | ✅ Cohérent avec ventes consultatives B2B cabinet (~standard) | Standard conseil B2B |
| Souveraineté data = vrai déclencheur (vs argument marketing) | ⚠️ À valider terrain | Rapports Cigref 2025 |

### Checkpoint viabilité 3 v2 — Budget + Maturité (par archétype)

```
                     DFY Julien   DIY Marc   DIY Hélène
Budget dédié        : Oui ✅      Oui ✅     Oui ✅ (CODIR)
Maturité            : Éduqué ✅   Éduqué ✅  Émergente ⚠️
Décideurs           : 1           1          3-5 (chaîne)
Cycle closing       : 3-14j       14-30j     60-180j
Signal global       : ✅          ✅          ⚠️ Long mais haute valeur
```

### Décisions clés `/competitive v2`

- DIY-S : ajouter benchmark consultants n8n/Make/Zapier FR + cours/formations "AI for consultants"
- DIY-A : ajouter Big4 IA + intégrateurs Hubspot/Salesforce + cabinets IA spécialisés
  (Artefact, Quantmetry, Hub Institute, Onepoint AI, Capgemini Invent)
- Vérifier qu'aucun acteur ne propose **déjà** un "pipeline IA création d'offres B2B"
  packagé pour cabinet — si oui, repositionner.
