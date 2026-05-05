# OFFER_FINAL.md : Mintizy / Portail revendeurs ERP

- Date : 2026-05-05 | Version : 1.0 | Agent : /offer-final
- Destinataire principal : **Acheteur revendeur** (intégrateur ERP français avec practice SAV)
- Destinataire secondaire : utilisateur final (PME maintenance technique cliente du revendeur), via le revendeur
- Format : document source unique, alimente pitch deck, site web étude, kit commercial revendeur, scripts de prospection
- Statut : **PRÊT À UTILISER**

---

## Synthèse pipeline (extrait PIPELINE_SUMMARY)

```
Idée        : Portail client Mintizy revendu en marque Mintizy (white-label optionnel) à des intégrateurs ERP français orientés SAV/maintenance
Cible       : 🥇 Intégrateurs ERP français 10-80 personnes avec practice SAV (Cegid XRP Flex, Sage X3 prioritaires)
Problème    : Les intégrateurs ERP perdent des deals SAV faute de brique "portail client" prête-à-bundler ; les PME maintenance perdent des appels d'offres faute de portail client professionnel
Valeur      : Pour le revendeur, +30 à 40% de marge sur une brique différenciante sans R&D ; pour le client SAV, portail clé-en-main à 252€/mois HT vs 30-80k€ de dev custom
Canal       : Distribution indirecte (revendeurs intégrateurs ERP)
Concurrent  : Praxedo (FSM dominant, complément ou alternative selon cas) ; Microsoft D365 FS, Sage X3 SAV, Synchroteam
Prix cible  : Grille palier 120/180/240/300€ HT UCCELLO + 40% marge revendeur + setup fee 990€ + options Quick-Start passerelle / white-label
Verdict     : GO ferme, **VIABLE SOUS CONDITIONS** (cf. score ci-dessous)
```

---

## Score de viabilité globale

```
Critère 1 : Douleur intense et prioritaire
  Score douleur     : 7/10
  Déjà dépensé      : OUI (4 clients facturés via OCI + 15 pipeline, willingness to invest prouvée des 2 côtés)
  Signal            : ✅ PRIORITAIRE

Critère 2 : Cible concrètement prospectable
  Score amont       : 7/10 (Stéphane Maréchal, intégrateur ERP)
  Canaux identifiés : LinkedIn Sales Navigator nominatif, événements partenaires éditeurs (Cegid Connections, Sage Sessions, Microsoft Inspire), recommandation OCI, communautés Cegid Partners / Sage Partners FR
  Univers cible     : 50-100 cabinets prioritaires (filtre SAV + capacité dev), extensible à 150-200 avec Quick-Start Passerelle
  Signal            : ✅ PROSPECTABLE

Critère 3 : Marché avec budget + prêt à investir
  Budget dédié      : ✅ OUI (enveloppes R&D bundle existantes, programmes partenaires éditeurs structurés)
  Maturité marché   : ✅ ÉDUQUÉ (Praxedo, Twimm, Synchroteam établis 10+ ans, vocabulaire FSM connu)
  Cycle closing     : 3 à 9 mois (médiane 5 mois) pour un partenariat de distribution
  Signal            : ✅ MARCHÉ PRÊT

VERDICT GLOBAL    : ⚠️ VIABLE SOUS CONDITIONS
```

### Conditions critiques pour passer à VIABLE FERME

1. **Setup fee 990€ HT par client final intégré dès le 1er contrat hors OCI**. Sans lui, ROI passerelle 4 ans 7 mois pour un nouveau revendeur, modèle non soutenable. Avec : 14 mois.
2. **Quick-Start Passerelle UCCELLO opérationnel sur Sage X3 d'ici M+6** (1 connecteur livré, documenté, testé) pour ouvrir le marché aux 50-100 cabinets sans dev senior.
3. **Sourcing structuré dès M+1** : LinkedIn Sales Navigator + script outbound + 1 événement partenaire éditeur à viser en année 1 (Cegid Connections ou Sage Sessions).
4. **Au moins 1 deuxième revendeur signé sous 6 mois** pour dérisquer la dépendance OCI. Sinon, retour en /offer-cadrage pour reconsidérer la stratégie canal.

