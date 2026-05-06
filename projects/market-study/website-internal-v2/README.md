# Offer Pipeline · Site interne (étude v2)

Étude interne complète du projet market-study v2 (gamme 3 portes).
Stack : Astro 5 + CSS variables. Mobile-first, **noindex**, protection client-side
par mot de passe.

## Pages

- `/` — Accueil + tracker pipeline + cartes de navigation
- `/decouverte/` — IDEA_BRIEF v2 (3 archétypes scorés + sources)
- `/offre/` — OFFER_FINAL v2 (gamme 3 portes + plan go-to-market)
- `/persona/` — PERSONA v2 (Julien + Marc + Hélène)
- `/marche/` — MARKET RESEARCH v2 (TAM/SAM/SOM par archétype)
- `/concurrence/` — COMPETITIVE_BRIEF v2 (4 battlecards)
- `/pricing/` — PRICING_BRIEF v2 (3 modèles, no SaaS)
- `/viabilite/` — Score viabilité globale + conditions
- `/contact/` — Coordonnées projet
- `/login/` — Page de connexion (gate)

## Lancer en local

```bash
npm install
npm run dev
```

Ouvre http://localhost:4321 → redirigé vers /login/.

## Build production

```bash
npm run build
npm run preview
```

Output dans `dist/`.

## Configurer le mot de passe

La protection est client-side (security through obscurity, pas de sécurité robuste).
Pour changer le mot de passe :

1. Choisir un mot de passe (ex : `offerpipeline2026`)
2. Calculer son SHA-256 :
   ```bash
   echo -n "offerpipeline2026" | shasum -a 256
   ```
3. Remplacer la valeur de `EXPECTED_HASH` dans `public/auth.js`

**Mot de passe par défaut :** non valide (placeholder).
Tu DOIS calculer un hash réel avant de déployer.

Session valide 12 heures après connexion (sessionStorage).

## Design system

Mêmes tokens que le site public (Trust & Calm) — Space Grotesk + Inter,
blue + sky. Composants additionnels : battlecards dépliables, scores,
gauge circulaire, journal intime stylisé, pricing cards denses, pipeline tracker.

## Pour une protection robuste

Le gate client-side est une **protection légère**. Pour une vraie auth :
- Cloudflare Access (gratuit jusqu'à 50 users)
- Netlify Identity
- Vercel Password Protection (sur Pro)
- Forge HTTP basic auth (le plus simple si déjà sur Forge)
