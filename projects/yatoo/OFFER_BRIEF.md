# OFFER_BRIEF.md
- Date : 2026-05-04 | Version : 1.0 | Agent : offer-cadrage | Statut : GO ⚠️ (réserve concurrence)

---

## PIPELINE SUMMARY

```
Idée        : Plateforme SaaS mobile-first pour piloter les panneaux LED en < 90s depuis un smartphone
Cible       : TPE commerçants (restaurateurs, pharmaciens, agents immobiliers) — à affiner par /offer-persona
Problème    : Le CMS natif des panneaux est inutilisable au quotidien (15 min pour un changement de texte, pas de mobile, pas d'IA, pas de multi-panneaux)
Valeur      : Mise à jour du contenu en < 90s, sans formation, depuis un smartphone, avec génération IA de visuels brandés
Canal       : D — Mixte (Direct J1-90 → Revendeurs CHR/pharmacies/immo M4+)
Concurrent  : OptiSigns (10$/mois, IA, 1000+ templates) + Yodeck (gratuit 1 écran, 7000+ avis) + Cenareo (FR enterprise) — tous software-only, aucun bundle hardware
Prix cible  : Pro SaaS 29€/mois | Bundle all-inclusive 99€/mois (panneau + SaaS 36 mois) | ROI 7 semaines
Verdict     : ✅ GO — sous condition d'analyse concurrentielle préalable
Pipeline    : Idea — | Cadrage ✅ | Persona ✅ | Market ✅ | Competitive ✅ | Pricing ✅ | Final ✅ | Website ✅ | Deck ⬜
```

---

## 1. Idée en une phrase

**YATOO** aide les **professionnels non-techniques propriétaires de panneaux LED** à **mettre à jour leur affichage en moins de 90 secondes depuis leur smartphone** grâce à **une plateforme SaaS mobile-first avec génération d'images par IA et diffusion WebSocket temps réel**.

---

## 2. Problème résolu

**Principal** — Le CMS natif livré avec les panneaux LED du marché est inutilisable pour un usage professionnel quotidien : interface complexe, 15 min pour changer un texte, non adapté au mobile, absence d'IA, gestion panneau par panneau uniquement.

**Sans cette offre** — Les panneaux restent avec du contenu statique pendant des jours ou des semaines. La valeur perçue du matériel s'effondre. Le taux de churn sur l'abonnement SaaS est élevé faute d'usage.