---

## ⚠️ Points de vigilance exécution

| Vigilance | Impact | Action recommandée |
|-----------|--------|--------------------|
| Temps vente 1,5 j/sem (Jonathan + Jonadabe) | Cycle de 5 mois × 5-7 deals = ~25-35 mois cumulés | Concentrer 80% du temps sur Cegid + Sage X3 (focus). Externaliser le sourcing administratif (assistant LinkedIn, Sales Navigator workflow) |
| Bootstrapped (pas de marketing payant) | Dépendance totale outbound | Activer 3 leviers gratuits : (1) cas client OCI publié, (2) présence événements partenaires éditeurs, (3) communautés LinkedIn sectorielles |
| Pas de réseau pré-existant intégrateurs ERP | Ramp-up sourcing 3-6 mois avant 1er deal | Démarrer immédiatement le mapping nominatif des 50-100 cibles + envoi 5-10 messages personnalisés/semaine |
| Quick-Start Passerelle pas encore développé | Filtre cible serré (50-100 vs 150-200) | Prioriser la passerelle Sage X3 en année 1 (ROI maximal vu volume du réseau Sage) |
| Confusion concurrentielle Praxedo | Risque de cycle allongé par incompréhension du positionnement | Cristalliser la frontière "B2B sous-traitance vs B2B2C exposition client final" dans tous les supports dès J+0 |

---

## L'OFFRE

### 1. TITRE

> **Mintizy. Le portail client B2B2C que vous bundlez à votre ERP pour gagner les deals SAV : prêt en 4 semaines, à votre marque, à 252€ HT/mois, +40% de marge récurrente.**

### 2. PROBLÈME (langage du persona Stéphane)

Vos clients SAV perdent des appels d'offres face à des concurrents équipés d'un portail client professionnel. Vous, vous perdez des deals d'intégration parce que votre bundle s'arrête à l'ERP, sans la brique "exposition au client final" que vos prospects réclament. Quand un cuisiniste pro veut répondre à Carrefour, à McDonald's, à un appel d'offres GMS, il a besoin d'un portail à sa marque, intégré à son ERP, accessible à ses propres clients : ni Excel, ni un dev custom à 50k€, ni un FSM générique. Cette brique manque dans votre catalogue, et chaque deal que vous perdez sur ce critère est un manque-à-gagner récurrent et irrattrapable.

### 3. POURQUOI LES SOLUTIONS ACTUELLES NE SUFFISENT PAS

- **Le module SAV de votre ERP** (Sage X3 SAV, Cegid XRP Flex Service, Divalto Service) est conçu pour le back-office ERP : fonctionnel mais UX datée, pas mobile-first, pas de QR codes équipements, peu adapté à l'exposition à un client final non technique.
- **Praxedo et autres FSM** équipent vos techniciens et adressent la collaboration B2B donneur d'ordres ↔ prestataire. Leur portail est orienté sous-traitance, pas exposition vitrine commerciale. Le pricing per-user technicien (49€/user × 35 = 1 715€/mois) devient prohibitif pour le sous-besoin "portail client final".
- **Le dev custom maison** (sur-mesure ou via un confrère intégrateur) coûte 30 à 80k€, prend 6 à 12 mois, et vous laisse seul à porter la dette technique et le support N1+N2.
- **Microsoft Dynamics 365 Field Service Portal** est puissant mais réservé à l'écosystème Dynamics 365 FS payant (95-150€/user/mois), inaccessible à 95% des PME maintenance.

### 4. SOLUTION

