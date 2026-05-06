# OFFER_FINAL_v2.md
- Date : 2026-05-06 | Version : 2.0 | Agent : offer-final (re-run gamme 3 portes)
- Destinataire : Client final (3 archétypes — page de gamme + 3 pages produit)
- Format : Page de gamme + fiches produits / one-pagers
- Statut : PRÊT À UTILISER — recommandation séquencement go-to-market validée
- Successeur de : OFFER_FINAL.md v1.0 (2026-04-27)

---

## Synthèse pipeline v2

```
Idée        : Gamme à 3 portes — DFY freelance + DIY freelance + DIY agence
Backend     : Pipeline IA propriétaire offer-pipeline (skills + agents Claude)
Cibles      : Julien (DFY) | Marc (DIY-Solo) | Hélène (DIY-Studio)
Problèmes   : Offre floue (DFY) | Bricolage IA fragile (DIY-S) | Pas d'outil interne IA souverain (DIY-A)
Valeurs     : Livrable 48-72h | Install machine 5j | Setup cabinet 8-10 sem
Canaux      : LinkedIn (DFY) | Contenu expert+IH (DIY-S) | Réseau pro (DIY-A)
Concurrents : RESET/LiveMentor (DFY) | n8n consultants/OSS (DIY-S) | Big4 IA / boutique (DIY-A)
Prix        : 890-1490€ | 1990-2990€ + 590€/an | 6990-9990€ + custom + 1990-3990€/an
Verdict     : ✅ VIABLE — gamme cohérente, séquencement DFY → DIY-A → DIY-S sur 12 mois
Pipeline    : Idea ✅v2 | Cadrage ✅v2 | Persona ✅v2 | Market ✅v2 | Comp ✅v2 | Price ✅v2 | Final ✅v2
Statut      : OFFRE GAMME PRÊTE — passer aux supports (pitch deck, prospection, website)
```

---

## Score de viabilité globale v2

```
Critère 1 — Douleurs intenses et prioritaires
  DFY Julien     : 8/10 (douleur viscérale, bien documentée)
  DIY Marc       : 6/10 (latente — déclencheur "stack fragile + souveraineté")
  DIY Hélène     : 7/10 (stratégique — ROI consultants + différenciation cabinet)
  Signal global  : ✅ Trois douleurs réelles et monétisables

Critère 2 — Cibles concrètement prospectables
  DFY Julien     : 9/10 (LinkedIn massif)
  DIY Marc       : 7/10 (contenu expert + Indie Hackers)
  DIY Hélène     : 6/10 (réseau pro + événements, cycle long)
  Signal global  : ✅ Avec séquencement DFY d'abord (volume) puis Hélène (réseau pro)

Critère 3 — Marché avec budget et maturité
  DFY Julien     : ✅ Marché éduqué, paie déjà
  DIY Marc       : ✅ Power users ont budget pour outil pro
  DIY Hélène     : ✅ Cabinets ont budget IA dédié (78% engagés selon McKinsey 2025)
  Signal global  : ✅ Tous matures, maturité progressive

VERDICT GLOBAL  : ✅ VIABLE — gamme cohérente, séquencée, no-SaaS aligné contrainte Jonathan
```

**Conditions non négociables :**

1. **Séquencer le go-to-market** — pas tout lancer en parallèle. DFY (M1-3) → DIY-A (M3-6) → DIY-S (M6-12).
2. **Valider DFY par 2-3 missions pilotes** avant d'ouvrir DIY-A (preuve sociale + témoignages).
3. **Valider DIY-A par 1 client pilote signé** avant d'ouvrir DIY-S (référence cabinet).
4. **Brander en parapluie** ("Offer Pipeline" + 3 produits nommés) — pas 3 marques distinctes.
5. **Cadrer la dépendance Anthropic** dans les contrats DIY (clauses upgrade + support migration).
6. **Plafonner la production solo** : 3 dossiers DFY/mois max + 1 setup DIY en cours simultané.

---

## ⚠️ Points de vigilance exécution

