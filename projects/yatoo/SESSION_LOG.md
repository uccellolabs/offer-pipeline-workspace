# SESSION_LOG.md — Journal du pipeline

> Créé automatiquement par le premier agent lancé sur le projet.
> Mis à jour à chaque étape.
> Évite aux agents de relire tous les fichiers en détail.

---

## Statut du pipeline

```
/idea-finder         : ⬜ Non lancé
/offer-cadrage       : ✅ 2026-05-04
/persona             : ✅ 2026-05-04
/market-research     : ✅ 2026-05-04
/competitive-intel   : ✅ 2026-05-04
/pricing             : ✅ 2026-05-04
/offer-final         : ✅ 2026-05-04
/offer-study-website : ✅ 2026-05-04
/pitch-deck          : ⬜ Non lancé
/prospection-strategy: ⬜ Non lancé
/cold-call           : ⬜ Non lancé
/discovery-call      : ⬜ Non lancé
```

---

## Décisions clés

*(Format : [DATE] [AGENT] — [décision] — [output])*

[2026-05-04] [/offer-project-manager] — Projet yatoo créé. PROJECT_CONTEXT.md alimenté depuis le CdC YATOO v1.0 (Avril 2026). Offre : plateforme SaaS mobile-first de gestion de panneaux LED Coworker Smart Panel. Stack : Laravel + React + Flutter + PostgreSQL + Redis + S3 + IA Nano Banana. — PROJECT_CONTEXT.md initialisé.

[2026-05-04] [/offer-pricing] — Modèle hybride D. SaaS : Starter 19€ / Pro 29€⭐ / Business 59€ / Enterprise devis. Bundle all-inclusive 99€/mois (panneau + SaaS 36 mois). ROI restaurateur : 7 semaines. Revendeur actif : -40%. Pas de boucle requise (prix < budget max persona). → PRICING_BRIEF.md v1.0 créé.

[2026-05-04] [/offer-market-research] — Canal D (Mixte) : Direct J1-90 → Revendeurs CHR/pharmacies M4+. SAM ~26 600 établissements. Profil prioritaire : restaurateur (16/20). Viabilité 3 : ⚠️ À travailler (cold start, double vente). → OFFER_BRIEF enrichi.

[2026-05-04] [/offer-competitive-intel] — Concurrents principaux : OptiSigns (10$/mois, IA, 1000+ templates), Yodeck (gratuit 1 écran, 7000+ avis), Cenareo (FR enterprise). Zone différenciante YATOO : bundle hardware+SaaS+service français (aucun concurrent ne couvre les 3). Pas de recommandation de boucle vers /offer-cadrage. → COMPETITIVE_BRIEF.md v1.0 créé.

[2026-05-04] [/offer-cadrage] — Verdict GO avec réserve. Points bloquants : concurrence non analysée (Yodeck, ScreenCloud…), go-to-market TPE inadapté au canal actuel, périmètre hardware non tranché. Douleur restaurateur 7/10 — signal prioritaire. → OFFER_BRIEF.md v1.0 créé.

[2026-05-04] [DÉCISION UX] — Précisions contenu : vidéo = upload S3 uniquement (pas d'IA, pas de limite taille/durée au MVP). Carousel = durée configurable par image + durée par défaut (valeur à définir), boucle automatique. — SESSION_LOG mis à jour.

[2026-05-04] [DÉCISION UX] — Flux de création de contenu style Typeform (une question à la fois). Étape 1 : type de contenu (image / carousel / vidéo). Étape 2 si image/carousel : source (images existantes OU génération IA). Étape 3 si IA : choix du template (champs prédéfinis par template : titre, tarif, description…). Étape 4 : formulaire adaptatif selon template. Résultat : images générées/configurées → diffusion directe sur le panneau. — Aucun fichier produit (décision de conception).

[2026-05-04] [/offer-final] — Verdict : ⚠️ VIABLE SOUS CONDITIONS. Score douleur 7/10, prospectabilité 8/10, marché ⚠️. 4 conditions non-négociables avant lancement. Offre commerciale complète rédigée (10 sections). → OFFER_FINAL.md v1.0 créé.

[2026-05-04] [/offer-study-website] — Site interne généré. Mode A (interne), HTML/CSS/JS pur, hébergement yatoo.offer.uccellolabs.com, protection mot de passe "Yatoo!" (SHA-256). 10 pages : login, index, offre, persona, marché, concurrence, pricing, viabilité, contact, 404. Design system YATOO (Space Grotesk + Inter, navy/amber/blue). → website/ créé.

---

## Versions des fichiers

| Fichier | Version actuelle | Date | Changement |
|---------|-----------------|------|------------|
| IDEA_BRIEF.md | — | — | — |
| OFFER_BRIEF.md | 1.0 | 2026-05-04 | Création initiale — verdict GO avec réserve concurrence |
| PERSONA_ACHETEUR.md | — | — | — |
| PERSONA_UTILISATEUR.md | — | — | — |
| COMPETITIVE_BRIEF.md | 1.0 | 2026-05-04 | Création — 6 concurrents analysés, zone différenciante : bundle hardware+SaaS+FR |
| PRICING_BRIEF.md | — | — | — |
| OFFER_FINAL.md | — | — | — |
| PITCH_DECK.pptx | — | — | — |

---

## Apprentissages terrain

> Rempli par l'utilisateur après tests, interviews ou retours prospects.
> Format : `[DATE] — [source] — [apprentissage] — [agent impacté]`
>
> Exemple : `2026-05-12 — Interview ESN X — Budget max 500€/mois, pas 2000€ — /pricing à revoir`

---

## Points de blocage / décisions en suspens

> Les agents notent ici ce qui nécessite une validation humaine avant de continuer.

- [2026-05-04] Logo YATOO non fourni dans le CdC — à intégrer pour pitch-deck et site web
- [2026-05-04] Pricing chiffré (€/mois par plan) non défini — à valider avec clients pilotes
- [2026-05-04] Budget acquisition mensuel non précisé
- [2026-05-04] Objectifs ARR 12 mois non chiffrés
- [2026-05-04] CLARIFICATION : Uccello Labs est la société qui développe le SaaS pour le compte de YATOO (client). Le pipeline analyse l'offre que YATOO commercialisera auprès des TPE. YATOO = client/distributeur. Uccello Labs = développeur/éditeur de la solution.
- [2026-05-04] ⚠️ CORRECTION MAJEURE : Les panneaux LED sont un NOUVEAU produit, marché différent de l'offre Coworker actuelle. Zéro client, zéro base installée, départ à froid sur hardware ET SaaS. Le réseau de 150 partenaires est B2B industriel — incompatible avec la cible TPE commerçants. Tous les fichiers impactés ont été corrigés.
- [2026-05-04] CMS natif panneaux = boîte noire — exploration technique nécessaire avant développement Flutter
- [2026-05-04] Périmètre hardware non tranché : Coworker-only vs ouvert à d'autres marques de panneaux — décision stratégique à prendre avant architecture
- [2026-05-04] Nano Banana (IA image) non validé publiquement — qualité, latence, coût par appel, SLA à vérifier
- [2026-05-04] Go-to-market TPE à repenser — canal partenaires industriels actuels inadapté pour restaurateurs/pharmaciens
