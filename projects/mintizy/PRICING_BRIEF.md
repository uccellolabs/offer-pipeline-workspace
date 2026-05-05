# PRICING_BRIEF.md : Mintizy / Portail revendeurs ERP

- Date : 2026-05-05 | Version : 1.0 | Type offre : **A (SaaS récurrent B2B2B revendeur)** | Agent : /offer-pricing
- Sources : grid OCI signé (preuve empirique), MARKET_RESEARCH, COMPETITIVE_BRIEF, calculs économie unitaire UCCELLO

---

## 1. Diagnostic du grid OCI existant

### Le grid OCI signé

| Tranche utilisateurs finaux | Prix UCCELLO HT/mois | Marge revendeur (+40%) | Prix client final HT/mois |
|----------------------------|----------------------|------------------------|---------------------------|
| 1 à 10 | 120€ | 48€ | 168€ |
| 11 à 50 | 180€ | 72€ | 252€ |
| 51 à 100 | 240€ | 96€ | 336€ |
| 100+ | 300€ | 120€ | 420€ |

### Ce qui fonctionne

- ✅ Grille palier "client final" : aligne le prix sur la valeur perçue (pas per-user technicien comme Praxedo qui devient cher dès 30 techniciens)
- ✅ Marge revendeur 40% : standard SaaS B2B, suffisant pour rémunérer la vente + le support N1
- ✅ Empiriquement validé : OCI a 4 facturés + 15 en pipeline

### Le problème caché : ROI revendeur sur la marge récurrente seule

Investissement initial revendeur (passerelle ERP → portail) : ~12 000€ (3 semaines × 1 dev senior à ~600€/jour + tests + intégration).

**ROI sur marge récurrente seule, pour UN client :**
| Tranche | Marge récurrente/mois | Mois pour amortir 12k€ | Années |
|---------|----------------------|-----------------------|--------|
| 1-10 | 48€ | 250 | 20,8 |
| 11-50 | 72€ | 167 | 13,9 |
| 51-100 | 96€ | 125 | 10,4 |
| 100+ | 120€ | 100 | 8,3 |

Conclusion : la marge récurrente sur **un seul client** ne suffit jamais à justifier l'investissement passerelle. Le revendeur doit raisonner par **cohort** (portefeuille de 5 à 15 clients) ou ajouter d'autres sources de revenu.

### Contexte OCI versus autres revendeurs

OCI rentabilise parce qu'il a 4 clients déjà signés + 15 pipeline. Sa cohort effective est de 19 clients potentiels année 1 → 19 × 72€ × 12 = 16 416€/an récurrent. Amortit 12k€ en 9 mois.

Mais un nouveau revendeur (Sage X3, Dynamics BC, Divalto) sans portefeuille SAV pré-existant signe au mieux 3 à 5 clients année 1. Soit 3 × 72€ × 12 = 2 592€/an récurrent. Amortit 12k€ en **4 ans 7 mois**. Trop long pour décider d'investir.

→ **Le grid OCI seul ne suffit pas pour engager un nouveau revendeur sans cohort initiale.** Il faut ajouter d'autres leviers de revenu pour le revendeur.

---

## 2. Calcul de la valeur économique pour le client final

> Cette valeur justifie le prix vu par le client final (Pascal Dubreuil et profils similaires).

### Valeur directe annuelle

| Levier | Calcul | Valeur annuelle |
|--------|--------|-----------------|
| 1 appel d'offres remporté grâce au portail | 1 contrat moyen 40 à 80k€/an, attribuable à 30% au critère "portail" | 12 000€ à 24 000€ |
| Réduction appels entrants (-40% sur 30 appels/jour à 5 min/appel) | 1h/jour récupérée Sandrine × 220j × 35€/h | 7 700€ |
| Évitement dev portail custom (alternative) | 30 à 80k€ amortis sur 5 ans | 6 000€ à 16 000€ |
| Conformité audit qualité gros clients (réponse récap annuel automatisée vs 2j/an manuels) | 16h × 35€/h | 560€ |
| **Valeur totale annuelle estimée** | | **26 000€ à 48 000€** |