**Qui souffre le plus** — Le restaurateur (usage quotidien, le matin avant l'ouverture, sur smartphone). C'est le persona avec la douleur la plus intense et la fréquence la plus haute.

---

## 3. Cible

**Acheteur** — Gérant / dirigeant TPE (décide de l'abonnement SaaS + éventuellement du panneau physique)

**Utilisateur final** — Variable selon le persona :
- Restaurateur : le gérant lui-même
- Pharmacien : le préparateur délégué
- Agent immobilier : l'assistant(e) d'agence

**Intermédiaire** — Les 150+ partenaires YATOO (revendeurs actuels du hardware) sont un canal de distribution potentiel à activer — mais leur profil B2B industriel ne correspond pas encore à la cible TPE commerçants. Adaptation nécessaire.

---

## 4. Valeur

**Pour l'acheteur (dirigeant TPE)**
- Rentabilise le panneau physique déjà acheté (qui sinon affiche du contenu obsolète)
- Élimine la dépendance à un graphiste ou à un technicien pour chaque mise à jour
- Revenu récurrent prévisible (side benefit pour YATOO, avantage client = maîtrise des coûts)

**Pour l'utilisateur final**
- Mise à jour en < 90 secondes depuis un smartphone
- Visuels professionnels générés automatiquement sans compétences graphiques
- Diffusion instantanée sur un ou plusieurs panneaux simultanément

**Valeur quantifiable estimée**
- Restaurateur : 15 min/jour × 250 jours/an = 62h/an récupérées. À 20-30€/h équivalent dirigeant = 1 200-1 800€/an de valeur temps.
- Si l'abonnement est ≤ 20% de cette valeur → prix plancher ~20-30€/mois défendable.

---

## 5. Verdict Devil's Advocate

### ✅ Ce qui tient

- Douleur marché documentée : le CMS natif des panneaux LED est universellement critiqué — les concurrents SaaS existent parce que le problème est réel
- Pivot récurrent pertinent : l'activité tablette est saisonnière, le SaaS mensuel est une réponse structurelle solide
- Douleur restaurateur forte (7/10) : usage quotidien, friction mesurable, pain bien articulé
- UX Typeform décidée : une question à la fois, mobile-first — bonne réponse au profil non-technique de la cible
- ADN Android professionnel de YATOO : compétences techniques réelles pour développer l'app Flutter kiosque

### ❌ Ce qui ne tient pas

- **Concurrence non analysée** : Le marché digital signage SaaS est mature (Yodeck, ScreenCloud, OptiSigns, Fugo, Signagelive, NoviSign…). Plusieurs proposent déjà Android + templates + IA + multi-écrans. YATOO doit identifier son angle différenciant AVANT de construire, pas après.
- **Go-to-market inadapté** : ADN grands comptes industriels incompatible avec vente TPE (ticket 10x plus faible, volume 10x nécessaire, cycle 5x plus court). Les 150 partenaires actuels ne sont pas le bon canal pour atteindre les restaurateurs et pharmaciens.
- **Périmètre hardware flou** : Plateforme compatible uniquement avec les panneaux YATOO/Coworker (marché limité aux prospects acceptant ce hardware) ou ouverte à d'autres marques de panneaux déjà en place chez les TPE (complexité technique multipliée) ? Ce choix stratégique n'est pas tranché dans le CdC — il conditionne l'adressable total.

### ⚠️ Hypothèses non vérifiées

- Les gérants de TPE qui ont déjà un panneau LED (marque quelconque) se plaignent activement du CMS natif et seraient prêts à payer pour une alternative — à valider terrain (interviews prospects)
- Les restaurateurs sont prêts à payer un abonnement SaaS EN PLUS du panneau physique déjà acheté
- L'API Nano Banana (IA image) produit des visuels suffisamment professionnels en < 30s au coût acceptable — aucune validation publique disponible
- Les templates métiers (restaurant, pharmacie, immobilier) couvriront les cas d'usage réels sans personnalisation graphiste

### 🚧 Contraintes projet

- CMS natif des panneaux = boîte noire : exploration technique obligatoire avant développement Flutter
- Stack complexe (WebSocket + Android kiosque + IA + offline) = délai de livraison MVP non trivial (estimation : 4-6 mois minimum avec équipe dédiée)
- RGPD : données en UE, logs 12 mois, consentement analytics — contrainte à intégrer dès l'architecture

---

## 5b. Checkpoint viabilité 1 — Intensité de la douleur

- **Score douleur : 7/10** — Fort sur le segment restauration (quotidien), modéré sur pharmacie (hebdomadaire) et immobilier (habitudes établies). Douleur estimée — non validée terrain (zéro client actuel).
- **Déjà dépensé pour résoudre : Non validé** — ⚠️ CORRECTION : les panneaux LED sont un nouveau produit. Aucun client existant n'a encore acheté le hardware YATOO. La douleur du CMS natif est réelle sur le marché mais pas encore vécue par des clients YATOO. Départ à zéro — validation terrain requise avant d'investir.
- **Signal : ⚠️ À valider** — La douleur marché est documentée (concurrents existent, CMS natifs mauvais) mais YATOO n'a pas encore de client pour la confirmer en direct. Interviews prospects obligatoires avant lancement.

---

## 6. Direction recommandée

**[x] GO — sous condition**

**Justification :** L'offre est viable et le timing logique (marché en croissance, modèle récurrent inexistant chez YATOO, douleur terrain documentée sur le marché). Le risque principal n'est pas dans le produit — il est dans le go-to-market et la concurrence. Lancer le développement avant d'avoir analysé les solutions concurrentes existantes serait une erreur coûteuse : YATOO risque de reconstruire ce qui existe déjà à un prix de marché inférieur. La priorité immédiate est `/offer-competitive-intel` pour identifier les angles non couverts, puis `/offer-market-research` pour valider le canal de distribution adapté aux TPE. La décision hardware-only vs ouvert aux tiers panneaux doit également être tranchée avant de commencer l'architecture.

---

## 7. Questions prioritaires pour /offer-persona

1. Le restaurateur qui a déjà un panneau LED utilise-t-il le CMS natif livré avec, ou a-t-il abandonné ? Depuis quand le panneau affiche-t-il le même contenu ?
2. Qui prend la décision d'achat d'un abonnement SaaS dans une TPE restauration — le gérant seul, ou son comptable / franchise ?
3. Le pharmacien titulaire délègue-t-il la mise à jour à un préparateur : quelle est la tolérance de ce préparateur pour un outil numérique ? Niveau de compétence réel ?
4. L'agent immobilier parle de synchronisation avec son logiciel métier comme critère de succès — est-ce un vrai besoin différenciant ou une aspiration secondaire ? Quel logiciel métier exactement ?
5. Pour chaque persona : quel est le budget mensuel déjà alloué à la communication digitale locale (réseaux sociaux, Google Ads, affiches…) ? C'est contre ce budget que le SaaS va se positionner, pas contre zéro.

---

## MARKET RESEARCH UPDATE
- Date : 2026-05-04 | Canal : D — Mixte (Direct J1-90 → Revendeurs/Prescripteurs M4+) | Sources : web search (Statista, DREES, FNAIM, INSEE, Spherical Insights)

### Volumes marché France

| Segment | Établissements FR | SAM estimé | SOM réaliste Y1-2 |
|---------|-------------------|-----------|-------------------|
| Restauration traditionnelle | ~180 000 | ~18 000 (10% adoption affichage) | 100-300 clients |
| Pharmacies / officines | ~20 500 | ~4 100 (20% intérêt) | 50-150 clients |
| Agences immobilières | ~30 000 | ~4 500 (15% intérêt) | 30-100 clients |
| **Total** | **~230 500** | **~26 600** | **180-550 clients** |

TAM digital signage SaaS France : fraction d'un marché de 1,29 Mrd USD (2025) → segment TPE ~50-80 M€ sur 5 ans (estimé).

### Canal : D — Mixte

- **J1-90** : Direct terrain — démonstrations live, 10-30 clients pilotes restaurateurs
- **M4+** : Revendeurs CHR (Metro, Brake), groupements pharmacies (GIROPHARM, PHR), FNAIM régionale

### Profil prioritaire : Restaurateur — Score 16/20

Volume 4/5 | Approche 3/5 | Alignement 5/5 | Cycle 4/5

### Checkpoint viabilité 3

```
Budget dédié          : ⚠️ Dépense nouvelle (pas de ligne "panneau LED + SaaS" existante)
Budget annuel combiné : ~1 300-1 800€/an (leasing ~80€/mois + SaaS ~30-40€/mois)
Maturité marché       : ⚠️ Conscient — connaît l'affichage dynamique, ne connaît pas YATOO
Décideurs             : 1 personne (gérant TPE — décision solo)
Cycle closing         : 1-4 semaines si démonstration terrain convaincante
Signal global         : ⚠️ À travailler — marché réel, cold start exige effort commercial
```

### Hypothèses clés

- ✅ Marché existe : 230k+ établissements potentiels
- ✅ Budget communication disponible : les TPE dépensent dans la pub locale (~11 Mrd€/an FR)
- ❌ Canal partenaires YATOO : incompatible avec la cible TPE (B2B industriels uniquement)
- ⚠️ Double vente hardware + SaaS en cold start = effort commercial doublé

### Questions pour /offer-pricing

1. Leasing panneau (~80€/mois) + SaaS (~30€/mois) = ~110€/mois : acceptable sur le budget com d'un restaurateur ?
2. Bundle all-inclusive (panneau compris dans l'abonnement) plus simple à vendre qu'une double transaction ?

---

## Prochaine étape recommandée : /offer-competitive-intel → /offer-pricing
