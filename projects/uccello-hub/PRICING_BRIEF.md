# PRICING_BRIEF.md
- Date : 2026-04-25 | Version : 2.0 | Agent : pricing | Type offre : D (Hybride SaaS + Accompagnement)
- Mise à jour : grille par tranches d'utilisateurs + coûts IA réels Scaleway gpt-oss-120b

---

## Valeur économique

### Pour Claire (utilisateur final — agence marketing 12 personnes)

| Hypothèse | Calcul | Valeur |
|-----------|--------|--------|
| 30 min/jour récupérées × 12 collaborateurs | 6h/jour × 40€/h chargé × 20j/mois | 4 800€/mois |
| 1h/jour récupérées (optimiste) | 12h × 40€ × 20j | 9 600€/mois |
| Valeur annuelle conservatrice | 4 800 × 12 | 57 600€/an |
| **Prix value-based (10-20%)** | | **480 – 960€/mois** |

**Hypothèses :** Collaborateur agence 40€/h chargé (~3 500€ brut/mois). Gain de 30 min/jour sur la recherche d'infos entre outils. Estimation conservatrice.

Budget max Claire (300-800€/mois) ✅ — aligné avec la valeur créée.

---

## Coûts IA réels — Scaleway gpt-oss-120b

**Tarifs (source : scaleway.com, avril 2026)**
- Input : 0,15€/million de tokens
- Output : 0,60€/million de tokens
- Batches API (non temps-réel) : -50%

**Structure du master prompt (fixe, envoyé à chaque interaction) :**

| Composante | Tokens |
|-----------|--------|
| Instructions système + comportement agent | ~1 500 |
| Définitions outils (30 outils × 400 tokens) | ~12 000 |
| Contexte entreprise (knowledge base) | ~2 000 |
| Profil utilisateur + droits d'accès | ~500 |
| **Total master prompt** | **~16 000 tokens/interaction** |

**Calcul par interaction :**
- Input total : 16 000 (master) + 200 (question) + 1 800 (RAG + historique) = **~18 000 tokens**
- Output : **~600 tokens**

**Coût IA mensuel par tranche d'utilisateurs (usage standard = 10 interactions/jour/user) :**

| Tranche | Users | Input tokens/mois | Output tokens/mois | Coût IA/mois |
|---------|-------|------------------|--------------------|-------------|
| Starter | 1–5 (moy. 3) | 3×10×18k×22 = 11,9M | 3×10×600×22 = 396k | **1,79€ + 0,24€ = ~2€** |
| Team | 6–15 (moy. 10) | 10×10×18k×22 = 39,6M | 10×10×600×22 = 1,32M | **5,94€ + 0,79€ = ~7€** |
| Business | 16–30 (moy. 20) | 20×10×18k×22 = 79,2M | 20×10×600×22 = 2,64M | **11,88€ + 1,58€ = ~14€** |
| Scale | 31–50 (moy. 40) | 40×10×18k×22 = 158,4M | 40×10×600×22 = 5,28M | **23,76€ + 3,17€ = ~27€** |

**Usage intensif (+50% interactions, 15 interactions/jour) :** multiplier par 1,5

---

## Architecture de tiers

### NIVEAU 1 — Uccello Labs → Partenaire (Licence Revendeur)

**Règle : tarif revendeur = 50% du tarif public conseillé. Zéro coût d'entrée.**

| Tier | Users IA | Prix Uccello Labs → Partenaire | Prix public recommandé |
|------|----------|---------------------|----------------------|
| **Starter** | 1–5 | 99€/mois | 199€/mois |
| **Team** | 6–15 | 174€/mois | 349€/mois |
| **Business** | 16–30 | 274€/mois | 549€/mois |
| **Scale** | 31–50 | 399€/mois | 799€/mois |
| **Enterprise** | 50+ | Sur devis | Sur devis |
| **On-premise Partenaire MSP (flat)** | Capacité totale Partenaire | 499–1 499€/mois | Sur devis |
| **On-premise client final** | Par client | 1 000–2 000€/client/mois | Sur devis |
| **Accès plateforme (base)** | — | 99€/mois | — |