### Valeur indirecte

- Sécurisation contrats existants face à concurrents équipés
- Image de marque, légitimité réponse à AO
- Capacité à pricer plus haut grâce à la transparence (effet "premium service")
- Argument transmission de boîte (cabinet plus structuré, valorisation plus élevée)

### Prix value-based recommandé pour le client final

10 à 20% de la valeur annuelle = 2 600€ à 9 600€ HT/an = 217€ à 800€ HT/mois.

**Le grid OCI (168€ à 420€ vu client final) est dans la fourchette basse de la valeur, parfaitement aligné avec un positionnement "ROI rapide, accessible, démontrable"**. C'est un signal de discount stratégique délibéré : Mintizy capture moins de valeur unitaire en échange d'une adoption plus large.

---

## 3. Architecture tarifaire recommandée

### A. Grille publique récurrente (identique grid OCI, étendue)

| | Starter | **Business** ⭐ | Scale | Enterprise |
|--|---------|---------------|-------|-----------|
| **Utilisateurs finaux** | 1 à 10 | 11 à 50 | 51 à 100 | 100+ (palier dégressif) |
| **Prix UCCELLO HT/mois** | 120€ | 180€ | 240€ | 300€ jusqu'à 200, puis +1€ par user supplémentaire au-delà |
| **Prix revendeur public suggéré HT/mois** | 168€ | 252€ | 336€ | 420€ + (selon palier) |
| **Marge revendeur** | 48€ (40%) | 72€ (40%) | 96€ (40%) | 120€+ (40%) |
| **Pour qui** | TPE 5-15 techniciens, 1 client final structuré | PME 15-50 techniciens, 5 à 30 clients finaux | PME 50-100 techniciens, 30+ clients finaux | ETI / chaînes / multi-sites |
| **Inclus** | Portail standard, mobile, QR codes, hébergement FR, RGPD, support N2 UCCELLO | + IA conversationnelle WhatsApp, dashboard avancé | + sync ERP via Yousign + Stripe pré-paramétrée, multi-marques | + SLA 4h ouvrées, account manager dédié |
| **Argument clé** | Porte d'entrée appels d'offres, ROI 1 contrat suffit | **Cible majoritaire**, équilibre prix/fonctions, levier différenciation marketing | PME structurées avec multi-clients critiques | Comptes nationaux, groupements |

**Ouverture année 2** : ajouter un palier 200-500 et 500+ avec dégressif au user, pour adresser les ETI sortant naturellement du palier 100+.

### B. Setup fee client final (recommandation forte)

**990€ HT one-shot** par client final, facturé par le revendeur au client final, conservé à 100% par le revendeur.

Justification :
- Couvre le travail réel du revendeur (paramétrage compte, formation 2h commerciaux + admin, accompagnement go-live)
- Apporte une marge ponctuelle qui accélère le ROI revendeur de ~12 à 18 mois sur la passerelle
- Standard du marché SaaS B2B intégré (range 500-3000€)
- N'est PAS partagé avec UCCELLO : c'est la rémunération du revendeur pour son service de déploiement local

**Impact sur le ROI revendeur** :
- Cohort 5 clients/an : 5 × 990€ = 4 950€ one-shot année 1, 4 950€ année 2…
- Combiné à la marge récurrente : amortit la passerelle en ~14 mois (vs ~4 ans 7 mois sans setup fee)

### C. Option Quick-Start Passerelle UCCELLO

**14 900€ HT one-shot**, livré par UCCELLO au revendeur sur les ERP cibles (Sage X3, Cegid XRP Flex, Dynamics 365 BC, Divalto, Akuiteo).

