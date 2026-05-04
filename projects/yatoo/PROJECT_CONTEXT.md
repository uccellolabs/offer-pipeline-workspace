# PROJECT_CONTEXT.md — YATOO

> Source : Cahier des Charges Fonctionnel v1.0 — Avril 2026 (confidentiel)

---

## L'entreprise

**Nom** — YATOO SAS (client) — Plateforme développée par **Uccello Labs**  
**Secteur** — Distribution / Intégration de solutions mobiles professionnelles → diversification SaaS affichage dynamique LED  
**Description** — Fondée en 2001, YATOO est une référence française dans la distribution de tablettes durcies (Zebra, Coworker) et l'intégration de solutions mobiles pour des clients industriels (Airbus, Dassault, Carmat, ACTIA, BCA Expertise, Éducation Nationale). YATOO souhaite se lancer sur le marché des panneaux LED d'affichage dynamique pour TPE (restaurateurs, pharmaciens, agents immobiliers). **Uccello Labs** est la société en charge de concevoir et développer le SaaS de gestion de ces panneaux, conformément au CdC v1.0.  
**Stade** — [x] MVP *(hardware à sourcer/lancer + SaaS à construire — départ à zéro)*

**Relation Uccello Labs / YATOO**
- **YATOO** : client final, commercialisera la solution (panneaux + abonnement SaaS) auprès des TPE
- **Uccello Labs** : développe la plateforme SaaS (backend Laravel + frontend React + app Flutter Android)
- Le CdC YATOO v1.0 est le document de référence technique et fonctionnel produit par Uccello Labs

**Contexte stratégique** — L'activité tablette durcie est saisonnière (cycles d'achat longs, projets ponctuels). Les panneaux LED constituent un **nouveau marché totalement distinct** de l'offre Coworker actuelle. Aucun client, aucune base installée, aucune vente réalisée à ce jour. Départ à zéro sur les deux jambes (hardware + SaaS). Le réseau de 150 partenaires actifs de YATOO est un canal tablettes/mobiles industriels — il ne couvre pas le marché TPE commerçants ciblé.

---

## Ressources disponibles

**Équipe commerciale** — Réseau de 150+ partenaires actifs ; force de vente interne existante (profil commercial B2B industriel / grands comptes)  
**Budget acquisition** — [ ] Bootstrapped  [ ] <2k€/mois  [x] 2-10k€  [ ] >10k€ *(à confirmer)*  
**Temps vente** — À préciser  
**Compétences vente** — Fort historique B2B grands comptes + PME industrielles ; à adapter pour la vente SaaS récurrent auprès de TPE commerçants

---

## Compétences + Orientations

**Compétences techniques disponibles**
- Intégration & déploiement de devices Android professionnels — 20+ ans
- Gestion de cycle de vie équipements mobiles durcie
- Stack retenue : Laravel (PHP) + React + Flutter + PostgreSQL + Redis + S3

**Type de projet**
- [x] SaaS B2B récurrent
- [x] Hybride (matériel + SaaS)

**Marché cible** (par ordre de priorité)
1. Restaurateurs / CHR (café-hôtel-restaurant) — usage quotidien, pain fort
2. Pharmacies / parapharmacies — usage hebdomadaire, délégué
3. Agences immobilières — usage pluri-hebdomadaire, PC + mobile
4. Commerçants de proximité (fleuristes, boulangers, opticiens)
5. Franchises multi-établissements — pilotage centralisé
6. Collectivités locales (mairies, gares) — hors MVP

**Ce que YATOO NE veut PAS construire**
- Surveillance / tracking comportemental des clients finaux
- Marché grand public (B2C)

**Complexité technique acceptable** — 8/10 *(architecture WebSocket + Android kiosque + IA + offline = projet technique sérieux)*

---

## Contraintes