**Inclus dans la licence Uccello Labs → Partenaire :**
- SaaS : hébergement (serveur mutualisé + DB dédiée + S3), support N2, updates
- On-premise : support N2 dédié, audit sécurité, kit déploiement, accompagnement

---

### NIVEAU 2 — Partenaire → Client final (Grille recommandée)

Le Partenaire est libre de ses prix. Uccello Labs lui fournit cette grille comme référence.

| Tier | Users IA | Prix public HT | Connecteurs inclus | Setup recommandé |
|------|----------|---------------|---------------------|-----------------|
| **Starter** | 1–5 | 199€/mois | 3 | 500€ |
| **Team ⭐** | 6–15 | 349€/mois | 6 | 800€ |
| **Business** | 16–30 | 549€/mois | 10 | 1 200€ |
| **Scale** | 31–50 | 799€/mois | Illimité | 1 500€ |
| **Enterprise** | 50+ | Sur devis | Illimité | Sur devis |

**Connecteurs supplémentaires (hors pack) :** 50€/connecteur/mois (recommandé Partenaire)

---

## Modes de déploiement

| Mode | Hébergement IA | Coût Uccello Labs | Coût IA Partenaire | Recommandé pour |
|------|---------------|---------------|-------------|-----------------|
| **SaaS multi-tenant** | Uccello Labs | Prix tier ci-dessus | 0€ (inclus) | PME standard |
| **Scaleway souverain** | Partenaire (Scaleway) | Prix tier ci-dessus | 2–27€/mois selon tier | PME RGPD sensible |
| **On-premise chez Partenaire (MSP)** | Partenaire (ses serveurs) | Licence capacitaire flat — voir section dédiée ci-dessous | ~5–30€/mois (infra Partenaire) | Partenaire autonome, multi-clients depuis 1 infra |
| **On-premise chez le client final** | Client final | 1 000–2 000€/mois/client | ~5–20€/mois (infra client) | Client avec données très sensibles, déploiement dédié |

---

## Marge Partenaire — Simulations par tier

### Tier Team (6-15 users) — le sweet spot agence marketing

| Flux | Montant |
|------|---------|
| Partenaire facture le client final | +349€/mois |
| Coût Uccello Labs | -174€/mois |
| Coût IA Scaleway (usage standard ~7€) | -7 à 15€/mois |
| **Marge brute Partenaire** | **160–168€/mois (46–48%)** |
| Setup 800€ (100% marge Partenaire) | +800€ à la signature |
| Conseil / formation (100% Partenaire) | Variable |

### Tier Business (16-30 users)

| Flux | Montant |
|------|---------|
| Partenaire facture le client final | +549€/mois |
| Coût Uccello Labs | -274€/mois |
| Coût IA Scaleway (~14€) | -14 à 25€/mois |
| **Marge brute Partenaire** | **250–261€/mois (46–47%)** |
| Setup 1 200€ (100% marge Partenaire) | +1 200€ à la signature |

**Marge Uccello Labs (SaaS Team à 174€) :**
- Coûts serveur + DB + S3 : ~10-15€/client/mois
- **Marge nette Uccello Labs : ~159€/client/mois (91%)**

---

## Chemin vers les objectifs

### Objectif Uccello Labs 12 mois : 10 000€ MRR

```
3 revendeurs × 17 clients Team SaaS = 51 clients × 174€ = 8 874€/mois
+ 3 × 99€ accès plateforme                               =   297€/mois
Total                                                     = 9 171€/mois

Avec mix Team + Business (20% Business) :
= 41 clients Team × 174€ + 10 clients Business × 274€ = 9 874€ ✅

Rythme : ~1,4 client/mois/revendeur dès mois 4
```

### Objectif Partenaire : MRR confortable (tier Team)

| Nb clients | MRR Partenaire brut | Coûts (Uccello Labs + IA) | MRR net Partenaire | + Setups annuels |
|-----------|--------------|----------------------|-------------|-----------------|
| 3 clients | 1 047€ | 3×181€ = 543€ | **504€** | 3×800€ = 2 400€ |
| 5 clients | 1 745€ | 5×181€ = 905€ | **840€** | 5×800€ = 4 000€ |
| 10 clients | 3 490€ | 10×181€ = 1 810€ | **1 680€** | 10×800€ = 8 000€ |
| 20 clients | 6 980€ | 20×181€ = 3 620€ | **3 360€** | 20×800€ = 16 000€ |

