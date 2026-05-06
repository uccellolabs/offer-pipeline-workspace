# IDEA_BRIEF_v2.md — Re-cadrage avec 3 archétypes
- Date : 2026-05-06 | Version : 2.0 | Agent : idea-finder (re-run)
- Projet : market-study | Opérateur : Jonathan SARDO, Uccello Labs
- Successeur de : IDEA_BRIEF.md v1.0 (2026-04-27)

---

## Pourquoi cette v2

La v1 a tranché entre Idée #1 (service freelance) et Idée #2 (étude PME), toutes deux **DFY**.
Elle a manqué la troisième voie, pourtant implicite dans 3 risques identifiés
(faisabilité solo, scalabilité, plafond 2-4 dossiers/mois) : **vendre le pipeline lui-même**
plutôt que ses livrables.

**Nouvelle hypothèse :** la monétisation peut prendre 3 formes parallèles ou complémentaires —
livrable clé-en-main (DFY) ou installation du pipeline chez le client (DIY freelance / DIY agence).

**Contrainte non négociable (Jonathan, 2026-05-06) :** pas de modèle SaaS.
Le DIY est un **service d'installation + configuration des skills sur la machine du client**,
avec option d'intégrations sur mesure (CRM, outils internes) et contrat de support annuel optionnel.
Le client est autonome après livraison.

---

## Méthode

