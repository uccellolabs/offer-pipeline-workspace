# PROJECT_CONTEXT.md — Contexte du projet

> Remplis ce fichier AVANT de lancer les agents du pipeline.
> Sans contexte précis, les agents travaillent dans l'abstrait.

---

## L'entreprise

**Nom** — Uccello Labs
**Secteur** — Édition SaaS et outils métiers B2B
**Description (2 phrases)** — Uccello Labs analyse les processus métiers des organisations et conçoit des outils sur mesure, en s’appuyant sur l’IA pour automatiser tout ou partie de ces processus. L’offre s’adresse aux entreprises B2B qui veulent industrialiser des flux sans se contenter de logiciels génériques.
**Stade** — [ ] Idée  [ ] MVP  [x] Traction  [ ] Croissance établie

---

## Ressources disponibles

**Équipe commerciale** — Pas de commercial dédié : le gérant porte vision produit + prospection/closing. Exécution : COO (administratif, conseil de gestion), 2 développeurs focalisés produit.
**Budget acquisition** — [x] Bootstrapped  [ ] <2k€/mois  [ ] 2-10k€  [ ] >10k€
**Temps vente** — ~1,5 jour / semaine (prospection, devis, suivi commercial)
**Compétences vente** — Fort côté produit / technique et vision ; marketing opérationnel limité ; relation commerciale assumée par le gérant (pas de profil « pur commercial » en interne).

---

## Compétences + Orientations

> Utilisé par `/idea-finder` pour filtrer les opportunités business.

**Compétences techniques fortes** (ordre décroissant)
- Développement full-stack
- Résilience
- Capital sympathie (facile de créer du réseau) — moins à l’aise sur les réseaux sociaux

**Type de projet préféré**
[ ] SaaS B2B récurrent
[ ] Service / prestation haut de gamme
[ ] Produit digital one-shot
[x] Hybride (SaaS + sur-mesure)

**Marché cible préféré** (par ordre de priorité)
1. **TPE et PME** B2B (organisations qui veulent industrialiser des flux / outils métiers, sans être limitées à un secteur précis pour l’instant)
2. **Francophonie élargie** (priorité géographique)
3. **Canal** : **vente indirecte** d’abord (partenaires, distributeurs, intégrateurs) ; **vente directe** possible en complément au cas par cas

**Ce que vous REFUSEZ de construire** (même si rentable)
- Armée / défense
- Jeux d’argent
- Sexe et relation amoureuse (produits / marchés)
- Alcool
- Religion
- Occultisme
- Hypnose (y compris ericksonienne)

**Complexité technique acceptable** — **3/10**
*(1 = ultra-simple, livrer vite / 10 = R&D sur 2 ans)* — objectif : **démarrer vite**, avec une base **pérenne** et des **lots / commandes spécifiques** successifs (lot 1, 2, 3…).

---

## Contraintes

**Géographiques** — Francophonie élargie (priorité actuelle)
**Sectorielles** — Exclusions listées dans « Refus » ci-dessus. **Pas de secteur positif prioritaire** renseigné pour le moment (à affiner au fil des projets / idées).
**Légales / RGPD** — RGPD dans le cadre habituel B2B ; pas de positionnement « données santé / biométrie » comme cœur d’offre pour l’instant
**Ce que vous ne voulez PAS faire** — Pas de ligne rouge GTM stricte sur le modèle économique (freemium, forfait, etc.) : **priorité à la vente indirecte** ; vente directe possible en complément

---

## Stack technique / outils

**Outils utilisés en interne** — CRM : peu structuré aujourd’hui ; passage prévu sur **Axell** (produit maison — suivi de prospection). Gestion de projet : **Linear**. Facturation : **Pennylane**. Compta : **cabinet d’expertise comptable** (externalisé). Support client : surtout **e-mail** pour le moment ; **outil de support** (helpdesk / ticketing) à mettre en place.
**Intégrations possibles avec l'offre** — ERP et CRM du client ; écosystèmes **Google** et **Microsoft** ; **webhooks** ; toute stack exposant une **API** (intégration au cas par cas selon la doc et les contraintes client).
**Dépendances tierces critiques** — **IA** : modèles **open source**, inférence privilégiée via **Scaleway** (API IA) — le choix exact peut s’ajuster avec le client selon contraintes et besoins. **Auth** : développement **sur mesure** sur les projets livrés.

---

## Charte visuelle / Design system

> **Source canonique** : répertoire `design-system/` à la racine du pipeline.
> Fichiers clés : `design-system/README.md` (règles complètes), `design-system/colors_and_type.css` (tokens CSS), `design-system/SKILL.md` (usage agents), previews HTML sous `design-system/preview/`, prototype `design-system/ui_kits/website/`.

**Couleurs** (extraits — voir CSS pour l’échelle complète)
- **Primaire (marque)** : `#79d374` (vert — accent, CTA, focus glow)
- **Charcoal (texte / logo foncé)** : `#40434c`
- **Gris soutenu** : `#707279`
- **Navy (surfaces sombres / hero)** : `#1a1d2e` (et `#0f1120` plus profond)
- **Fonds clairs** : `#ffffff`, off-white `#f5f6f8`
- **Sémantique** : succès = vert marque ; warning / error / info = conventions standard (voir CSS)