Justification :
- Coût UCCELLO de production : ~10-12k€ (3 semaines × 1 dev senior + tests + doc)
- Marge UCCELLO : 25 à 30% (≈ 3 à 5k€) qui finance le maintien et la documentation
- Ouvre le marché aux 50-100 cabinets sans dev senior dispo (passe l'univers cible de ~50-100 à ~150-200 cibles, cf. MARKET_RESEARCH)
- Conditions : engagement revendeur minimum 5 clients signés sur 18 mois OU exclusivité territoriale concédée par UCCELLO

**Variante "open source connecteur"** : UCCELLO peut publier les connecteurs Quick-Start sur GitHub après 12 mois pour devenir un standard de marché. Stratégie communautaire à arbitrer en /offer-final.

### D. Option White-label

Deux modèles au choix du revendeur :

**Modèle 1 : surcoût récurrent**
- +50€ HT/mois par client final déployé en marque blanche
- Facturé par UCCELLO au revendeur, qui le répercute (ou pas) au client final

**Modèle 2 : setup global revendeur**
- 4 900€ HT one-shot, débloque le white-label illimité sur tous les clients du revendeur
- Adapté aux revendeurs qui font du volume

Justification :
- Le white-label représente un effort UCCELLO réel (configuration domaine, branding, emails, sous-marques techniques)
- Préserve la valorisation marque Mintizy (qui reste le default, le white-label est l'exception payante)
- Standard du marché (modèle blanc-de-marque facturé)

### E. Engagement contractuel

| Acteur | Engagement |
|--------|------------|
| Client final | Minimum 12 mois (alignement ERP), renouvellement tacite, préavis 3 mois |
| Revendeur partenaire | Pas d'engagement de volume nominal MAIS minimum 3 clients signés sur 18 mois pour conserver l'exclusivité territoriale (négociable) |
| UCCELLO | Engagement de support N2 et de roadmap produit, clause anti-concurrence sur les clients actifs du revendeur |

**Pas d'engagement 24 mois en standard** (génère friction commerciale) sauf en échange d'une remise volume négociée (-10% prix UCCELLO).

---

## 4. Économie unitaire revendeur (LTV / CAC)

### Hypothèses de référence (palier majoritaire 11-50 utilisateurs)

| Variable | Valeur |
|----------|--------|
| Prix UCCELLO mensuel | 180€ HT |
| Prix revendeur mensuel | 252€ HT |
| Marge revendeur récurrente | 72€/mois |
| Setup fee one-shot (perçu par revendeur) | 990€ |
| Durée moyenne client final estimée | 36 mois (alignement ERP) |
| Coût d'acquisition revendeur (CAC) par client final | 1 jour commercial + 1 jour avant-vente = ~600€ |

### Calcul LTV par client final

```
LTV = Setup fee + (Marge récurrente × Durée)
LTV = 990 + (72 × 36)
LTV = 990 + 2 592
LTV = 3 582 €
```

### Calcul CAC

```
CAC ≈ 600 €
```

### Ratio LTV/CAC

```
LTV/CAC = 3 582 / 600 = 5,97x
```

**Standard SaaS B2B sain : LTV/CAC ≥ 3x.** Avec 5,97x, le modèle est rentable pour le revendeur sous condition d'avoir au moins 3-5 clients sur 18 mois pour amortir la passerelle.

### Calcul ROI passerelle (cohort 5 clients/an, palier moyen 11-50)

```
Investissement passerelle             :  12 000 € (ou 14 900 € si Quick-Start UCCELLO)
Revenu setup fees année 1             : 5 × 990 € =  4 950 €
Revenu marge récurrente année 1       : 5 × 72 € × 12 = 4 320 €
Total revenu année 1                  :  9 270 €
ROI passerelle année 1                : 77 % (12 000 € investis, 9 270 € récupérés)
Mois pour ROI complet                 : ~14 mois
ROI 3 ans (cohort 15 clients cumulés) : 30 510 € de marge nette après amortissement
```

**Sans setup fee, le ROI passerelle s'effondre à ~4 ans 7 mois pour une cohort équivalente.** Le setup fee n'est pas optionnel, c'est la condition de viabilité du modèle pour les revendeurs hors OCI.

---

## 5. Comparaison concurrentielle (cas type : PME SAV 35 techniciens / 50 clients finaux)

| Solution | Prix mensuel total HT | Composition |
|----------|----------------------|-------------|
| **Mintizy seul (palier 11-50)** | **252€ HT/mois** | Portail B2B2C dédié client final |
| Praxedo Classic | 1 715€ HT/mois | 35 × 49€/user FSM (inclut Portail donneur d'ordres mais orienté B2B sous-traitance) |
| Mintizy + Praxedo Classic (bundle OCI type) | 1 967€ HT/mois | FSM complet + portail B2B2C |
| Dynamics 365 Field Service | 3 325€ HT/mois | 35 × 95€/user FSM Microsoft (inclut portail, exige BC ou licence Customer Engagement) |
| Sage X3 SAV + Weblinks (custom intégrateur) | 250 à 400€ HT/mois | Portail B2B custom |
| Synchroteam Customer Portal | ~770€ HT/mois | 35 × 22€/user multi-secteurs |
| Excel + emails + dev custom 1 fois | 0 à 35 000€/an dev one-shot | Inertie ou rachat sur-mesure |

**Argument value-based revendeur** : *"À 252€ HT/mois pour un portail spécialisé exposition client final, Mintizy est 6x moins cher que Praxedo Classic en pricing isolé. Si vous avez déjà Praxedo, vous l'utilisez pour ce qu'il fait le mieux (terrain technicien). Si vous n'avez pas Praxedo, Mintizy seul couvre votre besoin "portail client final" à un prix accessible. Dans les deux cas, vous différenciez vos réponses à appels d'offres avec un investissement minimal."*

---

## 6. Justifications prêtes

### Argumentaire ROI (à destination de Pascal, le client final)

> *"Pour un frigoriste de 35 techniciens, Mintizy coûte 252€/mois HT, soit 3 024€/an. Un seul appel d'offres GMS remporté grâce au portail (typiquement 40 à 80k€/an de contrat) représente 13 à 26 ans de portail amortis. La réduction des appels entrants en interne (-40% sur 30 appels/jour) libère 1h/jour à votre responsable administrative, soit 7 700€/an de productivité. ROI cumulé : 4 à 10x dès la première année."*

### Argumentaire revendeur (à destination de Stéphane, l'acheteur intégrateur)

> *"Pour un cabinet de 35 personnes signant 5 clients SAV par an, Mintizy génère 4 320€/an de marge récurrente + 4 950€/an de setup fees, soit 9 270€/an dès l'année 1. La passerelle ERP s'amortit en 14 mois. Sur 3 ans, marge nette cumulée : 30 510€ par cohort de 5 clients/an. À 100% sans charge d'exploitation supplémentaire, c'est l'équivalent de 0,5 ETP en marge pure. Et vous différenciez votre bundle dans tous vos pitches commerciaux SAV."*

### Argumentaire concurrentiel

> *"Praxedo équipe vos techniciens et la collaboration B2B sous-traitance. Mintizy expose la vitrine commerciale au client final. Selon votre contexte, c'est un complément (modèle OCI) ou une alternative (cabinets sans Praxedo). Dans les deux cas, à 252€/mois HT pour 35 techniciens vs 1 715€ pour Praxedo Classic, le pricing palier client final donne un avantage économique inégalable sur le sous-périmètre portail."*

---

## 7. Réponses aux objections prix

| Objection | Réponse |
|-----------|---------|
| "Trop cher, mes clients ne paieront pas 252€/mois" | "Comparez à un dev custom (30 à 80k€), à Praxedo Classic (1 715€/mois) ou à un appel d'offres perdu (40 à 80k€/an de contrat). Le portail est l'option la moins chère. Sans engagement, 1 mois gratuit, ROI mesurable en 3 mois." |
| "Praxedo est moins cher si on regarde uniquement leur abonnement de base" | "Praxedo Start à 24,5€/user × 35 = 858€/mois pour des fonctions FSM minimales sans portail B2B donneur d'ordres. Mintizy à 252€/mois est dédié au portail B2B2C exposition client final. Comparez ce qui est comparable : Mintizy seul vs Praxedo Classic + Portail." |
| "Le client final peut le faire en interne avec Excel" | "Oui, c'est ce que 80% du marché fait. Et c'est ce qui leur fait perdre les appels d'offres réglementés. Combien d'AO Carrefour, Auchan, McDonald's avez-vous perdus sur le critère "absence de portail" ces 24 mois ?" |
| "Je n'ai pas de budget revendeur pour la passerelle" | "Option Quick-Start Passerelle UCCELLO : 14 900€ HT one-shot, livré clé-en-main. Amortit en 16-18 mois sur cohort de 5 clients/an. Zéro charge dev pour vous." |
| "Pourquoi je signerais sans exclusivité ?" | "Vous obtenez l'exclusivité territoriale (région ou département) ou sectorielle dès 3 clients signés sur 18 mois. Cela vous protège commercialement vis-à-vis de vos confrères." |
| "Et si vous augmentez les prix dans 2 ans ?" | "Clause de prix gelé sur 24 mois post-signature dans le contrat de distribution. Au-delà, indexation maximum sur l'inflation INSEE." |
| "Pourquoi pas un modèle commission pure plutôt que marge revendeur ?" | "La marge revendeur 40% rémunère le travail de vente + support N1 + formation. C'est plus engageant qu'une simple commission, ce qui aligne nos intérêts sur la satisfaction client à long terme." |

---

## 8. Pricing revendeur (synthèse contractuelle)

| Type partenaire | Niveau d'engagement | Remise / marge | Justification |
|----------------|---------------------|----------------|---------------|
| **Revendeur actif certifié** | 3+ clients signés sur 18 mois | **40% marge** sur tarif UCCELLO | Vente + support N1 + formation |
| **Revendeur en montée en charge** | 1 à 2 clients signés | 30% marge premiers 6 mois, 40% ensuite | Période de découverte |
| **Apporteur d'affaires** | Lead seulement, pas de support | 15% commission unique versée 6 mois après signature client | Lead uniquement |
| **Prescripteur (consultant, cabinet conseil)** | Recommandation passive | 5% commission unique | Recommandation simple |

---

## 9. Décisions critiques pour /offer-final

1. **La grille OCI devient la grille publique Mintizy** pour tous les futurs revendeurs (cohérence + équité). Pas de négociation case-by-case sur le prix UCCELLO. Négociation possible uniquement sur exclusivités et engagements de volume.
2. **Setup fee 990€ HT par client final est OBLIGATOIRE** dans la grille recommandée pour rendre le ROI revendeur soutenable hors OCI.
3. **Option Quick-Start Passerelle 14 900€ HT** est CRITIQUE pour ouvrir l'univers cible de 50-100 à 150-200 cabinets adressables.
4. **White-label = option premium payante**, pas le mode par défaut. Préserve la marque Mintizy.
5. **Engagement client final 12 mois minimum**, alignement standard SaaS B2B intégré.

---

## 10. Questions pour /offer-final

1. La grille publique Mintizy doit-elle être visible publiquement (site web) ou rester en partenariat NDA (négociation revendeur par revendeur sur l'exclusivité) ?
2. Le Quick-Start Passerelle est-il à inclure dans l'offre standard dès l'année 1, ou à mettre en réserve pour année 2 (commencer par les revendeurs avec dev senior dispo) ?
3. La marque Mintizy doit-elle rester par défaut ou laisser le choix au revendeur dès la signature (white-label gratuit pour les premiers 5 partenaires comme incitation) ?