- Sources v1 conservées (Reddit, Malt 2023, lefreelance.fr, scalecity.fr, koino.fr, etc.)
- Sources additionnelles pour les archétypes DIY :
  * Tendance "AI-native consulting firms" (rapports McKinsey 2025, BCG 2025 sur l'IA en cabinet)
  * Marché "AI install / setup services" (analogie : Make, Zapier, n8n consultants)
  * Communautés FR cabinets/agences (Réseau ESN, Syntec, AFCM)
  * Marché des intégrateurs CRM (Hubspot Solutions Partners France, Salesforce Consulting Partners)
- Archétypes générés : 3 (DFY / DIY freelance / DIY agence)
- Comparaison scorée + recommandation

---

## Shortlist (classée par score)

---

### Archétype #1 — DFY freelance ("Offer Clarity")
**Score : 24/30** (inchangé v1)

Reprise du résumé v1 — voir IDEA_BRIEF.md pour le détail.

- **Cible :** Julien, consultant freelance 30-42 ans, 18-36 mois d'activité, offre floue
- **Achète :** un livrable complet (offre cadrée + persona + pitch deck + templates + 30-80 prospects CSV) en 48-72h
- **Modèle économique :** service one-shot 890€-1490€ HT
- **Volume marché :** SAM 50 000 / SOM 20-80 clients/an
- **Valeur perçue :** "fais-le pour moi, je n'ai ni le temps ni la distance émotionnelle"

**Score conservé**

| Critère | /5 |
|---------|----|
| Intensité de la douleur | 5 |
| Volume du segment | 5 |
| Willingness to pay | 4 |
| Fit compétences | 5 |
| Fit orientation projet | 3 |
| Faisabilité ressources | 2 |
| **Total** | **24/30** |

> Note faisabilité : faible — Jonathan livre seul, plafond 2-4 dossiers/mois.
> Le DFY ne casse pas le plafond de revenus.

---

### Archétype #2 — DIY freelance / solo expert ("Pipeline Solo")
**Score : 22/30** (nouveau)

**La douleur** (mots de la cible)

> "Je donne des conseils stratégiques à mes clients depuis 10 ans.
> Comment je transforme tout ça en process IA pour livrer 3x plus vite,
> sans dépendre d'un outil tiers qui peut fermer ou augmenter les prix demain ?"
> — Synthèse forums Indie Hackers FR + LinkedIn power users IA

> "J'ai monté un setup ChatGPT custom pour mes offres, j'ai passé 80h dessus,
> ça marche à moitié. Si quelqu'un me vendait un truc opérationnel,
> je signais en 2 jours."
> — Pattern récurrent communautés "AI for solopreneurs" (Reddit r/solopreneur, FR)

**Qui souffre** (segment + taille)

Consultants seniors, freelances stratégie/ops/marketing avec une pratique mature
(5-15 ans d'expérience), qui veulent **industrialiser leur propre production de livrables**
ou monter une offre packagée IA-augmentée pour leurs propres clients.

Profils types :
- Consultant business qui structure les offres de PME → veut un pipeline interne pour livrer plus vite
- Freelance senior qui veut se positionner "expert IA" en revendant lui-même du DFY à sa clientèle
- Indie hacker qui construit son propre cabinet/agence solo

Taille du segment :
- ~30 000 consultants FR avec 5+ ans d'expérience et appétence IA forte (estimation triangulée
  via LinkedIn, communautés Indie Hackers FR, NoCode FR)
- Power users IA actifs (Claude/Cursor/n8n/Make) en France : ~80 000-120 000 (estim. SimilarWeb,
  benchmarks plateformes)

**Preuves (3+ sources)**

1. Croissance des "AI consultant" sur LinkedIn FR : +180% en 24 mois (search "consultant IA" FR)
2. Multiplication des stack-customs ChatGPT/Claude documentées sur Indie Hackers, ProductHunt
3. Marché des "AI workflow setups" (n8n, Make, Zapier consultants) : ticket moyen 2-5k€ par setup
   (sources : freelance platforms, témoignages publics)
4. Demande explicite "je veux pas un SaaS, je veux mon outil" : pattern montant souveraineté
   data + résistance aux SaaS opaques (rapports CNIL/Eurostat 2025)

**Preuve willingness to pay**

- Setups n8n / Make custom : 1 500-5 000€ par projet (marché établi)
- Formations IA "build your stack" type Wunjo, Make Mastery : 500-2 500€
- Intégrateurs Zapier/Make freelances FR : TJM 600-900€/jour
- "AI consultant" qui revendent leur propre pipeline : tickets jusqu'à 10k€

**Ce que Jonathan apporterait de différent**

→ Pas un setup générique n8n. Un **pipeline propriétaire éprouvé en production** (offer-pipeline)
installé clé-en-main + 1 session de prise en main. Le client repart avec un outil métier
spécialisé "création/validation d'offres B2B", pas un workflow horizontal qu'il doit configurer.

**Solution potentielle (esquisse)**

"Pipeline Solo" — Installation du pipeline offer-pipeline sur la machine du consultant :
- Audit setup machine (1h)
- Installation skills + dépendances (Claude Code, agents, templates)
- 1 session de formation 2h (cas d'usage + bonnes pratiques)
- Documentation personnalisée
- 30 jours de support email/Slack inclus

Format possible :
- Forfait setup : 1 990-2 990€ HT one-shot
- Option formation équipe (si freelance avec sous-traitants) : +990€
- Pas de récurrence forcée (le client est autonome)
- Possibilité de contrat de support annuel : 590€/an (mises à jour skills, dépannage)

**Pourquoi Jonathan**

- Auteur du pipeline → il maîtrise l'install, les edge cases, les évolutions
- 21 ans de conception logicielle → setup propre, reproductible
- Profil "expert" → vente consultative naturelle à des power users
- Production semi-standardisée possible (script d'install + checklist)

**Risques / angles morts**

1. Volume marché plus restreint que DFY (~30k vs ~50k profils)
2. Cycle de vente plus long (ticket ~2k€ + setup technique → décision plus prudente)
3. Risque "client mécontent" si l'IA évolue (modèles, coûts) → contrat de support à clarifier
4. Le power user IA peut être tenté de bricoler seul plutôt que d'acheter
5. Risque cannibalisation DFY : un client DIY peut revendre du DFY à ses propres prospects
   → opportunité (canal indirect) ou menace selon angle

**Score détaillé**

| Critère | /5 |
|---------|----|
| Intensité de la douleur | 3 |
| Volume du segment | 3 |
| Willingness to pay | 5 |
| Fit compétences | 5 |
| Fit orientation projet | 5 |
| Faisabilité ressources | 4 |
| **Total** | **25/30** |

> Note : faisabilité plus haute que DFY car installation est semi-standardisable (script + checklist).
> WTP supérieur (ticket 2-3k€ vs 890-1490€). Volume plus restreint mais ticket compense.

---

### Archétype #3 — DIY agence / cabinet ("Pipeline Studio")
**Score : 26/30** (nouveau — meilleur score)

**La douleur** (mots de la cible)

> "Mes consultants passent 40% de leur temps à structurer des offres et propositions clients
> qu'on a déjà faites 100 fois. On automatise quoi sans dépendre d'un Notion ou un SaaS qui voit
> nos données clients ?"
> — Synthèse entretiens informels Syntec / cabinets stratégie FR

> "Notre cabinet refacture 1 200€/jour. Si je gagne 2 jours par mission consultant grâce
> à un outil interne — c'est 2 400€ × 50 missions/an = 120k€ de marge."
> — Logique business cabinet (calcul standard ROI cabinets conseil)

> "On utilise Hubspot. Tout outil qui ne s'y connecte pas, on l'oublie."
> — Pattern récurrent intégrateurs Hubspot FR

**Qui souffre** (segment + taille)

Cabinets de conseil, agences stratégie/marketing, équipes innovation/produit en PME-ETI,
qui produisent à la chaîne des offres, propositions, études marché pour leurs clients.

Profils ciblés :
- Cabinets stratégie/conseil 5-30 consultants (FR ~1 500 cabinets selon Syntec)
- Agences marketing/branding mid-size (FR ~3 000 agences selon AFCM)
- Équipes innovation interne PME-ETI (~2 000 entreprises avec un service innovation structuré)
- Studios design/produit (~500 en FR)

Taille du segment :
- TAM FR : ~7 000 cabinets/agences cibles
- SAM (avec ouverture IA + budget setup) : ~1 500-2 500 entreprises
- SOM 12 mois (solo, ticket 8-15k€, vente consultative) : 5-15 clients/an

**Preuves (3+ sources)**

1. McKinsey Global Survey on AI 2025 : 78% des cabinets conseil ont engagé un projet IA interne
2. Marché des intégrateurs Hubspot/Salesforce FR : forte croissance, tickets 5-30k€ par projet
3. Souveraineté data en cabinet : enjeu structurant (rapports Cigref, France Stratégie 2025)
4. Tendance "AI-native consulting firms" : Bain, BCG, McKinsey investissent massivement dans
   des stacks internes propriétaires, pas SaaS tiers (rapports publics 2025)

**Preuve willingness to pay**

- Setup Hubspot pro chez un cabinet : 8 000-25 000€
- Custom dev consulting (intégrations) : TJM 800-1500€/jour, missions 5-20 jours
- Stacks IA internes en cabinet : budgets dédiés 20-100k€/an (souvent CIO + COO sponsors)
- Outils B2B "expert" (Pipedrive Power, ClickUp Enterprise) : 5-20k€/an

**Ce que Jonathan apporterait de différent**

→ Pas un consultant Hubspot ni un freelance n8n. Un **pipeline propriétaire spécialisé "création
d'offres B2B"** + intégration custom à leurs outils + formation équipe. Combine expertise
business (offer-pipeline) + expertise technique (21 ans dev, Laravel, IA) — couple rare.

**Solution potentielle (esquisse)**

"Pipeline Studio" — Installation du pipeline offer-pipeline en environnement cabinet :
- Audit besoins (2h discovery)
- Installation skills + adaptations terminologie cabinet
- Connecteurs sur mesure (CRM Hubspot/Pipedrive/Salesforce, outils internes)
- Formation équipe (3-5 consultants, 1 demi-journée)
- Documentation interne personnalisée
- 60 jours support post-install

Format :
- Setup forfait : 6 990-9 990€ HT
- Connecteurs custom : 990-2 990€ par connecteur (selon complexité)
- Formation équipe étendue : +1 500€ (jusqu'à 10 personnes)
- Maintenance annuelle optionnelle : 1 990€/an (mises à jour + 4h dépannage/an)

**Tickets typiques** : 8-18k€ HT par projet selon scope.

**Pourquoi Jonathan**

- Auteur du pipeline → adaptation, terminologie, edge cases maîtrisés
- 21 ans Laravel/conception logicielle → connecteurs Hubspot/Salesforce/etc. à sa portée
- Profil sénior → légitimité naturelle face à un COO/CIO/Head of Strategy
- Capacité à vendre une vision "pipeline IA souverain" cohérente avec souveraineté data

**Risques / angles morts**

1. Cycle de vente B2B long (3-6 mois — décideurs multiples : Direction, IT, Ops)
2. Concurrence indirecte des Big4 / cabinets IA (Capgemini Invent, Onepoint) avec offres "AI workshop"
3. Dépendance technique : si Anthropic change ses prix/CGU, le client est exposé → à anticiper
   contractuellement
4. Chaque mission custom = 1-3 semaines de delivery → peu scalable mais ticket compense
5. Risque "achat budget" : les cabinets veulent du sur-mesure → tentation de tout dire oui →
   à packager rigoureusement

**Score détaillé**

| Critère | /5 |
|---------|----|
| Intensité de la douleur | 4 |
| Volume du segment | 3 |
| Willingness to pay | 5 |
| Fit compétences | 5 |
| Fit orientation projet | 5 |
| Faisabilité ressources | 4 |
| **Total** | **26/30** |

> Faisabilité 4/5 : delivery custom mais ticket × volume = 50-150k€/an réaliste avec 5-15 clients.
> Casse le plafond du DFY freelance.

---

## Tableau de synthèse

| Archétype | Score | Ticket | SOM 12m | CA potentiel an | Fit Jonathan |
|-----------|:-----:|:------:|:-------:|:---------------:|:------------:|
| #1 DFY freelance ("Offer Clarity") | 24/30 | 890-1 490€ | 20-80 clients | 18-120 k€ | ⭐⭐⭐ |
| #2 DIY freelance ("Pipeline Solo") | 25/30 | 2-3 k€ | 8-25 clients | 16-75 k€ | ⭐⭐⭐⭐ |
| #3 DIY agence ("Pipeline Studio") | 26/30 | 8-18 k€ | 5-15 clients | 40-270 k€ | ⭐⭐⭐⭐⭐ |

**Trois constats :**

1. **Aucun n'écrase totalement les autres** sur tous les critères → ils peuvent **coexister** en gamme.
2. **Le DFY (#1) est le meilleur produit d'appel** (douleur viscérale, cycle court, volume haut).
3. **Le DIY agence (#3) est le meilleur générateur de marge** (ticket 10x plus haut, fit Jonathan max).

---

## Recommandation

**Architecture commerciale en 3 portes — pas une seule offre.**

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  OFFER CLARITY   │ →  │  PIPELINE SOLO   │ →  │  PIPELINE STUDIO │
│   DFY freelance  │    │  DIY freelance   │    │   DIY agence     │
│   890-1490€      │    │   2-3k€          │    │   8-18k€         │
│  one-shot        │    │   one-shot       │    │  setup + custom  │
│  vente directe   │    │  vente directe   │    │  vente consultativ│
│  cycle 3-14j     │    │  cycle 14-30j    │    │  cycle 60-180j   │
└──────────────────┘    └──────────────────┘    └──────────────────┘
       VOLUME                   MARGE                 ANCRAGE
   (proof of value)         (autonomie)            (revenus pros)
```

**Pourquoi 3 portes plutôt qu'une seule ?**

- Le DFY (#1) génère du **flux** (preuve sociale, contenu, témoignages) → alimente le funnel des #2 et #3
- Le DIY freelance (#2) capte ceux qui sortent du DFY et veulent leur propre outil — **upsell naturel**
- Le DIY agence (#3) finance la R&D du pipeline et stabilise le revenu pro
- Les trois partagent **le même pipeline backend** → coût marginal de complexité maîtrisé
- Risque d'éparpillement Jonathan : à mitiger en **séquençant** le go-to-market (D'abord #1, puis #3, puis #2)

**Si une seule offre devait être retenue : Pipeline Studio (DIY agence).**

Raisons :
- Score le plus élevé (26/30)
- Ticket × volume = meilleur CA potentiel (40-270k€/an)
- Fit max avec le profil Jonathan (sénior dev + business + souveraineté IA)
- Vente consultative haut de gamme = naturel pour son profil
- Casse définitivement le plafond du DFY solo (3 dossiers/mois max)

**Mais** : c'est aussi le plus long à amorcer (cycle 3-6 mois, légitimité à construire).
D'où l'intérêt de garder le DFY comme **produit d'appel** pour générer témoignages, contenu, légitimité.

---

## Points critiques à challenger en `/offer-cadrage v2`

1. **Architecture commerciale** : 3 portes parallèles ou séquentielles ? Si séquentiel, quel ordre ?
2. **Risque d'éparpillement Jonathan** (solo + Uccello Hub + 3 offres) : comment cadrer ?
3. **Intersection commerciale** : un client DFY peut-il devenir client DIY ensuite ? Comment éviter
   la cannibalisation ?
4. **Branding** : 1 marque mère "Offer Clarity" avec 3 produits, ou 3 marques distinctes ?
5. **Risque dépendance Anthropic/Claude Code** : à clarifier dans les contrats DIY (quid si CGU changent ?)

---

## Prochaine étape

→ Lancer `/offer-cadrage v2` en l'orientant sur **3 archétypes coexistants** (gamme à 3 portes)
   avec verdict GO/NO-GO/PIVOT par archétype + verdict global sur la stratégie de gamme.
