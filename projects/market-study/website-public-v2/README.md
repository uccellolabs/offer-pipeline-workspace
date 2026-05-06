# Offer Pipeline · Site public

Site vitrine commercial de la gamme Offer Pipeline (Uccello Labs).
Stack : Astro 5 + CSS variables (no framework). Mobile-first, indexable.

## Pages

- `/` — Page de gamme (parapluie 3 portes)
- `/offer-clarity/` — Done For You (freelance)
- `/pipeline-solo/` — DIY install machine consultant senior
- `/pipeline-studio/` — DIY setup cabinet 5-30 consultants
- `/pour-qui/` — 3 personas + fits/anti-fits
- `/contact/` — Calendrier + email + LinkedIn

## Lancer en local

```bash
npm install
npm run dev
```

Ouvre http://localhost:4321

## Build production

```bash
npm run build
npm run preview
```

Output dans `dist/`.

## Design system

Charte issue de PROJECT_CONTEXT.md (Trust & Calm) :
- Primaire : `#1D4ED8` (blue-700)
- Secondaire / accent : `#0EA5E9` (sky-500)
- Display : Space Grotesk
- Body : Inter
- Boutons : 4px radius
- Max width : 1200 px

Tous les tokens sont dans `src/styles/global.css` (`:root`).

## Déploiement Forge (recommandé)

Cohérent avec v1 (sardoj/offer-clarity-market-study) :
- Repo GitHub dédié
- Forge site Astro (build : `npm run build`, public : `dist/`)
- Sous-domaine `offer-pipeline.uccello.io` (à provisionner)
- SSL Let's Encrypt
- Quick deploy : git push → auto-build

## Hors scope (à ajouter si besoin)

- Sitemap auto (intégration `@astrojs/sitemap`)
- Image OG par page (actuellement défaut `/og-default.png` non fourni)
- Calendrier embed Cal.com / Calendly
- Formulaire de contact actif (actuellement liens mailto + Cal.com)