**Ce que c'est** : Mintizy est un portail client B2B2C en marque blanche ou en marque Mintizy, intégrable à n'importe quel ERP via API ouverte, déployable en 4 semaines une fois la passerelle ERP construite (par votre dev senior ou livrée clé-en-main par UCCELLO), revendu à vos clients SAV à 252€ HT/mois pour le palier majoritaire 11-50 utilisateurs finaux.

**Ce que ça fait** :
- ✅ **Expose en temps réel les interventions** à vos clients finaux (calendrier, dashboard, historique sur 3 ans, rapports CERFA téléchargeables)
- ✅ **Couvre les exigences réglementaires** (CERFA, F-Gas, audit qualité, traçabilité)
- ✅ **Transforme les réponses à appel d'offres** par un argument visuel net (démonstration en RDV commercial)
- ✅ **Réduit les appels entrants -40%** côté votre client SAV (charge mentale interne récupérée, productivité +1h/jour pour son admin)
- ✅ **S'adapte à la marque du revendeur ou du client final** (white-label optionnel, branding personnalisable)

**Ce que ça change pour votre cabinet (avant/après)** :

| Avant | Après |
|-------|-------|
| Vous chiffrez un dev custom à 50k€ qui ne se signe pas | Vous présentez Mintizy à 252€/mois en RDV commercial, le client signe en 1-3 mois |
| Vos commerciaux n'ont pas d'argument différenciant SAV face aux concurrents équipés Praxedo | Vous bundlez Mintizy en complément ou en alternative selon le contexte, ROI démontrable en 1 contrat AO remporté |
| Votre cabinet stagne en marge récurrente, valorisation faible | +30 à 40% marge récurrente sur une brique sans R&D, ARR cumulé 8-15k€/an par cohort de 5 clients/an |

### 5. POUR QUI

**✅ Vous êtes le bon profil si :**
- Vous êtes un cabinet d'intégration ERP français de 10 à 80 collaborateurs
- Vous avez une practice SAV/maintenance active OU vous voulez la lancer
- Vous opérez sur Cegid XRP Flex, Sage X3, Microsoft Dynamics 365 BC, Divalto, Akuiteo, SAP B1 ou Odoo Enterprise
- Vous avez au moins 1 dev senior interne disponible 3 semaines pour la passerelle, OU vous êtes prêt à investir 14 900€ dans le Quick-Start Passerelle UCCELLO
- Vous voulez augmenter votre part d'ARR récurrent sans alourdir votre roadmap produit
- Vous êtes basé en France, vos clients sont en France, RGPD et hébergement France sont des arguments commerciaux pour vous

**❌ Vous n'êtes pas le bon profil si :**
- Vous êtes un cabinet < 10 personnes sans dev senior dédié
- Votre cœur de métier est strictement la comptabilité (Sage 100, Cegid Quadra) sans practice SAV
- Vous opérez exclusivement sur Dynamics 365 Field Service (vous avez déjà mieux intégré nativement)
- Vous voulez un partenariat sans engagement minimum (3 clients/18 mois requis pour exclusivité territoriale)

### 6. DIFFÉRENCIATION (3 arguments non-comparables)

1. **Le seul portail B2B2C dédié à l'exposition client final, intégrable à tout ERP via API ouverte.** Praxedo Portail donneur d'ordres = collaboration B2B sous-traitance. Microsoft D365 FS Portal = couplé Microsoft. Sage X3 SAV = UX ERP-back-office. Mintizy = vitrine commerciale UX-first dédiée client final, indépendante de l'ERP cible.

2. **Pricing palier client final, pas per-user technicien.** Pour 35 techniciens, Mintizy = 252€ HT/mois (palier 11-50 users finaux). Praxedo Classic = 1 715€/mois. Microsoft D365 FS = 3 325€/mois. Ratio x6 à x13 favorable à Mintizy sur le sous-périmètre portail. Pour vos clients aux budgets serrés, c'est un argument décisif.