| Point | Statut | Action recommandée |
|-------|--------|--------------------|
| Capacité Jonathan solo | ⚠️ Plafond physique | Plafonner 3 DFY/mois + 1 DIY en cours. Pas plus. |
| Zéro cas client aujourd'hui | ⚠️ Friction maxi | M1-2 : 2 missions DFY pilotes 490€ + 1 DIY-A pilote tarif réduit (5990€) |
| Branding | ⚠️ À figer | "Offer Pipeline" parapluie + Offer Clarity / Pipeline Solo / Pipeline Studio |
| Dépendance Anthropic | ⚠️ Risque structurel | Clauses contrat client + maintenance optionnelle qui couvre breaking changes |
| Risque revente DIY → concurrence DFY | ⚠️ À cadrer | Clause licence non revendable par défaut + option licence revendeur séparée si demande |

---

# L'OFFRE — Gamme Offer Pipeline

---

## Page de gamme (parapluie)

### Titre parapluie

**Le pipeline IA de création d'offres B2B
disponible en livrable, en install, ou en stack interne.**

*Choisis ta porte — 3 produits, 1 backend éprouvé en production.*

---

### Pourquoi 3 portes ?

Tu n'achètes pas la même chose selon où tu es. Un freelance qui veut un livrable
n'achète pas la même chose qu'un consultant senior qui veut son outil, ni qu'un cabinet
qui veut une stack interne.

Trois produits, un même backend : le pipeline offer-pipeline éprouvé en production
sur la création d'offres commerciales B2B.

---

### Tableau comparatif

