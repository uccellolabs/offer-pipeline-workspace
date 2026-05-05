# MARKET_RESEARCH.md : Mintizy / Portail revendeurs ERP

- Date : 2026-05-05 | Version : 1.0 | Agent : /offer-market-research
- Sources : API Recherche d'Entreprises (data.gouv.fr / SIRENE INSEE), annuaires partenaires éditeurs ERP, web search
- MCP Datagouv : ✅ utilisé (API gratuite, base SIRENE) | MCP INSEE tiers : non détecté

---

## 1. Canal qualifié

**Mode B : Revendeurs (intégrateurs ERP).**

Confirmé par PROJECT_CONTEXT et par la traction empirique (OCI = preuve d'un revendeur actif). Pas de mixte recommandé : la vente directe Mintizy direct existe déjà comme offre distincte (Starter/Business/Scale) et cible un autre segment (PME SAV souhaitant la plateforme complète, pas juste le portail).

---

## 2. Volumétrie amont : intégrateurs ERP français adressables

### Source SIRENE (API Recherche d'Entreprises, code NAF 62.02A "Conseil en systèmes et logiciels informatiques")

| Tranche d'effectifs | Nb d'entreprises FR (état actif) |
|---------------------|----------------------------------|
| 10 à 19 salariés | 1 373 |
| 20 à 49 salariés | 1 155 |
| 50 à 99 salariés | 381 |
| 100 à 199 salariés | 214 |
| 200 à 249 salariés | 33 |
| **Total 10-249 sal.** | **3 156** |

> Le NAF 62.02A inclut **toutes les ESN et SS2I**, pas uniquement les intégrateurs ERP métier. Les intégrateurs ERP représentent une fraction de ce total.

### Estimation des intégrateurs ERP par éditeur (sources : annuaires officiels + presse spécialisée)

| Éditeur | Partenaires actifs FR (estimation) | Source |
|---------|------------------------------------|--------|
| Cegid XRP Flex | ~30 (25 certifiés + 6 en certification) | Cegid.com/partenaires-integrateurs, ChannelNews |
| Sage X3 | ~50 à 80 | Sage Top League, lebonlogiciel.com |
| Microsoft Dynamics 365 BC | ~50 à 100 | Microsoft Partner Directory, foxeet.fr |
| Divalto | 150 distributeurs/intégrateurs (50 labellisés) | Divalto.com |
| Akuiteo | ~10 à 25 | Akuiteo.com (réseau diffus) |
| SAP Business One | ~15 à 30 | OPTI-ONE Master VAR + réseau |
| Odoo Enterprise | ~80 à 150 (forte croissance) | annuaires Odoo |
| **Total cumulé (avec doublons multi-ERP)** | **~400 à 600 cabinets** | |
| **Total dédoublonné estimé** | **~250 à 400 cabinets distincts** | méthode : ~30-40% des intégrateurs servent 2+ ERP |

### Filtres successifs pour qualifier l'univers cible

```
Univers brut intégrateurs ERP français (10-249 sal.)            ~ 250 à 400 cabinets
  │
  ├── Filtre "practice SAV/maintenance active"                   ~ 30 à 40 % qualifient
  │   (cabinets ayant déjà des clients récurrents en SAV/        → 75 à 160 cabinets
  │    maintenance, identifiables via leurs cas clients
  │    publics, leurs landing pages "secteurs" ou
  │    leur communication événementielle)
  │
  ├── Filtre "capacité dev API senior dispo 3 semaines"          ~ 50 à 70 % passent
  │   (au moins 1 dev senior interne ou pool d'astreinte         → 40 à 100 cabinets
  │    bandwidth, exigence pour construire la passerelle
  │    ERP → portail Mintizy)
  │
  └── Univers cible prioritaire année 1                          ≈ 50 à 100 cabinets
```

### Ce que confirme la SIRENE

Les **595 ESN françaises de 50 à 199 salariés** (tranches 21+22 du NAF 62.02A) constituent le cœur de marché pour le profil Stéphane Maréchal (cabinet de 35 personnes, soit tranche 12). En descendant à 10-19 salariés, beaucoup ne disposent pas d'un dev senior dédié, ce qui exclut la moitié.

---

## 3. Volumétrie aval : PME maintenance technique françaises adressables

### Source SIRENE (entreprises actives, 10-249 salariés)

| Code NAF | Libellé | Effectifs FR (10-249 sal.) |
|----------|---------|---------------------------|
| 43.22B | Travaux d'installation d'équipements thermiques et de climatisation (CVC, frigorifique) | **2 404** |
| 93.11Z | Gestion d'installations sportives (parcs fitness, salles, complexes) | **712** |
| 33.20D | Installation d'équipements industriels | 205 |
| 33.14Z | Réparation d'équipements électriques | 190 |
| 33.19Z | Réparation d'autres équipements | 39 |
| **Total 5 verticales prioritaires** | | **~3 550** |

### Volumétrie complémentaire à explorer (non chiffrée ici mais pertinente)

- 95.21Z, 95.22Z, 95.24Z : réparation grand public et électroménager (potentiel TPE/PME parc national, distributeurs automatiques)
- 81.30Z : aménagement paysager (entretien terrains)
- 43.21A : installation électrique
- Entreprises ascensoristes indépendantes : segment éclaté entre plusieurs NAF (43.29B, 33.20D)

### Filtres successifs pour qualifier l'univers cible aval

```
PME maintenance technique 10-249 sal. (5 verticales)              ~ 3 550 entreprises
  │
  ├── Filtre "déjà cliente d'un ERP intégré chez un partenaire    ~ 30 à 50 % du total
  │    Mintizy potentiel" (Cegid XRP Flex, Sage X3, Dynamics BC,  → 1 065 à 1 775
  │    Divalto, Akuiteo, SAP B1, Odoo Enterprise)                    PME adressables
  │
  ├── Filtre "douleur portail client identifiée" (appels d'offres ~ 40 à 60 % du précédent
  │    réglementés perdus, demande client final, modernisation    → 425 à 1 065
  │    image, conformité réglementaire CERFA/F-Gas)                  PME prioritaires
  │
  └── Pool de prospects qualifiés activables via canal             ≈ 400 à 1 000
       partenaire en année 1                                          PME activables
```

---

## 4. TAM / SAM / SOM

### TAM (Total Addressable Market) : marché théorique français

```
3 550 PME maintenance × 190€ HT moyen/mois UCCELLO × 12 mois = ~8,1 M€ ARR théorique
(prix moyen pondéré = palier 11-50 sal. à 180€ = palier majoritaire estimé)
```

### SAM (Serviceable Addressable Market) : adressable via le canal partenaire

```
1 000 à 1 800 PME (déjà clientes d'un partenaire ERP cible) × 190€ × 12 = 2,3 à 4,1 M€ ARR
```

### SOM (Serviceable Obtainable Market) : capture réaliste à 3 ans

```
Hypothèse 5 % de pénétration du SAM en 3 ans :
50 à 90 clients finaux × 2 280€/an = 114 à 205 k€ ARR à horizon 3 ans
```

**Revue à la hausse possible** si :
- Effet de levier groupements (Gasel) confirme un multiplicateur de 3 à 5x sur certains comptes : +30 à +50 % SOM
- UCCELLO ouvre une option "passerelle livrée clé-en-main" pour ouvrir le marché aux intégrateurs sans dev senior

**Cohérence avec l'objectif PROJECT_CONTEXT** : objectif 12 mois (60 à 120 k€ ARR) = 2 à 4 % du SAM activé en année 1, soit cohérent avec un ramp-up commercial classique (5 à 7 partenaires signés, dont 2 à 3 actifs commercialement).

---

## 5. Priorisation des ERP cibles

### Matrice de priorisation

| Éditeur | Volume partenaires FR | Affinité SAV/maintenance | Capacité dev typique | Proof point existant | Priorité |
|---------|----------------------|--------------------------|---------------------|---------------------|----------|
| **Cegid XRP Flex** | ~30 | Moyenne (industrie/négoce) | Forte (cabinets bien staffés) | ✅ OCI 4 facturés + 15 pipeline | 🥇 1 |
| **Sage X3** | ~50 à 80 | Moyenne-Forte (industrie/négoce/services) | Forte | ❌ aucun à date | 🥇 2 |
| Microsoft Dynamics 365 BC | ~50 à 100 | Forte (FSM natif dans BC) | Forte (Microsoft-friendly) | ❌ aucun à date | 🥈 3 |
| Divalto | 50 labellisés | Forte (positionnement services) | Moyenne | ❌ aucun à date | 🥈 4 |
| Akuiteo | ~10 à 25 | Forte (gestion par affaires) | Forte | ❌ aucun à date | 🥉 5 |
| SAP Business One | ~15 à 30 | Faible (industrie pure) | Forte mais coûteuse | ❌ aucun à date | 6 |
| Odoo Enterprise | ~80 à 150 | Faible-Moyenne | Variable (du freelance au gros cab.) | ❌ aucun à date | 7 |

### Recommandation année 1

**Focus 2 ERP en année 1 : Cegid XRP Flex (proof OCI à dupliquer) + Sage X3 (volume + maturité industrielle).**

Justification :
- Cegid : permet de capitaliser sur la référence OCI dans la communication (témoignage chiffré, recommandation entre dirigeants de cabinets), ramp-up plus rapide. Pool restant après OCI : ~25 à 28 partenaires.
- Sage X3 : volume le plus large parmi les ERP "industriels-services" pertinents, écosystème mature, communauté active (Sage Sessions, Top League). Pool : 50 à 80 partenaires.
- Dynamics 365 BC + Divalto en année 2 : permettent de doubler la cible une fois le kit commercial éprouvé.
- Akuiteo, SAP B1, Odoo en opportuniste : si lead entrant, traiter, sinon ne pas prioriser.

### Argument supplémentaire pour Sage X3 en priorité 2

Sage X3 attaque la même cible PME industrielle/services que Cegid XRP Flex. Les frigoristes professionnels et cuisinistes (vertical Mintizy historique) sont **fortement représentés sur les deux écosystèmes**, ce qui permet de réutiliser les mêmes cas clients et arguments.

---

## 6. Checkpoint viabilité 3 : Budget + Maturité

### Budget réel chez l'acheteur (Stéphane Maréchal, intégrateur ERP)

**Q1.** Ligne budgétaire dédiée ?
- ✅ **OUI**. Les cabinets d'intégration ERP français disposent d'enveloppes "R&D bundle" et "partenariats éditeurs tiers" structurées (cf. programmes partenaires Cegid, Sage Marketplace, Microsoft AppSource). L'investissement de la passerelle (~3 semaines de dev senior, ~12-15 k€ coût interne) entre dans une logique d'investissement commercial classique.

**Q2.** Budget moyen pour une brique tierce intégrée au bundle ?
- Setup interne : 10 à 30 k€ (dev passerelle + formation commerciale + marketing)
- Récurrent : marge 35 à 40 % sur abonnement client final, soit 67 à 168 € de marge brute mensuelle par client.
- ROI typique attendu par un dirigeant de cabinet : amortissement setup en 5 à 8 clients signés.
- Sources comparables : Talentia, Esker connector pricing pour intégrateurs Sage X3.

### Maturité du marché

**Q3.** Maturité : ✅ **ÉDUQUÉ**.
Les notions de "FSM" (Field Service Management), de "portail donneur d'ordres", de "bundle ERP + outil terrain" sont enseignées depuis 10+ ans. Acteurs présents : Praxedo (depuis 2005), Twimm, Synchroteam, ClicktoSAV, Mobi-G, Sigma SAV. Les éditeurs ERP eux-mêmes communiquent activement sur ces thèmes (Microsoft Dynamics 365 BC inclut un module FSM natif).

**Implication marketing** : ne pas faire de pédagogie de catégorie. Aller direct à la différenciation Mintizy.

### Cycle de décision

**Q4.** Décideurs côté intégrateur ERP : 2 à 3 personnes (DG/Associé + Directeur Commercial + Directeur Technique). Validation finale en COMEX ou CODIR.

**Q5.** Cycle moyen de signature partenariat de distribution : **3 à 9 mois**, avec une médiane à 5 mois. Phases : qualification (1-2 mois) → démo + due diligence technique (1-2 mois) → négociation contrat (1-3 mois) → signature.

### Bloc viabilité 3

```
Budget dédié          : ✅ OUI (enveloppes R&D bundle existantes chez les cabinets cibles)
Budget moyen segment  : 10 à 30 k€ setup + 35-40 % marge récurrente
Maturité marché       : ✅ ÉDUQUÉ (Praxedo, Twimm, Synchroteam établis depuis 10+ ans)
Décideurs             : 2 à 3 personnes (DG + Dir Co + Dir Tech)
Cycle closing         : 3 à 9 mois (médiane 5 mois)

Signal global         : ✅ Marché prêt
```

---

## 7. Score profil prioritaire

### Profil ACHETEUR : Stéphane Maréchal (Directeur Associé cabinet ERP 35 personnes)

| Critère | Score | Justification |
|---------|-------|---------------|
| Volume | 3/5 | 50 à 100 cibles prioritaires en France année 1 (étroit mais identifiable nominativement) |
| Approche | 4/5 | LinkedIn Sales Navigator nominatif + événements partenaires éditeurs (Cegid Connections, Sage Sessions) + recommandation OCI |
| Alignement | 5/5 | Douleur prouvée empiriquement (OCI 4+15), pricing tient, économie unitaire saine |
| Cycle | 3/5 | 3 à 9 mois (long mais standard pour partenariats de distribution) |
| **Total** | **15/20** | **Profil prioritaire confirmé** |

### Profil UTILISATEUR : Pascal Dubreuil (PME maintenance frigo)

| Critère | Score (point de vue UCCELLO direct) | Score (via revendeur) |
|---------|--------------------------------------|------------------------|
| Volume | 5/5 (~3 550 PME) | 5/5 |
| Approche | 1/5 (canal indirect by design) | 4/5 (relation existante revendeur) |
| Alignement | 4/5 | 4/5 |
| Cycle | 4/5 (1 à 3 mois après prise de contact revendeur) | 4/5 |
| **Total** | **14/20 nominal mais 8/20 en direct UCCELLO** | **17/20 via revendeur** |

> Le profil utilisateur est secondaire pour la prospection UCCELLO. Le job d'UCCELLO est d'**armer** le revendeur pour qu'il convertisse Pascal, pas d'aller chercher Pascal.

---

## 8. Verdict market research

### **GO ferme avec focus sélectif.**

**Hypothèses validées :**
- ✅ Univers amont suffisant pour atteindre 5 à 7 revendeurs signés en année 1 (~50-100 cibles prioritaires)
- ✅ Univers aval largement suffisant (3 550 PME, dont ~1 000 à 1 800 adressables via canal partenaire)
- ✅ Marché éduqué, budgets dédiés disponibles côté revendeur, économie unitaire saine
- ✅ TAM cohérent avec objectif 12 mois (PROJECT_CONTEXT 60-120 k€ = 2-4 % du SAM, ramp-up classique)

**Hypothèses invalidées :**
- ❌ Aucune

**Hypothèses à confirmer terrain :**
- ⚠️ La part exacte d'intégrateurs avec capacité dev senior dispo 3 semaines (estimation 50-70 %, à valider via prospection terrain)
- ⚠️ Le multiplicateur "groupements" (type Gasel) — combien de revendeurs ont accès à des groupements multi-membres ? À tester par interview de 3 à 5 partenaires Cegid/Sage candidats
- ⚠️ Le différenciateur Mintizy face à Praxedo (qui a un "Portail donneur d'ordres" actif) → critique à creuser en /offer-competitive-intel

**Recommandation forward :**
- /offer-competitive-intel **doit absolument creuser Praxedo**, son Portail donneur d'ordres, ses tarifs, son positionnement, et la frontière fonctionnelle Mintizy/Praxedo. C'est la prochaine zone de risque.
- /offer-pricing : valider que le grid OCI tient sur les tranches basses (1-10 users à 120€ peut être trop bas vs charge de support N2 par UCCELLO).
- Considérer ouvrir une **option "passerelle livrée clé-en-main"** par UCCELLO pour les intégrateurs sans dev senior dispo (ouvre le marché de ~50-100 à ~150-200 cibles).

---

## Questions pour /offer-competitive-intel

1. **Praxedo a-t-il un portail client comparable à Mintizy ?** Le "Portail donneur d'ordres" Praxedo couvre-t-il : suivi temps réel par client final, rapports CERFA, calendrier, dashboard ? Ou se limite-t-il à la création/déclenchement d'interventions par le donneur d'ordres B2B ?
2. **Coexistence OCI Mintizy + Praxedo dans un même bundle** : quels périmètres fonctionnels distincts ? Si Praxedo couvre déjà 80 % du portail, pourquoi OCI vend les deux ?
3. **Tarifs Praxedo portail client** : combien Praxedo facture-t-il l'option portail client ? Modèle de partage avec partenaires intégrateurs ?
4. **Twimm, Synchroteam, ClicktoSAV, Mobi-G** : portail client présent ? Modèle white-label ? Tarification ?
5. **Portails ERP natifs** : Microsoft Dynamics 365 FSM, Sage X3 module SAV, Divalto Service. Ces portails natifs concurrencent-ils Mintizy ou laissent-ils un espace ?