3. **+40% marge revendeur récurrente + setup fee 990€ conservé à 100% par vous.** Sur cohort 5 clients/an palier moyen : 4 320€/an récurrent + 4 950€/an setup = 9 270€/an dès la 1ère année. Passerelle ERP amortie en 14 mois. Sur 3 ans, 30 510€ de marge nette par cohort. À 100% sans charge d'exploitation supplémentaire.

### 7. OFFRE ET PRIX

#### Grille publique récurrente (par client final servi)

| | Starter | **Business** ⭐ | Scale | Enterprise |
|--|---------|---------------|-------|-----------|
| **Utilisateurs finaux** | 1 à 10 | 11 à 50 | 51 à 100 | 100+ |
| **Prix UCCELLO** | 120€ HT/mois | 180€ HT/mois | 240€ HT/mois | 300€+ HT/mois |
| **Prix client final (suggéré)** | 168€ | 252€ | 336€ | 420€+ |
| **Marge revendeur** | 48€ (40%) | 72€ (40%) | 96€ (40%) | 120€+ (40%) |
| **Inclus** | Portail standard, mobile, QR codes, RGPD, support N2 | + IA conversationnelle WhatsApp, dashboard avancé | + sync ERP Yousign + Stripe pré-paramétrée, multi-marques | + SLA 4h ouvrées, account manager dédié |

#### Frais et options

| Option | Prix | Bénéficiaire |
|--------|------|--------------|
| **Setup fee client final** | 990€ HT one-shot | Conservé à 100% par le revendeur (couvre paramétrage, formation, accompagnement go-live) |
| **Quick-Start Passerelle UCCELLO** (Cegid XRP Flex, Sage X3, Dynamics 365 BC, Divalto, Akuiteo) | 14 900€ HT one-shot | UCCELLO livre la passerelle clé-en-main au revendeur ; alternative au dev interne 3 semaines |
| **White-label premium** | +50€/mois HT/client OU 4 900€ HT one-shot global | UCCELLO maintient configuration custom marque revendeur |

#### Engagement

- **Client final** : 12 mois minimum, renouvellement tacite, préavis 3 mois
- **Revendeur** : pas d'engagement de volume, mais minimum 3 clients signés sur 18 mois pour conserver l'exclusivité territoriale (région ou département) ou sectorielle
- **UCCELLO** : engagement support N2, roadmap produit, clause anti-concurrence sur les clients actifs du revendeur, prix gelé 24 mois post-signature contrat

### 8. PREUVE

- **Groupe OCI**, intégrateur Cegid XRP Flex basé à Bourgoin-Jallieu : 1er revendeur signé sous contrat de distribution Mintizy. **4 clients facturés + 15 en pipeline qualifié** au 5 mai 2026. ARR initial estimé 60 à 100k€ à fin 2026 sur OCI seul.
- **Mintizy en marché depuis 2022**, 1 200+ utilisateurs revendiqués, hébergement France, conformité RGPD, certifications sécurité (chiffrement en transit et au repos, sauvegardes quotidiennes).
- **Cas clients existants Mintizy direct** : cuisinistes professionnels (Toulouse), parcs fitness (cas client documenté sur mintizy.com), exploitables en témoignages publiables.
- **Levier groupements professionnels** : OCI a signé Groupe Gasel (groupement multi-membres) → 1 deal commercial peut activer 5-20 sociétés. Multiplicateur réel sur l'ARR.
- **Marque Mintizy** : éditeur UCCELLO LABS, siège Montpellier, équipe stable, 4 ans d'existence, pas de levée de fonds (bootstrapped, indépendance financière garantie).

> **Rappel** : aucun chiffre n'est inventé. Tous les éléments ci-dessus sont sourcés depuis PROJECT_CONTEXT et le contrat OCI.

### 9. OBJECTIONS ANTICIPÉES