| | **Offer Clarity** | **Pipeline Solo** | **Pipeline Studio** |
|--|:----------------:|:-----------------:|:-------------------:|
| **Pour qui** | Consultant freelance, 1-3 ans d'activité, offre floue | Consultant senior power user IA qui veut son outil | Cabinet 5-30 consultants qui veut une stack interne souveraine |
| **Tu reçois** | Un livrable (offre, persona, pitch deck, prospects) | L'install du pipeline sur ta machine | Le pipeline en stack interne + intégrations CRM |
| **En combien de temps** | 48-72h | 5-10 jours | 6-10 semaines |
| **Prix** | **890-1 490€** | **1 990-2 990€** | **6 990-9 990€ + custom** |
| **Modèle** | Forfait one-shot | Forfait setup + support optionnel | Setup + custom + maintenance optionnelle |
| **Tu es autonome après** | Tu utilises les livrables | Tu utilises ton install | Tes consultants utilisent l'outil |
| **Page produit** | [Offer Clarity →](#offer-clarity-dfy-freelance) | [Pipeline Solo →](#pipeline-solo-diy-freelance) | [Pipeline Studio →](#pipeline-studio-diy-agence) |

---

# Offer Clarity (DFY freelance)

> ✅ **Tier recommandé : Clarity Pro 1 490€ HT**

## 1. Titre

**Tu sors de la mission vendredi.
Ton offre est cadrée, tes supports sont prêts, ta liste de 50 prospects qualifiés est dans ta boîte mail.
Lundi matin, tu prospectes.**

*Service de packaging commercial pour consultants et freelances indépendants.*

## 2. Problème

Tu sais faire ton métier. Tes clients sont contents quand tu travailles avec eux.
Mais quand tu dois expliquer ce que tu fais à quelqu'un de nouveau — ça ne prend pas.

Tu essaies de te présenter. Ils hochent la tête poliment. On passe à autre chose.

La mission se termine. Tu n'as rien préparé pour la prochaine. Tu repars de zéro,
épuisé, au moment exact où il faudrait prospecter.

Tu as essayé de "définir ton offre" seul. Plusieurs fois. Tu n'as jamais terminé.

Ce n'est pas un problème de compétence. C'est un problème de distance émotionnelle :
on ne se cadre pas soi-même.

## 3. Pourquoi les solutions actuelles ne suffisent pas

Tu peux prendre un coach : 6 semaines, 1 900-2 500€. Tu sors avec un process.
Mais ta liste de prospects ? Tu la construis après, seul.

Tu peux suivre une formation. 3-4 mois de vidéos. Tu sors avec des connaissances.
Et le temps de tout appliquer, c'est encore 3 mois.

Tu peux le faire avec ChatGPT. Tu sais que tu ne le finiras pas.

## 4. Solution — Offer Clarity

**En une session de 2h, je structure ton offre et je livre en 48-72h
le package complet pour commencer à prospecter immédiatement.**

Ce que tu reçois :
- ✅ Ton offre cadrée (formulée pour ton acheteur, sans jargon)
- ✅ Ton persona acheteur
- ✅ Ton pitch deck HTML (12 slides)
- ✅ Tes templates LinkedIn + email (3 à 5 chacun)
- ✅ Ta liste de prospects qualifiés CSV (30 à 80 profils)

## 5. Prix

| | **Clarity** | **Clarity Pro** ⭐ |
|--|:----------:|:------------------:|
| **Prix** | **890€ HT** | **1 490€ HT** |
| Délai | 48h | 72h |
| Liste prospects | 30 CSV | 80 CSV |
| Analyse concurrence + battlecard | ❌ | ✅ |
| Recommandations pricing | ❌ | ✅ |
| Session suivi à 30 jours | ❌ | ✅ |

**Option mise à jour trimestrielle : 390€ HT** — nouvelle liste prospects + revue offre.

**ROI :** 1 client à 700€/jour × 2 jours de mission = service amorti.

## 6. Pour qui — Offer Clarity n'est pas pour toi si

- Tu viens de te lancer (<6 mois)
- Tu as déjà une offre claire + prospection active
- Tu cherches un coaching de plusieurs semaines

## 7. Appel à l'action

**Réserve une session de cadrage de 30 min — offerte, sans engagement.**

→ [Calendrier]

---

# Pipeline Solo (DIY freelance)

> ✅ **Tier recommandé : Solo + Custom 2 990€ HT**

## 1. Titre

**Tu as essayé de monter ton stack IA seul. 18 mois plus tard, ça marche à moitié.
Pipeline Solo, c'est mon pipeline propriétaire, installé sur ta machine, opérationnel
vendredi prochain — formé, documenté, à toi pour toujours.**

*Setup pipeline IA propriétaire pour consultant senior et freelance expert.*

## 2. Problème

Tu vends de l'IA à tes clients. Tu utilises Claude, GPT, Cursor, n8n, Make. Tu as monté
un setup maison sur 12-18 mois. Ça marche à 70%. Quand tu dois livrer une étude marché
complète, tu fais 5 prompts à la main, tu recopies, tu reformates. Le temps que tu gagnes
avec l'IA, tu le perds en plomberie.

Tu refuses ChatGPT Enterprise (données clients dans un cloud opaque), tu refuses les
formations "Build Your AI Stack" (tu sais déjà faire), tu veux **l'outil opérationnel
chez toi** — pas une compétence à acquérir, pas un SaaS qui te lâche demain.

## 3. Pourquoi les solutions actuelles ne suffisent pas

**Setup maison** : tu y as passé 80h. Le résultat est fragile, non versionné, pas reproductible.

**Frameworks open-source (CrewAI, LangChain)** : il faut tout intégrer toi-même. 80h+ de plomberie
avant qu'un workflow tourne. Et zéro méthodologie business derrière.

**Cours / formations IA** : tu n'as pas besoin d'apprendre — tu as besoin de l'outil.

**Consultants n8n / Make freelance** : ils livrent des workflows horizontaux. Pas un pipeline
propriétaire spécialisé "création d'offres B2B" éprouvé en production.

## 4. Solution — Pipeline Solo

**J'installe sur ta machine le pipeline offer-pipeline propriétaire (skills + agents Claude),
adapté à ta terminologie, avec une session de prise en main de 2h. En 5 à 10 jours, opérationnel.**

Ce que tu reçois :
- ✅ Audit de ton setup (1h-1h30 visio)
- ✅ Installation pipeline + 14 skills + agents Claude
- ✅ Configuration des templates par défaut
- ✅ (Pro) Personnalisation terminologie / 1 secteur métier
- ✅ (Pro) 1 connecteur léger (Notion, Drive, ou autre outil de ton choix)
- ✅ Session de formation 2h-2h30 sur cas réel
- ✅ Documentation personnalisée
- ✅ Support email/Slack 30-60 jours

## 5. Prix

| | **Solo** | **Solo + Custom** ⭐ |
|--|:------:|:--------------------:|
| **Prix** | **1 990€ HT** | **2 990€ HT** |
| Audit besoins | 1h | 1h30 |
| Installation pipeline + skills | ✅ | ✅ |
| Personnalisation terminologie | ❌ | ✅ |
| Connecteur léger (1 outil) | ❌ | ✅ |
| Formation prise en main | 2h | 2h30 |
| Support inclus | 30 jours | 60 jours |
| Délai de livraison | 5 jours | 7-10 jours |

**Option support annuel : 590€ HT/an**
Mises à jour pipeline + breaking changes Anthropic + 4h dépannage/an.
*Optionnel — le pipeline tourne sans.*

**ROI :** 2,5 jours de ton TJM. 1 mission gagnée grâce à la rapidité = ROI immédiat.

## 6. Pour qui — Pipeline Solo n'est pas pour toi si

- Tu débutes avec l'IA (achète plutôt Offer Clarity)
- Tu veux apprendre comment construire un pipeline (achète une formation)
- Tu n'as pas l'usage récurrent (1-2 missions IA-augmentées/an minimum recommandé)

## 7. Garanties

- **Pipeline éprouvé** : 2 ans en production sur des offres B2B réelles
- **Souverain** : tout chez toi, aucune donnée Uccello, RGPD ok
- **Évolutif** : skills modulaires, tu peux ajouter / modifier toi-même

## 8. Appel à l'action

**Réserve une session de découverte de 30 min — offerte.**

On regarde ton setup actuel et on définit le scope d'install.

→ [Calendrier]

---

# Pipeline Studio (DIY agence)

> ✅ **Tier recommandé : Studio Pro 9 990€ HT + custom selon scope**

## 1. Titre

**Vos consultants seniors passent 30-40% de leur temps à structurer des offres,
des cadrages et des études marché. Pipeline Studio installe dans votre cabinet
le pipeline IA propriétaire qui les fait gagner 2 jours par mission.
Souverain, intégré à votre Hubspot, opérationnel en 8-10 semaines.**

*Setup pipeline IA propriétaire pour cabinets de conseil et agences 5-30 consultants.*

## 2. Problème

Vos consultants seniors sont à 1 200€ TJM. Ils passent 30-40% de leur temps à structurer
des cadrages d'offres, des notes de positionnement, des études concurrence — qu'ils ont
faits 50 fois.

Vous avez engagé une initiative IA il y a 12 mois : ChatGPT Enterprise testé, formation
1-2 jours, GPTs custom lancés. **Adoption moyenne : 2-3 prompts par semaine par consultant.**
L'IA reste un gadget, pas un levier industriel.

Les Big4 (Capgemini Invent, Onepoint AI) vous proposent des projets de transformation à
60-200k€ sur 6-12 mois. Hors budget, hors timeline. Les cabinets IA boutique
(Fabernovel, Datawise) à 20-80k€ font du sur mesure que vous devez ensuite maintenir
vous-même. Et recruter un AI engineer interne : 6 mois de rampup, pénurie marché.

Vous voulez un **outil**. Pas un projet. Pas une formation. Pas un POC à industrialiser.

## 3. Pourquoi les solutions actuelles ne suffisent pas

| Solution | Limite |
|----------|--------|
| Big4 IA (Capgemini, Onepoint, Sopra Steria) | 60-200k€, 6-12 mois, projet de transformation pas un outil |
| Cabinets IA boutique (Fabernovel, Datawise, Ekimetrics) | 20-80k€, POC sur mesure que vous maintenez ensuite |
| ChatGPT Enterprise / Microsoft Copilot | Outil horizontal, adoption stagne, pas de pipeline métier |
| Recrutement AI engineer interne | 6 mois de rampup, pénurie, salaire 80-120k€/an |
| Continuer GPTs custom | Adoption stagne à 2-3 prompts/semaine/consultant |

## 4. Solution — Pipeline Studio

**J'installe dans votre cabinet le pipeline offer-pipeline propriétaire, adapté à votre
terminologie, connecté à votre CRM, avec formation de 5-10 consultants. En 6-10 semaines,
opérationnel. Vous restez propriétaires.**

Ce que vous recevez :

- ✅ Discovery audit (2-4h, 1-2 sessions)
- ✅ Installation pipeline complet + 14 skills + agents Claude
- ✅ Adaptation terminologie cabinet (vocabulaire missions, livrables, méthodes)
- ✅ Connecteurs CRM/outils inclus (1 ou 2 selon tier)
- ✅ Templates secteur (1 à 3 secteurs métier)
- ✅ Formation équipe (1 demi-journée à 1 journée, 5-10 personnes)
- ✅ Documentation interne personnalisée + playbook (Pro)
- ✅ Support post-livraison 60-90 jours + 2 sessions de revue J+30/J+60 (Pro)

## 5. Prix

| | **Studio Essentials** | **Studio Pro** ⭐ |
|--|:--------------------:|:------------------:|
| **Setup** | **6 990€ HT** | **9 990€ HT** |
| Discovery | 2h | 4h |
| Connecteurs inclus | 1 | 2 |
| Templates secteur | 1 | 2-3 |
| Formation équipe | demi-journée / 5 pax | journée / 10 pax |
| Documentation | Standard | Personnalisée + playbook |
| Support inclus | 60 jours | 90 jours + revue J+30/J+60 |
| Délai | 6-8 semaines | 8-10 semaines |

### Custom au temps (au-delà du setup)

| Type de custom | Durée typique | Tarif (1 200€/j) |
|----------------|:-------------:|:-----------------:|
| Connecteur CRM additionnel (Pipedrive, Salesforce, Sellsy) | 2-4j | 2 400-4 800€ |
| Connecteur outil interne (API custom client) | 3-7j | 3 600-8 400€ |
| Adaptation skill secteur (ex : pharma) | 2-5j | 2 400-6 000€ |
| Formation équipe étendue (>10 ou multi-sites) | 1-2j | 1 200-2 400€ |

### Maintenance annuelle optionnelle

| | **Standard** | **Pro** |
|--|:-----------:|:-------:|
| **Prix** | **1 990€/an** | **3 990€/an** |
| Mises à jour pipeline | ✅ | ✅ |
| Adaptation breaking changes Anthropic | ✅ | ✅ |
| Heures dépannage incluses | 4h/an | 12h/an |
| Session de revue annuelle | 1h | 2h + atelier équipe |
| Priority support | 5j | 24h ouvré |

**Tickets typiques :**
- Cabinet 5-10 consultants, simple : **9-12 k€** an 1
- Cabinet 10-20 consultants, intégrations CRM : **16-22 k€** an 1
- Cabinet 20-30 consultants, multi-connecteurs : **22-30 k€** an 1

**ROI :** Cabinet 8 consultants × 2 jours/mois économisés × 1 200€ TJM = **19 200€/mois** de
capacité libérée. Pipeline Studio amorti en **1-2 mois** si l'adoption tient.

## 6. Pour qui — Pipeline Studio n'est pas pour vous si

- Vous êtes un cabinet 1-4 personnes (achetez Pipeline Solo)
- Vous cherchez un projet de transformation IA complet (Big4 vous conviendra mieux)
- Vos consultants ne produisent pas régulièrement des offres / études / cadrages
- Vous n'avez pas de sponsor IA interne (CIO ou directeur innovation)

## 7. Garanties

- **Souverain** : tout sur votre infrastructure, aucune donnée client chez Uccello
- **Adoption** : adoption checklist 30j + 2 sessions de revue (Pro) — si l'adoption ne tient pas, on ajuste
- **Portable** : skills modulaires, vous restez propriétaires, pas de dépendance Uccello pour l'usage
- **Couverture API** : maintenance optionnelle couvre breaking changes Anthropic

## 8. Appel à l'action

**Discovery call de 60 min — gratuit.**

On scope vos besoins (volume offres/an, intégrations CRM nécessaires, équipe à former) et
on cale un devis structuré pour validation CODIR.

→ [Calendrier discovery]

---

## Preuves communes (toutes portes)

**Jonathan SARDO — fondateur Uccello Labs**
- 21 ans de conception logicielle B2B (Laravel, architecture SaaS)
- Auteur du pipeline offer-pipeline (utilisé en production sur 12+ projets internes)
- Ex-architecte sénior plusieurs ESN et scale-ups françaises

> *Note : la gamme Offer Pipeline est en lancement public à partir de mai 2026. Les premières
> missions de chaque porte sont proposées à un tarif pilote (490€ DFY / 1490€ DIY-S /
> 5990€ DIY-A) en échange d'un témoignage détaillé.*

---

## Cahier des objections cross-portes

### Sur la dépendance Anthropic / Claude

> "Le pipeline est conçu pour évoluer. Les skills sont modulaires et documentés. Vous gardez
> votre install si Anthropic publie une rupture API ; le contrat de support optionnel
> couvre la migration. Sans contrat, vous avez la doc — ou vous me rappelez ponctuellement."

### Sur la souveraineté des données

> "Tout est installé chez vous (Pipeline Solo / Studio) ou produit en off-platform et livré
> (Offer Clarity). L'API Anthropic est appelée pour la génération mais aucune donnée client
> n'est stockée chez Uccello. RGPD ok, audit possible."

### Sur le ROI

> "DFY : amorti en 2 jours de mission consultant. Solo : amorti en 2,5 jours TJM consultant
> senior. Studio : amorti en 1-2 mois de capacité consultants libérée."

---

## Sources utilisées

- IDEA_BRIEF_v2.md (3 archétypes, 2026-05-06)
- OFFER_BRIEF_v2.md (cadrage gamme + market research v2, 2026-05-06)
- PERSONA_ACHETEUR_DFY.md (Julien — issu de v1)
- PERSONA_ACHETEUR_DIY.md (Marc + Hélène, 2026-05-06)
- COMPETITIVE_BRIEF_v2.md (n8n + Big4 + cabinets IA, 2026-05-06)
- PRICING_BRIEF_v2.md (modèles Service + Setup + Setup custom, no-SaaS, 2026-05-06)

---

## Checklist FAISABILITÉ v2

- [x] Backend (pipeline) déjà éprouvé en production interne → pas de R&D bloquante
- [x] Capacité Jonathan compatible (3 DFY/mois + 1 DIY simultané) → plafond physique géré
- [x] Compétences techniques pour custom (Laravel + connecteurs CRM) → ✅
- [x] Compétences vente B2B sénior pour DIY-A → ✅ (à mi-chemin)
- [x] Budget acquisition zéro compatible avec canal LinkedIn + réseau pro → ✅
- [x] Contrainte no-SaaS respectée sur les 3 portes → ✅
- [x] Conformité RGPD via install client → ✅
- [ ] Cas client réel sur chaque porte → à construire (M1-3 DFY, M3-6 DIY-A, M6-12 DIY-S)

---

## Checklist QUALITÉ v2

- [x] Page de gamme cohérente (parapluie + 3 produits)
- [x] Chaque porte a son titre, son problème, sa solution distincte
- [x] Pricing clair par porte avec tier recommandé identifié
- [x] Concurrents mentionnés et reframés par porte
- [x] Objections anticipées (par porte + cross-portes)
- [x] CTA unique par porte (session découverte / discovery call)
- [x] Aucun superlatif non prouvé
- [x] Preuve honnête (phase pilote signalée explicitement)
- [x] Souveraineté data explicite pour DIY-S et DIY-A

---

## Plan de lancement go-to-market (12 mois)

### Mois 1-3 — Lancement Offer Clarity (DFY)

- Sem 1-2 : 2 missions pilotes 490€ → 2 témoignages détaillés publics
- Sem 3-6 : Page Offer Clarity + 3 posts LinkedIn/sem sur la douleur "offre floue"
- Sem 7-12 : LinkedIn outbound 20-30 profils Julien/sem + conversion en sessions découverte
- **Objectif M3 :** 5-10 clients DFY payants au prix plein, 3+ témoignages publics

### Mois 3-6 — Ouverture Pipeline Studio (DIY-A)

- Activation réseau pro Jonathan + identification 20-40 cabinets cibles
- Création page Pipeline Studio + 1 post LinkedIn long format/sem (positionnement expert)
- 2-3 discovery calls cabinets/sem
- Mise en place 1 mission pilote DIY-A à tarif réduit (5 990€ + 1 connecteur Hubspot offert)
- **Objectif M6 :** 1-2 cabinets pilotes signés, 1 référence cabinet publiable

### Mois 6-12 — Ouverture Pipeline Solo (DIY-S)

- Lancement public Pipeline Solo quand DFY a 5+ témoignages + 1 cabinet référence DIY-A
- Cible : power users IA déjà clients DFY ou contacts forum / Indie Hackers / NoCode FR
- Contenu LinkedIn 2-3 posts/sem sur la souveraineté + cas Pipeline Solo
- 2-3 démos en visio/sem aux profils Marc qualifiés
- **Objectif M12 :** 3-5 clients DIY-S payants

### KPI 12 mois (objectif réaliste)

```
DFY  :  10-15 clients × ~1 200€ moyen   = 12-18 k€
DIY-S:   3-5 clients × ~2 500€ moyen   =  8-13 k€
DIY-A:   2-3 clients × ~15 000€ moyen   = 30-45 k€

Maintenance/support :                     2-5 k€
TOTAL CA an 1                          : 52-81 k€
```

→ Ordre de grandeur **50-80 k€** sur la première année — réaliste pour un solo bootstrappé
   avec activité Uccello Hub en parallèle.

→ Année 2 (cabinets DIY-A référencés + bouche-à-oreille pro) : projection **120-220 k€**
   réaliste si les conditions de séquencement sont respectées.

---

## Prochaines étapes recommandées

1. **Immédiat (sem 1-2) :** Préparer la landing page de gamme + les 3 pages produit (peut être
   généré via `/offer-study-website` ou `/offer-pitch-deck`).
2. **Sem 1-2 :** Identifier 2 freelances réseau pour missions pilotes DFY 490€.
3. **Sem 3-4 :** Lancer le contenu LinkedIn DFY (3 posts/sem).
4. **Sem 5-8 :** Identifier 5-10 cabinets cibles pour discovery calls Pipeline Studio (réseau pro).
5. **Mois 3 :** Évaluer DFY → si 3+ témoignages obtenus, ouvrir Pipeline Studio prospection.
6. **Optionnel — supports** :
   - `/offer-pitch-deck` : produire 1 deck Pipeline Studio (vente CODIR cabinet)
   - `/offer-prospection-strategy` : templates LinkedIn/email par persona
   - `/offer-discovery-call` : plan de call adapté par persona (Julien / Marc / Hélène)
   - `/offer-study-website` : régénérer le site avec la gamme 3 portes (le site v1 ne couvre que DFY)

---

## ⚠️ Recommandation de boucle

Le **website v1** (déployé sur https://3bagtocq.offer.uccello.io) ne reflète que l'offre DFY.
Si tu veux exposer la gamme complète, il faut :
- Soit régénérer le site avec `/offer-study-website` v2 (nouvelle structure 3 portes)
- Soit conserver v1 comme site DFY et créer 2 sites secondaires (DIY-S, DIY-A) — moins recommandé

→ Je n'ai pas refait le website (hors scope demandé). À lancer manuellement si besoin.
