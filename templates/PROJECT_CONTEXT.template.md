# PROJECT_CONTEXT.md — Contexte du projet

> Remplis ce fichier AVANT de lancer les agents du pipeline.
> Sans contexte précis, les agents travaillent dans l'abstrait.

---

## L'entreprise

**Nom** — [ex : Uccello Labs]
**Secteur** — [ex : Édition SaaS B2B]
**Description (2 phrases)** — [ce que fait l'entreprise, pour qui, depuis quand]
**Stade** — [ ] Idée  [ ] MVP  [ ] Traction  [ ] Croissance établie

---

## Ressources disponibles

**Équipe commerciale** — [ex : Solo fondateur / 1 commercial / équipe de 3]
**Budget acquisition** — [ ] Bootstrapped  [ ] <2k€/mois  [ ] 2-10k€  [ ] >10k€
**Temps vente** — [ex : 2 j/semaine / temps plein / externalisé]
**Compétences vente** — [ex : Technique fort, vente faible / Ex-commercial]

---

## Compétences + Orientations

> Utilisé par `/idea-finder` pour filtrer les opportunités business.

**Compétences techniques fortes** (ordre décroissant)
- [ex : Backend Laravel — 21 ans d'expérience]
- [ex : Architecture SaaS B2B — 10 ans]
- [ex : IA locale via Ollama / Qwen3]

**Type de projet préféré**
[ ] SaaS B2B récurrent
[ ] Service / prestation haut de gamme
[ ] Produit digital one-shot
[ ] Hybride

**Marché cible préféré** (par ordre de priorité)
1. [ex : PME françaises 5-50 salariés]
2. [ex : TPE / indépendants]
3. [ex : Cabinets conseil / experts-comptables]

**Ce que vous REFUSEZ de construire** (même si rentable)
- [ex : Surveillance employés]
- [ex : Crypto / gambling]
- [ex : SaaS avec obligations RGPD santé]

**Complexité technique acceptable** — [X/10]
*(1 = ultra-simple, livrer vite / 10 = R&D sur 2 ans)*

---

## Contraintes

**Géographiques** — [France / Francophonie / International]
**Sectorielles** — [Focus PME / Éviter public / Exclure retail]
**Légales / RGPD** — [RGPD critique / Données santé / Aucune]
**Ce que vous ne voulez PAS faire** — [Pas de vente directe / Pas de freemium]

---

## Stack technique / outils

**Outils utilisés en interne** — [CRM, ERP, analytics, code...]
**Intégrations possibles avec l'offre** — [APIs, connecteurs disponibles]
**Dépendances tierces critiques** — [ex : Scaleway pour IA, Stripe pour paiement]

---

## Design System

> Utilisé par `/pitch-deck` (HTML) et `/study-website`.
> Si absent, les agents proposent 3 thèmes prédéfinis.

**Identité visuelle**
- Nom de marque : [ex : Axell]
- Logo : [chemin vers logo.svg ou logo.png — relatif au projet]
- Tagline : [ex : "L'IA commerciale pour PME"]

**Palette de couleurs (HEX)**
- Primaire : [#1E2761]
- Secondaire : [#CADCFC]
- Accent : [#FFFFFF]
- Texte principal : [#1a1a1a]
- Texte muted : [#6b7280]
- Background : [#ffffff]
- Background alternatif : [#f9fafb]

**Typographies (Google Fonts recommandées)**
- Header : [ex : Inter, Space Grotesk, DM Serif Display, Georgia]
- Body : [ex : Inter, DM Sans, Source Sans Pro]
- Poids utilisés : [ex : 400, 500, 600, 700]

**Motif visuel signature**
[ex : icônes en cercles colorés / coins arrondis 8px / trait d'accent latéral 4px]

**Ton visuel**
[Executive / Bold Modern / Trust & Calm / Editorial / Tech Premium / Custom]

**Conventions de design**
- Style des boutons : [arrondis / carrés / outline]
- Style des cards : [shadow / border / flat]
- Largeur max contenu : [ex : 1200px]
- Espacement de base : [ex : 8px / 16px / 24px / 32px / 48px / 64px]

---

## Existant commercial

**Clients actuels** — [Nombre, profil, secteur]
**Canaux déjà testés** — [Ce qui a été essayé, résultats]
**Réseau existant** — [Contacts LinkedIn, partenaires potentiels]

---

## Offres existantes

> Remplir si tu as déjà une offre en production sur ce projet.

**Offre principale**
- Nom — [ex : Uccello Hub]
- Description (2 phrases) — [...]
- Prix actuel — [ex : 299€/mois + 500€ setup]
- Clients actuels — [nombre, profil]
- Ce qui fonctionne — [retours positifs]
- Ce qui frotte — [objections fréquentes, friction]

---

## Ambition

**Objectif 12 mois** — [ex : 10 revendeurs / 50 clients / 100k€ ARR]
**Objectif 3 ans** — [ex : Sortir de l'exécution solo / Équipe 5 / Leader FR]

---

> Une fois rempli, lance `/idea-finder` ou `/offer-cadrage` pour démarrer.