| Objection | Réponse courte |
|-----------|----------------|
| *"Je n'ai pas le bandwidth dev pour la passerelle"* | OCI a fait la sienne en 17 jours-homme. Sinon, Quick-Start Passerelle UCCELLO 14 900€ HT clé-en-main, livré en 2-3 semaines. |
| *"Et si vous décidez de go-direct sur ma base ?"* | Clause anti-prospection contractuelle + exclusivité territoriale dès 3 clients signés. Notre canal commercial n'a pas de force de vente directe sur le segment grand compte SAV. Modèle économique aligné sur le succès des partenaires. |
| *"Praxedo / Microsoft / Sage est plus connu, plus rassurant"* | Vrai, et c'est précisément l'opportunité. La notoriété joue contre vous quand vous voulez vous différencier. Mintizy adresse une niche fonctionnelle (portail B2B2C exposition client final) avec un pricing imbattable, là où les leaders restent généralistes ou cher. OCI a choisi Mintizy en parfaite connaissance de cause. |
| *"Pricing trop bas pour me valoir le coup en marge"* | 40% marge récurrente + 990€ setup fee one-shot conservé. Cohort 5 clients/an palier moyen = 9 270€ année 1, 13 590€ année 2, 17 910€ cumulés sur 3 ans. ROI passerelle 14 mois. À 100% sans charge d'exploitation. |
| *"Mes clients ne paieront pas un abonnement supplémentaire"* | Comparez à un dev custom (30-80k€), à Praxedo Classic (1 715€/mois), à un appel d'offres perdu (40-80k€/an). Le portail à 252€/mois est l'option la moins chère et la plus rapide. Sans engagement, 1 mois gratuit. |

### 10. APPEL À L'ACTION

> **Réservez un call de qualification de 30 minutes avec Jonathan Sardo (UCCELLO LABS).**
> Vous repartez avec : (1) la grille tarifaire détaillée + business case sur votre périmètre client, (2) une démo du portail Mintizy en marque blanche sur votre vertical prioritaire, (3) un chiffrage spécifique de votre passerelle ERP cible, (4) le contrat de distribution type pour étude juridique.
>
> **Réservation : [lien Calendly] · jonathan@uccellolabs.com · LinkedIn /in/jonathansardo**

---

## Plan de mise en marché 12 mois (M+1 à M+12)

### Trimestre 1 (M+1 à M+3) : Activation