**Typographies**
- **Titres & UI** : **Plus Jakarta Sans** (Google Fonts — proche du wordmark ; remplaçable si fichiers officiels dans `fonts/`)
- **Code / technique** : **JetBrains Mono**
- **Poids** : display 700–800 ; sous-titres 600 ; corps 400–500 ; tracking serré sur gros titres, caps espacées pour labels catégorie

**Logo**
- Fond clair : `design-system/assets/logo-uccello-labs.png`
- Fond sombre : `design-system/assets/logo-uccello-labs-white.png`
- Source fournie : `design-system/uploads/Logo Uccello Labs.png`, `design-system/uploads/Logo Blanc Uccello.png`

**Motif visuel signature**
- Géométrique arrondi (aligné logo), **vert vif** + **navy premium**, ombres douces (`shadow-md` …), rayons 4 / 8 / 12–16 / pill
- Pas d’illustrations « main dessinée », pas de dégradés agressifs ; option grille / texture très légère sur fonds navy
- **Icônes** : [Lucide](https://lucide.dev) recommandé (stroke 1.5px, cohérent avec le wordmark)

**Voix & ton** (pour copy / slides)
- Expert mais humain, **nous** institutionnel, phrases courtes, voix active
- Marque en **minuscules** dans le texte : *uccello.* selon README ; pas d’emoji en contexte pro
- UI produit : clair et efficace ; marketing : confiant, légèrement visionnaire

**Ton visuel** — Premium tech **accessible** (capacité haut de gamme sans rigidité « corporate » classique)

---

## Existant commercial

**Clients actuels** — Cœur de cible habituel : **PME ~5–10 collaborateurs**. Référence : un **groupe ~300 collaborateurs** (plus gros compte). **Mintizy (portail)** : **12** clients, **~2,7 k€ MRR** (détail sous Offre 1). Missions **sur-mesure** : non agrégées ici.
**Canaux déjà testés** — **Historique** : réseau personnel + **bouche-à-oreille** (principal levier). **Réseaux sociaux** : peu exploités / peu à l’aise pour l’instant — pas le canal d’acquisition prioritaire aujourd’hui.
**Réseau existant** — **OCI** — intégrateur **Cegid XRP Flex** ; **distributeur partenaire** du SaaS **Mintizy**. (Autres partenaires / LinkedIn : à compléter si besoin.)

---

## Offres existantes

> Les agents utilisent cette base pour les projets **idea** / offre groupe. Les briefs dédiés restent dans `projects/mintizy/`, `projects/axell/`, etc.

**Offre 1 — Mintizy**
- Nom — **Mintizy** (portail client — voir [mintizy.com](https://www.mintizy.com))
- Description (2 phrases) — Portail client **spécialisé dans le suivi de l’entretien des équipements** sur sites. **Canal OCI** : déploiement du **portail uniquement** ; **OCI ne commercialise pas** le reste de l’écosystème Mintizy (**app web** et **mobile**) — celui-ci reste hors périmètre distributeur.
- Prix actuel — **Portail client** : **120 € à 300 € / mois** selon **tranches d’utilisateurs** — **120 € / mois** jusqu’à **10 utilisateurs** ; **300 € / mois** pour **utilisateurs illimités**. **OCI** revend **+40 %** vs grille de référence.
- Clients actuels — **Vente directe** : **8** clients, **~1 882 € MRR**. **Via OCI** : **4** clients, **~840 € MRR** (autres dossiers OCI attendus). **Total indicatif** : **12** clients portail, **~2 722 € MRR** sur cette ligne.
- Ce qui fonctionne — **UX** : application **intuitive**, **prise en main rapide** **sans formation** structurée.
- Ce qui frotte — **Données incomplètes** à l’usage : parfois des **données manquantes** — origine **variable** (côté **Uccello Labs** ou **OCI** qui **n’expose pas / n’envoie pas** tout le flux nécessaire).

**Offre 2 — Axell**
- Nom — **Axell** (suivi de prospection — usage interne prévu, évolution produit possible)
- Description — Outil de **suivi de prospection** ; **utilisateurs illimités**. Canaux via **Unipile** (**coût interne ~5 €/canal/mois**). **Crédits** consommation (**coût ~0,02 €/crédit**). Grille **packs + canal optionnel + recharge** — voir `projects/axell/PRICING_BRIEF.md`.
- Prix actuel — **Packs** (indicatif, **veille marché** **v1.2**) : Pilote **59 € HT/mois** ; Croissance **79 € HT/mois** ; Équipe **119 € HT/mois**. **Canal +** **24 € HT/mois** (+ **350 crédits/mois**). **Recharge** : ex. **5 000 crédits ≈ 159 € HT**. Voir `projects/axell/PRICING_BRIEF.md`.
- Clients actuels — [interne / pilotes / revenus : à préciser]
- Ce qui fonctionne — [à compléter]
- Ce qui frotte — [à compléter]

---

## Ambition

**Objectif 12 mois** — **Plancher** : **~20 k€ MRR** avec **3 partenaires**. **Cible plutôt visée** : **~50 k€ MRR** avec **5 partenaires**.
**Objectif 3 ans** — Rester une **petite équipe**, **100 % remote**. **COO** aujourd’hui freelance : **possibilité d’embauche**. **Rôle du gérant** : moins l’**opérationnel**, plus le **réseau**, la **vision produit** et la **vente**. **Mix revenus visé** : **~80 % récurrent** (produits) / **~20 % sur-mesure**.

---

> Une fois rempli, lance `/idea-finder` ou `/offer-cadrage` pour démarrer.
