# PROJECT_CONTEXT.md — Mintizy / Portail revendeurs ERP

> Projet ciblé : **packager et distribuer le portail client Mintizy comme produit autonome auprès d'intégrateurs ERP français orientés SAV/maintenance**.
> Le revendeur intègre le portail à son ERP via API (intégration à sa charge) et le commercialise à ses clients finaux (entreprises de SAV/maintenance), qui l'utilisent pour leurs propres clients (les destinataires des interventions).

---

## L'entreprise

**Nom** — UCCELLO LABS
**Secteur** — Édition SaaS B2B — gestion de maintenance
**Description** — UCCELLO LABS édite **Mintizy**, plateforme SaaS de gestion de maintenance composée de 3 briques connectées : appli mobile technicien (offline), ERP web responsable, portail client. 1200+ utilisateurs revendiqués. Siège : Montpellier. Hébergement France, RGPD. Site : mintizy.com.
**Stade** — [ ] Idée  [ ] MVP  [X] **Traction**  [ ] Croissance établie
*(Traction : produit en marché, premier contrat de distribution signé avec Groupe OCI, 4 clients finaux facturés via OCI + ~15 en pipeline)*

---

## Ressources disponibles

**Équipe commerciale** — Solo fondateur (Jonathan) aujourd'hui. COO Jonadabe pourra prendre le relais à terme.
**Budget acquisition** — [X] Bootstrapped  [ ] <2k€/mois  [ ] 2-10k€  [ ] >10k€  *(à confirmer)*
**Temps vente** — 1,5 jour/semaine
**Compétences vente** — Technique fort (édition produit Mintizy en prod). Vente B2B partenaires : à structurer (premier deal OCI signé sans process formalisé, pas de réseau intégrateurs ERP préexistant).

---

## Compétences + Orientations

**Compétences techniques fortes**
- Édition SaaS B2B maintenance — Mintizy en production (3 ans+)
- API REST exposée et documentée pour intégrateurs tiers
- Hébergement cloud, RGPD, sécurité (chiffrement, sauvegardes, contrôle accès)
- Intégrations : Yousign (signature), Stripe (paiement)

**Type de projet préféré**
[X] SaaS B2B récurrent
[ ] Service / prestation haut de gamme
[ ] Produit digital one-shot
[ ] Hybride

**Marché cible préféré** (par ordre de priorité)
1. **Intégrateurs ERP français** ayant un portefeuille de clients SAV/maintenance (Cegid XRP Flex, Sage X3, Divalto, Dynamics 365 BC, Odoo Enterprise, SAP B1, Akuiteo… à prioriser en `/offer-market-research`)
2. Groupements professionnels du SAV (type Groupe Gasel) — accessibles via les revendeurs
3. (Hors scope) Vente directe aux entreprises de SAV — déjà couverte par l'offre Mintizy SaaS standard

**Ce que vous REFUSEZ de construire** — Aucune red line déclarée.

**Complexité technique acceptable** — **3/10**
*Pas de R&D produit lourde sur ce projet : le portail existe, le revendeur fait son propre connecteur ERP. Les seuls dev acceptables sont : amélioration de la doc API, options white-label, petits ajustements UX réclamés par plusieurs revendeurs.*

---

## Contraintes

**Géographiques** — France (alignement avec hébergement France et RGPD).
**Sectorielles** — Cibler les ERP/intégrateurs avec exposition SAV/maintenance.
**Légales / RGPD** — Critique (données interventions, signatures, données personnelles techniciens et clients finaux).
**Ce que vous ne voulez PAS faire** — Pas de connecteur ERP custom dev par UCCELLO (chaque revendeur fait le sien). Pas de R&D produit majeure pour ce projet.

---

## Stack technique / outils

**Outils utilisés en interne** — Mintizy lui-même (plateforme + appli mobile + portail), API REST, infra cloud France.
**Intégrations possibles avec l'offre** — Le portail consomme une API REST documentée. Le revendeur construit la passerelle ERP→portail (réplication des données ; les champs absents restent vides côté portail). Modèle confirmé sur Cegid XRP Flex via OCI.
**Dépendances tierces critiques** — Hébergeur cloud France, Stripe, Yousign.

---

## Design System

**Identité visuelle**
- Nom de marque : **Mintizy** (par défaut). White-label possible si pertinent commercialement.
- Logo : à pointer (logo Mintizy depuis mintizy.com)
- Tagline actuelle : *"La tour de contrôle de votre maintenance"*