**Géographiques** — France priorité, francophonie ensuite  
**Sectorielles** — Focus TPE/PME commerçants dans un premier temps ; franchises et collectivités en V2  
**Légales / RGPD** — Critique : données personnelles (emails, logs d'usage) stockées et traitées en UE. Consentement explicite pour analytics comportementaux. Logs d'accès conservés 12 mois minimum.  
**Matérielles** — Devices Android 9 et Android 11. App Flutter légère (RAM/stockage potentiellement limités). Mode kiosque natif (Device Owner ou Screen Pinning selon version).  
**Réseau** — Fonctionnement hybride obligatoire : online (webview live) + offline (fallback contenu local). Reconnexion automatique. WebSocket avec backoff exponentiel.  
**CMS natif panneaux** — Boîte noire à explorer : l'app Flutter pourra se substituer entièrement au CMS.

---

## Stack technique / outils

**Backend** — Laravel (PHP) — API REST + WebSocket (Laravel Reverbi)  
**Frontend Web** — React — interface responsive mobile-first  
**Application panneau** — Flutter — Android 9/11 (kiosque plein écran, webview dynamique, fallback offline)  
**Base de données** — PostgreSQL (relationnel) + Redis (WebSocket, cache, file d'attente événements)  
**Stockage fichiers** — S3-compatible — ex. Scaleway Object Storage (visuels, vidéos, assets branding)  
**IA génération image** — API Nano Banana 2 ou Pro (texte → image brandée, photo → visuel mis en forme)  
**Authentification** — Laravel Sanctum (tokens API + session web) ; OAuth possible en V2  
**Infrastructure** — Cloud souverain UE (conformité RGPD)

**Dépendances tierces critiques**
- API Nano Banana (IA image) — risque de dépendance fournisseur
- Hébergeur cloud souverain UE (Scaleway, OVHcloud…)
- Laravel Reverbi (WebSocket temps réel)

---

## Design System

**Identité visuelle**
- Nom de marque : YATOO
- Logo : *(à fournir — non inclus dans le CdC)*
- Tagline : "Gérez vos panneaux LED en 90 secondes, depuis votre téléphone."

**Palette de couleurs** *(extraite du document CdC officiel)*
- Primaire : #1E2761 (navy foncé — couleur principale marque)
- Secondaire : #2563EB (bleu vif — titres, CTA secondaires)
- Accent : #F59E0B (orange/amber — alertes, badges, CTA primaires)
- Texte principal : #1a1a1a
- Texte muted : #6b7280
- Background : #ffffff
- Background alternatif : #f9fafb

**Typographies**
- Header : Inter ou Space Grotesk
- Body : Inter
- Poids utilisés : 400, 500, 600, 700

**Motif visuel signature** — Coins arrondis 8px, shadow légère sur les cards, trait d'accent bleu sur les éléments actifs

**Ton visuel** — Tech Premium + Trust & Calm (B2B professionnel, accessible aux non-techniciens)

**Conventions de design**
- Style des boutons : arrondis (border-radius 8px)
- Style des cards : shadow légère
- Largeur max contenu : 1200px
- Espacement de base : 8px / 16px / 24px / 32px / 48px / 64px

---

## Existant commercial

**Clients actuels (gamme panneaux LED)** — **Zéro.** Les panneaux LED sont un nouveau produit sur un nouveau marché. Aucune vente réalisée, aucune base installée.  
**Canaux déjà testés (panneaux LED)** — Aucun. Départ à zéro.  
**Réseau existant** — 150+ partenaires actifs issus de l'activité tablettes durcies professionnelles (Airbus, Dassault…). Ce réseau est B2B industriel — il ne couvre pas les TPE commerçants (restaurateurs, pharmaciens, agents immobiliers) ciblés par l'offre panneaux LED.

---

## Offre en construction — Plateforme SaaS YATOO

**Modèle économique**
- Levier 1 : Vente ou location de panneaux LED Coworker Smart Panel (matériel, one-shot ou leasing)
- Levier 2 : Abonnement mensuel SaaS de gestion de contenu (récurrent, prévisible)
- Revenus annexes : frais d'installation/mise en service, templates personnalisés, commission vente/location hardware

**Plans tarifaires envisagés** *(à valider avec 5-10 clients pilotes — essai 14 jours sans CB recommandé)*

| Plan | Panneaux | Fonctionnalités |
|------|----------|-----------------|
| Starter | 1 | Fonctionnalités de base |
| Pro | 1-5 | IA incluse, templates métiers, historique |
| Business | 6-20 | Multi-utilisateurs, analytics, priorité support |
| Enterprise | 20+ | Multi-sites, SLA garanti, intégrations tierces |

---

## UX/UI — Décisions de conception

### Flux de création de contenu (style Typeform — une question à la fois)

```
Étape 1 — Type de contenu
  ├── Image
  ├── Carousel d'images
  └── Vidéo

Étape 2 — Source (si Image ou Carousel)
  ├── Images existantes (upload)
  └── Générer par IA

Étape 3 — Template (si IA)
  └── Choix parmi la bibliothèque de templates métiers
      (ex : Plat du jour, Promotion, Bien immobilier, Produit pharmacie…)

Étape 4 — Formulaire adaptatif (champs selon le template choisi)
  ex. template "Plat du jour" → Titre, Description, Tarif, Photo du plat
  ex. template "Promotion"   → Titre, % de réduction, Date de fin

Résultat
  └── Image(s) générées ou configurées → diffusion directe sur le(s) panneau(x)
```

**Principes UX**
- Une seule question à la fois (pas de formulaire long)
- Mobile-first : conçu pour être rempli en < 90s sur smartphone
- Formulaire adaptatif : les champs varient selon le template sélectionné
- Prévisualisation avant diffusion (mentionnée dans le CdC)
- Diffusion directe après validation — pas d'étape intermédiaire

**Règles métier arrêtées**
- Vidéo : upload direct sur S3, pas de génération IA. Pas de limite de taille ni de durée pour le MVP.
- Carousel : durée d'affichage configurable par image. Une durée par défaut est appliquée (valeur à définir — ex. 5s ou 10s). Boucle automatique.

---

## KPIs de succès (MVP)

| Indicateur | Cible |
|------------|-------|
| Temps de mise à jour | < 90 secondes (contenu → diffusion) |
| Taux d'adoption hebdomadaire | > 70% des utilisateurs actifs à M1 |
| Taux de churn SaaS (M3) | < 10% |
| Délai installation panneau | < 5 min sans assistance technique |
| Génération IA | < 30 secondes par visuel |
| Disponibilité plateforme | > 99.5% uptime |

---

## Personas (définis dans le CdC)

**Persona 1 — Le Restaurateur** *(acheteur + utilisateur principal)*
- 35-55 ans, gérant, peu technique, usage quotidien (le matin avant ouverture), smartphone uniquement
- Besoin : plat du jour, promotions, horaires modifiés
- Critère de succès : "En 3 clics, mon panneau est à jour."
- Pain actuel : 15 min sur le CMS natif pour un changement de texte

**Persona 2 — Le Pharmacien** *(acheteur = titulaire / utilisateur = préparateur)*
- Titulaire ou préparateur délégué, usage hebdomadaire, tablette/PC (mobile occasionnel)
- Besoin : promotions saisonnières, produits du moment, messages santé
- Critère de succès : "Mes visuels sont professionnels sans faire appel à un graphiste."
- Pain actuel : pas de templates adaptés au secteur pharmaceutique

**Persona 3 — L'Agent Immobilier** *(acheteur = responsable agence / utilisateur = assistant)*
- 28-45 ans, responsable agence ou assistant(e), pluri-hebdomadaire, PC bureau + mobile
- Besoin : biens en vitrine, nouveautés, prix
- Critère de succès : "Mon panneau se met à jour en même temps que mon logiciel métier."
- Pain actuel : contenu statique pendant des semaines faute de temps

---

## Ambition

**Objectif MVP** — Livrable, testable terrain, générateur de revenus. Tout "nice to have" classé MLP ou V2.  
**MLP (V1.1+)** — Templates intelligents (contextuels), programmation de diffusions, playlists automatiques, analytics, multi-utilisateurs avec rôles, multi-établissements, intégrations tierces (Lightspeed, Kounta, logiciels pharma), app mobile dédiée (PWA ou native iOS/Android).  
**Objectif 12 mois** — À préciser (nombre de clients pilotes, ARR cible)  
**Objectif 3 ans** — Devenir la référence SaaS de gestion de panneaux LED en France/francophonie ; avantage concurrentiel durable indépendant du fabricant matériel

---

> Fichier alimenté depuis le CdC YATOO v1.0 (Avril 2026).  
> À compléter : logo, pricing chiffré (€/mois par plan), budget acquisition, objectifs ARR 12 mois.