*Coût total Partenaire/client Team = 174€ (Uccello Labs) + 7€ (IA Scaleway) = 181€*
*Hors conseil, formation et renouvellement setup*

---

---

## On-premise chez Partenaire (MSP) — Licence capacitaire flat

**Contexte :** Partenaire déploie Uccello Hub sur ses propres serveurs. Une seule installation multi-tenant dessert l'ensemble de ses clients. Partenaire gère l'infra, le support N1 et la disponibilité. Uccello Labs fournit la licence logicielle, les mises à jour et le support N2.

**Différence fondamentale avec l'on-premise client :**
- On-premise client → une installation par client final → tarif par client (1 000–2 000€/client/mois)
- On-premise Partenaire MSP → UNE installation pour tous ses clients → tarif capacitaire FLAT basé sur le volume total d'utilisateurs sur son infra

**Validation marché (sources on-premise réelles) :**
- OnPremiseAgent (plateforme agents IA on-premise) : $499/mois → 10 intégrations, 5 workflows / $1 499/mois → 30+ intégrations, 25 workflows
- n8n Business self-hosted : $667/mois
- Mattermost Professional self-hosted : $10/user/mois
- Chatwoot Enterprise self-hosted : $99/agent/mois
- AirgapAI perpétuel : $697/user one-time

**Grille licence MSP Uccello Labs → Partenaire (capacité totale sur infra Partenaire) :**

| Tier MSP | Capacité totale (tous clients) | Équivalent clients typiques | Prix mensuel | Setup one-time |
|----------|-------------------------------|----------------------------|-------------|---------------|
| **Starter MSP** | ≤20 users | 2–4 clients (5 users moy.) | **499€/mois** | 2 000€ |
| **Growth MSP** | 21–50 users | 5–10 clients | **899€/mois** | 2 500€ |
| **Professional MSP** | 51–100 users | 10–20 clients | **1 499€/mois** | 3 000€ |
| **Enterprise MSP** | 100+ users | 20+ clients | **Sur devis** | Sur devis |

**Option annuelle (incentive engagement 12 mois) :**
- Starter MSP : 4 990€/an (~416€/mois, −17%)
- Growth MSP : 8 990€/an (~749€/mois, −17%)
- Professional MSP : 14 990€/an (~1 249€/mois, −17%)

**Référence marché : OnPremiseAgent Starter = $499/mois, Professional = $1 499/mois → Uccello Hub est parfaitement aligné pour un outil plus complet (IA souveraine + centralisation data + multi-outils).**

**Inclus dans la licence MSP :**
- Kit déploiement + documentation technique
- Support N2 dédié (Uccello Labs → Partenaire uniquement, pas avec les clients finaux)
- Mises à jour logicielles incluses
- Audit sécurité initial (1 session)

**Non inclus (à la charge de Partenaire) :**
- Infrastructure serveur (hébergement, VPS, BDD)
- Modèle IA (Scaleway ou autre — ~5 à 30€/mois selon usage)
- Support N1 des clients finaux
- Supervision et maintenance de l'infra

**Simulation marge Partenaire (Growth MSP — 8 clients Team 10 users = 80 users) :**

| Flux | Montant |
|------|---------|
| Partenaire facture 8 clients × 349€ | +2 792€/mois |
| Licence Uccello Labs (Growth MSP 899€) | -899€/mois |
| Infra Partenaire (serveur + BDD + S3) | -80 à 120€/mois |
| Coût IA Scaleway (80 users) | -50 à 80€/mois |
| **Marge brute Partenaire** | **~1 693–1 763€/mois (61–63%)** |
| Setup (8 × 800€, 100% marge Partenaire) | +6 400€ à la signature |

*Comparaison vs SaaS (même 8 clients Team) : Partenaire payait 8 × 174€ = 1 392€/mois à Uccello Labs. En MSP, il paye 899€/mois. Économie : 493€/mois, soit +35% de marge supplémentaire pour Partenaire.*