**Palette de couleurs (HEX)** — extraite de mintizy.com
- Primaire : `#2FB293` (sarcelle/turquoise — `hsl(166 58% 44%)`)
- Primaire foncé : `#228470` (`hsl(166 58% 35%)`)
- Accent : `#00F0E0` (cyan vif — `hsl(176 100% 47%)`)
- Texte principal : `#1F2937` (`hsl(215 28% 17%)`)
- Texte muted : `#65758B` (`hsl(215 16% 47%)`)
- Background : `#FFFFFF`
- Background alternatif : `#F8FAFC`
- Border : `#E5E7EB`
- Succès : `#16A34A`

**Typographies**
- Header : Inter
- Body : Inter
- Poids utilisés : 400, 500, 600, 700

**Motif visuel signature**
- Gradients sarcelle (`linear-gradient(135deg, #2FB293, #228470)`)
- Cards à coins arrondis 12px (`--radius: 0.75rem`)
- Shadows douces (sm/md/lg/xl)
- Glow turquoise sur éléments interactifs

**Ton visuel** — Tech moderne SaaS, clair et accessible (pas executive lourd, pas brutaliste). Mode sombre disponible.

**Conventions de design**
- Boutons : arrondis (radius 0.75rem), filled primary + outline secondary
- Cards : shadow douce, fond blanc, border subtile
- Largeur max contenu : ~1200px
- Espacement de base : 8/16/24/32/48/64px

---

## Existant commercial

**Clients actuels (canal revendeur)** — 4 clients finaux facturés via Groupe OCI + ~15 en pipeline (perspectives à 3-6 mois).
**Canaux déjà testés** — Un seul : signature contrat de distribution avec Groupe OCI (intégrateur Cegid XRP Flex). OCI bundle Flex + Praxedo + portail Mintizy à ses clients ; OCI signe aussi des groupements professionnels (ex. Groupe Gasel = effet de levier multi-membres).
**Réseau existant** — Aucun contact établi chez d'autres intégrateurs ERP. **Cold outreach pur** à structurer.

---

## Offres existantes (à ne pas confondre avec ce projet)

> Mintizy a déjà 2 offres en marché. Ce projet en crée une **troisième**, ciblant un canal et un segment distincts.

**Offre 1 — Mintizy SaaS direct** (existante, non couverte par ce projet)
- 3 packs : Starter 392€ / Business 792€ / Scale 1520€ HT/mois (promo -20% en cours)
- Vente directe aux entreprises de SAV/maintenance

**Offre 2 — Programme partenaires Mintizy direct** (existante, non couverte par ce projet)
- Apporteurs d'affaires / revendeurs vendant la plateforme **complète** Mintizy
- Commissions récurrentes 15-20-25% selon pack

**Offre 3 — Portail Mintizy revendu via intégrateurs ERP** (objet de ce projet)
- Le revendeur intègre uniquement le **portail client** à son propre ERP
- Tarification UCCELLO au palier (HT/mois par client final) :
  - 1-10 utilisateurs finaux : 120€
  - 11-50 : 180€
  - 51-100 : 240€
  - 100+ : 300€
- Le revendeur applique sa marge (≈40% chez OCI)
- Support N1 = revendeur (accompagnement utilisation, anomalies fonctionnelles)
- Support N2 = UCCELLO (bugs produit Mintizy)
- Pas d'exclusivité OCI — UCCELLO peut signer d'autres intégrateurs Cegid XRP Flex et tous autres ERP
- Marque par défaut : Mintizy. White-label envisageable si pertinent commercialement.

---

## Ambition

**Objectif 12 mois** — 5–7 revendeurs intégrateurs ERP signés (incluant OCI), 25–50 clients finaux actifs, **60–120k€ ARR additionnel** sur ce canal.
*(Hypothèses : 1 revendeur signé = 6-9 mois de ramp-up avant premier client facturé ; OCI sert de proof point empirique avec 4 facturés + 15 pipeline.)*

**Objectif 3 ans** — 15–20 revendeurs actifs, 200–300 clients finaux, **500k€–1M€ ARR** sur ce canal. Sortir de l'exécution solo via Jonadabe (COO) puis recrutement commercial dédié.

---

## Points en suspens à arbitrer dans le pipeline

- [ ] Liste priorisée des ERP cibles à attaquer en année 1 → `/offer-market-research`
- [ ] Volumétrie réelle d'intégrateurs ERP français adressables → `/offer-market-research`
- [ ] Persona décideur côté intégrateur ERP (qui décide d'ajouter une brique au bundle ?) → `/offer-persona`
- [ ] Concurrents directs sur le créneau "portail client SAV pour intégrateurs ERP" → `/offer-competitive-intel`
- [ ] Décision marque vs white-label (par défaut Mintizy ; basculer si demande forte) → `/offer-final`
- [ ] Structure tarifaire : conserver le grid OCI ou refondre ? → `/offer-pricing`

---

> Lance `/offer-cadrage` pour cadrer l'idée, challenger la viabilité et obtenir un verdict GO/NO-GO/PIVOT.