- **M+1** : Mapping nominatif des 50-100 cabinets cibles prioritaires (Cegid XRP Flex + Sage X3) via LinkedIn Sales Navigator. Production du kit commercial revendeur (deck, ROI calculator, scripts d'objection, témoignage OCI). Rédaction d'un cas client OCI publiable.
- **M+2** : Démarrage outbound (5-10 messages personnalisés/semaine), demande de témoignage public OCI, présence digitale (1 article LinkedIn par semaine sur la frontière FSM/portail B2B2C).
- **M+3** : Premiers calls de qualification (objectif 8-12 calls). 1ère démo en RDV commercial sur 2-3 cabinets qualifiés.

### Trimestre 2 (M+4 à M+6) : Premiers signaux

- **M+4** : Présence à 1 événement partenaire éditeur (Cegid Connections OU Sage Sessions). Objectif : 5 RDV pré-bookés sur place.
- **M+5** : Lancement développement Quick-Start Passerelle Sage X3 (3 semaines de dev senior UCCELLO). Premier contrat de distribution signé (objectif : 1 nouveau revendeur Cegid XRP Flex hors OCI).
- **M+6** : Quick-Start Passerelle Sage X3 livré et testé. Ouverture officielle du canal Sage X3.

### Trimestre 3 (M+7 à M+9) : Montée en charge

- **M+7** : Premier client final signé sur le nouveau revendeur Cegid hors OCI (~3 mois après signature contrat distribution).
- **M+8** : Deuxième contrat de distribution signé (objectif : 1 revendeur Sage X3).
- **M+9** : Première itération du kit commercial sur la base des retours terrain. Présence à 1 deuxième événement partenaire éditeur.

### Trimestre 4 (M+10 à M+12) : Consolidation

- **M+10** : Lancement développement Quick-Start Passerelle Dynamics 365 BC (à partir des retours pipeline année 1).
- **M+11** : Troisième et quatrième contrats de distribution signés. Total : 4-5 revendeurs actifs (incluant OCI).
- **M+12** : Bilan commercial. Cible atteinte : 5-7 revendeurs signés, 25-50 clients finaux actifs, 60-120k€ ARR additionnel cumulé. Passage en accélération année 2 (recrutement commercial dédié à arbitrer selon performance).

---

## Checklist FAISABILITÉ avec ressources actuelles

| Critère | Statut | Note |
|---------|--------|------|
| L'équipe actuelle peut-elle délivrer le produit ? | ✅ | Mintizy est en production, support N2 déjà en place |
| Le temps vente (1,5 j/sem) permet-il le cycle (5 mois médian × 5-7 deals) ? | ⚠️ | Tendu mais réaliste avec sourcing très ciblé. Recommandation : externaliser les tâches admin LinkedIn |
| Le budget couvre-t-il le CAC implicite ? | ✅ | Bootstrapped + outbound = CAC ~600€/lead, soutenable |
| Les compétences internes suffisent ? | ⚠️ | Vente B2B partenariat à structurer (kit commercial à produire, scripts à itérer). Compétence technique : OK |
| Les contraintes techniques sont-elles respectées ? | ✅ | API existante, hébergement FR, RGPD, support N2 opérationnel |
| Quick-Start Passerelle production sur Sage X3 dans les 6 mois ? | ⚠️ | Investissement R&D 2-3 semaines × 1 dev senior à arbitrer en COMEX UCCELLO |
| Au moins 1 deuxième revendeur signé sous 6 mois ? | ⚠️ | Conditionne le passage de VIABLE SOUS CONDITIONS à VIABLE FERME |

---

## Sources utilisées

- [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) v1.0 (2026-05-05)
- [OFFER_BRIEF.md](OFFER_BRIEF.md) v1.0 enrichi (2026-05-05)
- [PERSONA_ACHETEUR.md](PERSONA_ACHETEUR.md) v1.0 : Stéphane Maréchal
- [PERSONA_UTILISATEUR.md](PERSONA_UTILISATEUR.md) v1.0 : Pascal Dubreuil
- [MARKET_RESEARCH.md](MARKET_RESEARCH.md) v1.0 : SIRENE via API recherche-entreprises.api.gouv.fr
- [COMPETITIVE_BRIEF.md](COMPETITIVE_BRIEF.md) v1.0 : 5 battlecards
- [PRICING_BRIEF.md](PRICING_BRIEF.md) v1.0 : architecture hybride, LTV/CAC 5,97x
- Site web Mintizy mintizy.com (extraction charte visuelle, packs Mintizy direct, programme partenaires existant)
- Web : annuaires partenaires Cegid, Sage, Microsoft Dynamics, Divalto, Akuiteo, SAP B1 ; sites Praxedo, Synchroteam, Twimm

---

## Prochaines étapes

1. **/offer-study-website** : générer le site multi-pages présentant l'étude (en attente de lancement)
2. **Tester le titre et le pitch sur 3 prospects** (validation langage du persona Stéphane Maréchal en conditions réelles)
3. **Valider la grille tarifaire avec 2-3 prospects** (willingness to pay test sur le setup fee 990€ et le Quick-Start 14 900€)
4. **Produire le kit commercial revendeur** (deck commercial, ROI calculator, scripts d'objection, témoignage OCI publié) → /offer-pitch-deck non demandé en Phase 4 actuelle, mais à arbitrer pour année 1
5. **Démarrer le sourcing nominatif des 50-100 cabinets cibles** dès M+1 (LinkedIn Sales Navigator + outbound 5-10/sem)