**Attention — Trade-off Uccello Labs :**
- SaaS 8 clients Team : 8 × 174€ = **1 392€/mois** pour Uccello Labs
- MSP Partenaire 8 clients : **899€/mois** pour Uccello Labs → -35% de revenus
- Uccello Labs cède de la marge contre la disparition de l'opérationnel (hébergement, incidents infra, scalabilité)
- Rentable pour Uccello Labs dès que Partenaire gagne en autonomie ET permet à Uccello Labs de se concentrer sur l'acquisition de nouveaux revendeurs

**Clause recommandée :** Engagement minimum 12 mois. Palier de révision tarifaire tous les 12 mois si capacité dépasse le tier.

---

## Pricing revendeur — Synthèse complète

| Partenaire | Modèle | Prix | Justification |
|------------|--------|------|---------------|
| **Revendeur SaaS (Partenaire)** | 99€/mois accès + 50% prix public/client | 99€ + 174–399€/client | Uccello Labs héberge, Partenaire vend et supporte N1 |
| **Revendeur MSP (Partenaire hosts)** | Licence capacitaire flat | 499–1 499€/mois + setup | Partenaire héberge pour tous ses clients, 1 seule instance |
| **On-premise client final** | Par client, prix élevé | 1 000–2 000€/client/mois | Déploiement dédié chez chaque client, plus de travail Uccello Labs |
| **Apporteur d'affaires** | Commission | 10–20% premier abonnement annuel | Lead uniquement, pas de support |

---

## Justifications prêtes

**ROI Partenaire (tier Team) :**
> "Votre premier client Team vous rapporte 160€ net/mois + 800€ de setup. Votre accès plateforme (99€) est couvert dès le 1er client. Chaque client supplémentaire = MRR pur à 46% de marge."

**ROI Claire (12 personnes, tier Team) :**
> "30 minutes récupérées par collaborateur et par jour = 4 800€ de coût salarial économisé chaque mois. Votre abonnement à 349€ est remboursé en moins de 2 jours ouvrés."

**vs ProSuite (Partenaire) :**
> "ProSuite vous permet de construire des apps from scratch. Uccello Hub connecte ce que vos clients ont déjà et leur garantit la souveraineté des données — ce que ProSuite ne peut pas offrir."

**vs Microsoft Copilot (Claire) :**
> "Copilot à 19.70€/user = 236€/mois pour 12 personnes, limité à M365 et données sur cloud américain. Uccello Hub à 349€ couvre TOUS vos outils et vos données restent sur votre infrastructure."

**Coût IA transparent (Partenaire) :**
> "Avec Scaleway gpt-oss-120b, le coût IA réel pour 10 collaborateurs en usage quotidien est de 7 à 15€/mois. Vous maîtrisez vos coûts à la virgule."

---

## Réponses objections prix

| Objection | Réponse |
|-----------|---------|
| "174€/client c'est trop" (Partenaire) | "Votre marge est de 160€/mois + 800€ setup. Rentable dès le 1er client signé." |
| "ProSuite est gratuit" (Partenaire) | "ProSuite ne garantit pas la souveraineté. Vos clients vous demandent où vont leurs données — vous aurez la réponse, eux non." |
| "349€/mois c'est cher" (Claire) | "30 min/personne/jour × 12 collaborateurs = votre abonnement remboursé en 2 jours ouvrés." |
| "Pas de budget" (Claire) | "Vous dépensez déjà 360-960€/mois en SaaS non connectés. Uccello Hub remplace une partie de ce coût et les connecte." |
| "Je veux tester avant" (Partenaire) | "Premier mois offert. Vous configurez votre sandbox, faites une démo chez un client — sans rien débourser." |
| "Et si mes clients sur-utilisent ?" (Partenaire) | "Avec gpt-oss-120b, même 15 users à 20 requêtes/jour = ~30€ de coût IA. Pas de mauvaise surprise." |

---

## Utilisation pipeline

- **/offer-final** → Justifications ROI + phrase de positionnement + grille par tiers
- **/pitch-deck** → Slide pricing : grille 2 niveaux + simulation MRR Partenaire + coûts IA réels
