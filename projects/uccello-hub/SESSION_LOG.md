# SESSION_LOG.md — Journal du pipeline

> Créé automatiquement par le premier agent lancé sur le projet.
> Mis à jour à chaque étape.
> Évite aux agents de relire tous les fichiers en détail.

---

## Statut du pipeline

```
/idea-finder       : ⬜ Non lancé
/offer-cadrage     : ✅ 2026-04-25
/persona           : ✅ 2026-04-25
/market-research   : ✅ 2026-04-25
/competitive-intel : ✅ 2026-04-25
/pricing           : ✅ 2026-04-25
/offer-final       : ✅ 2026-04-25
/pitch-deck        : ✅ 2026-04-25
/study-website     : ✅ 2026-04-25
/offer-vsl-script  : ✅ 2026-05-05
```

---

## Décisions clés

*(Format : [DATE] [AGENT] — [décision] — [output])*

2026-04-25 /offer-cadrage — Verdict GO — Hub IA souverain, modèle indirect, douleur quantifiable, pricing à construire → OFFER_BRIEF.md v1.0 créé
2026-04-25 /persona — Acheteur : Marc (consultant indépendant, 9/10 prospect.) | Utilisateur : Claire (dirigeante agence marketing B2B) → PERSONA_ACHETEUR.md + PERSONA_UTILISATEUR.md créés
2026-04-25 /market-research — Canal B (revendeurs) | Score Marc 18/20 | Viabilité 3 : ✅ Budget OK, ⚠️ Maturité Conscient→Éduqué, Cycle 2-4 sem → MARKET_RESEARCH.md créé
2026-04-25 /pricing — Modèle : Hybride D | Revendeur 99€/mois + par tier utilisateurs | Tiers Marc: 99/174/274/399€/mois | Marge Marc 46-48% | On-premise 1 000-2 000€ → PRICING_BRIEF.md v2.0 créé
2026-04-25 /offer-final — Score viabilité : ✅ VIABLE | Format : One-pager partenaire revendeur | Destinataire : Marc | ⚠️ 2 actions avant signature : contrat revendeur + support démo client final → OFFER_FINAL.md v1.0 créé
2026-04-25 /pitch-deck — Destinataire : Les deux | Contexte : Démo live | Durée : 15 min | Format : HTML → pitch-deck-client/ + pitch-deck-revendeur/ créés (index.html + style.css + script.js)

---

## Versions des fichiers

| Fichier | Version actuelle | Date | Changement |
|---------|-----------------|------|------------|
| IDEA_BRIEF.md | — | — | — |
| OFFER_BRIEF.md | — | — | — |
| PERSONA_ACHETEUR.md | — | — | — |
| PERSONA_UTILISATEUR.md | — | — | — |
| COMPETITIVE_BRIEF.md | — | — | — |
| PRICING_BRIEF.md | — | — | — |
| OFFER_FINAL.md | v1.0 | 2026-04-25 | Score viabilité global + one-pager partenaire revendeur |
| PITCH_DECK.pptx | — | — | — |

---

## Apprentissages terrain

> Rempli par l'utilisateur après tests, interviews ou retours prospects.
> Format : `[DATE] — [source] — [apprentissage] — [agent impacté]`
>
> Exemple : `2026-05-12 — Interview ESN X — Budget max 500€/mois, pas 2000€ — /pricing à revoir`

2026-05-04 — Cold calls vague 1 (3 appels) — Taux RDV : 2/3 (67%) — /offer-cold-call validé sur petit échantillon
2026-05-04 — RDV obtenu : Adem Boukhanoufa (Adem IA Automatisation, Lyon, Sociaty.io = formation/conseil IA) — score 6 CSV v3
2026-05-04 — RDV obtenu : Olivier Malamou (IA Automatisation, Nantes, Loup Digital = agence formation IA & automatisation) — score 6 CSV v3
2026-05-04 — Disqualifié : Implementation Consulting Automatisation (Adil El Marradi, Roubaix) — éditeur logiciel propriétaire (AmbiSmart.io) avec solutions IA internes — pas un revendeur potentiel — /offer-prospection-list à durcir
2026-05-04 — Apprentissage filtre — NAF 62.02A inclut consultants ET éditeurs ; discriminant = SaaS propriétaire (login/pricing/app) vs formation/conseil/agence ; les 2 RDV ont aussi un site "produit" mais c'est de la formation/agence (compatible persona Marc) — /offer-prospection-list : ajouter heuristique "détection SaaS propriétaire" (signaux : pricing page, login, free trial, mots-clés "platform/app/launch") plutôt que présence d'un site marketing

---

2026-04-25 /study-website — Deux sites générés complets | website-public (5 pages, hub.uccello.io) + website-internal (8 pages, usage local) | HTML/CSS/JS pur, Lucide icons, Bricolage Grotesque + DM Sans → website-public/ + website-internal/ créés

2026-04-26 /prospection-strategy — Canal : Revendeurs | Persona : Marc | Mode : A (SIRENE + LinkedIn manuel) | Volume : 20-50 prospects pilote
→ PROSPECTION_PLAYBOOK.md créé | 22 prospects Priorité A identifiés via Annuaire Entreprises data.gouv.fr (NAF 62.02A/62.01Z, solopreneurs, grandes métropoles) | Séquence LinkedIn 3 touches + Email 5 touches + Omnichannel J-3→J+14
/prospection-strategy : ✅ 2026-04-26

2026-04-26 /prospection-list — Segment : Consultants IT solopreneurs | Volume : 50 | Niveau : 1 (SIRENE + site web)
→ prospection.html créée (9 sections : config, top prospects, séquences LinkedIn+Email, omnichannel, objections, KPIs) | Nav ajoutée dans 8 pages | Pipeline steps mis à jour | index.html + contact.html mis à jour
/study-website update : ✅ 2026-04-26
→ PROSPECTS_2026-04-26_consultants-IT-solopreneurs.csv créé | 50 lignes | Score moyen 4.5/6 | 5 profils idéaux (score 6) | 16 très bons (score 5) | 47/50 NAF 62.02A/62.01Z | 42/50 grandes métropoles | 46/50 dirigeants identifiés
Complétude : 2% sites web (1/50 — enrichissement manuel requis via Hunter.io) | 92% dirigeants identifiés (via SIRENE)
/prospection-list : ✅ 2026-04-26 (vague 1)

2026-04-26 /study-website update v2 — prospection.html mis à jour avec couche DISC complète
→ Grille DISC 30 sec (tableau signaux) | 6 biais cognitifs (cartes) | Matrice DISC × Biais
→ Onglets DISC (D/I/S/C) sur les 3 touches LinkedIn + 5 touches Email (= 32 templates)
→ Timeline omnichannel avec colonne adaptation DISC | Objections DISC en tableau croisé
→ KPIs avec colonne "Tracking DISC" | Répartition DISC 50 prospects (barres visuelles)
→ Stats v2 (43 DISC estimés) | Référence CSV v2 | Footer v2.0
/study-website update v2 : ✅ 2026-04-26

2026-04-26 /prospection-list v2 — Enrichissement DISC sur 50 prospects existants
→ 6 colonnes ajoutées : LinkedIn_décideur, Email_pattern_1/2, Profil_DISC_estime, Signaux_DISC, Confiance_DISC
→ 1 DISC Moyenne (Marwan Toufiq — Codeur.com confirmé D-C) | 1 DISC Faible sourcé (Adil El Marradi — Viadeo C-S)
→ 3 INDÉTERMINABLE score 6 (Adem Boukhanoufa, Olivier Malamou, Philippe Vaitilingam — LinkedIn à chercher manuellement)
→ 4 INDÉTERMINABLE sans dirigeant (Colors Process, SARL Workflow, Workflow Groupware, Conception Integration PACA)
→ 42 DISC inférés contextuellement (Faible) depuis nom société + forme juridique + ancienneté + localisation
→ PROSPECTS_2026-04-26_consultants-IT-solopreneurs_v2.csv créé (50 lignes, v1 conservée)
Répartition DISC estimée : D=8 | D-C=3 | D-I=4 | C=11 | C-S=9 | C-D=2 | S=3 | S-C=3 | S-I=2 | I=4 | I-S=1 | INDÉT.=7 (dont 4 sans dirigeant)
/prospection-list v2 : ✅ 2026-04-26

2026-04-26 /prospection-strategy v2 — Ajout couche DISC complète + 6 biais cognitifs
→ Grille détection DISC 30 sec | Matrice DISC × Biais | 4 variantes par template (D/I/S/C)
→ Touches LinkedIn 1-2-3 modulées DISC | Emails Touch 1-5 × 4 profils | Objections DISC-adaptées
→ PROSPECTION_PLAYBOOK_v2.md créé (v1 conservée)
/prospection-strategy v2 : ✅ 2026-04-26

2026-04-26 /pricing update — Validation marché on-premise + correction grille MSP
→ Étude marché on-premise réelle : OnPremiseAgent ($499/$1 499/mois), n8n Business self-hosted ($667/mois), Chatwoot Enterprise ($99/agent/mois), AirgapAI ($697/user one-time)
→ Correction erreur précédente : comparaison GoHighLevel/Mewayz était du cloud SaaS white-label, pas du on-premise — invalide pour le scénario Marc MSP
→ Grille MSP validée et conforme au marché : 499€ (≤20 users) / 899€ (21–50) / 1 499€ (51–100) / Custom (100+) + setup 2 000–3 000€
→ Distinction clarifiée dans PRICING_BRIEF.md : On-premise Marc MSP (flat capacitaire, 1 instance) vs On-premise client final (par client, 1 000–2 000€/client)
→ Simulation marge Marc MSP (Growth 8 clients) : 61–63% marge brute vs 46% en SaaS — meilleure marge Marc mais -35% revenus Jonathan
/pricing update : ✅ 2026-04-26

2026-05-03 /offer-prospection-list — Coordonnées GMB + siège INSEE | Out : PROSPECTS_2026-04-26_consultants-IT-solopreneurs_v3.csv (49 lignes)
→ Adresses + GPS : recherche-entreprises.api.gouv.fr | Téléphone + avis + URL Maps : Google Places API (New) via `skills/offer-prospection-list/enrich_prospects_places.py` (dépôt Offer-Pipeline ; install `~/.claude/skills/offer-prospection-list/`) — clé MCP ou env
→ Complétude indicative : 48/49 fiches avec détail lieu | 36/49 téléphone | 35/49 site GMB | colonne Confiance_match_GMB pour trier les domiciliations / faux positifs
/offer-prospection-list : ✅ 2026-05-03 (enrichissement coordonnées v3)

2026-05-03 — Nettoyage projet local — `_tmp_ae.json` et `_prospects_siege_gouv.json` supprimés (cache / siège INSEE régénérable) | Patterns ajoutés au `.gitignore` racine | CSV v1 / v2 / v3 conservés (50 vs 49 lignes : v1 pas fusionnable à l’aveugle avec v2)
2026-05-03 — Copie locale `scripts/enrich_prospects_places.py` supprimée — script maintenu dans le dépôt du skill `offer-prospection-list` (chemin SKILL.md § batch) ; entrée du 2026-05-03 ci-dessus mise à jour

2026-05-03 /offer-cold-call — Cible : Consultant transformation digitale indépendant (Marc) | DISC : 4 variantes | Contexte : Froid | Volume : 5–20 calls/sem
→ COLD_CALL_SCRIPT.md créé | Script principal C (dominant dans CSV ~44%) + variantes D/I/S | Portier + boîte vocale + 9 objections DISC | Métriques calibrées
/offer-cold-call : ✅ 2026-05-03

2026-05-03 /offer-study-website (itération) — Ajout page /cold-call au site interne
→ cold-call.html créé (5 blocs verbatim, 4 onglets DISC, scripts portier + VM, tableau 9 objections, 6 métriques)
→ Lien "Cold Call" ajouté dans le nav de 10 pages HTML + carte dans nav-grid index.html + pipeline step
/offer-study-website update cold-call : ✅ 2026-05-03

2026-05-04 /offer-study-website — Site public PARTENAIRES REVENDEURS (mode B custom)
→ Dossier projects/uccello-hub/website-revendeurs/ — distinct de website-public/ (clients finaux Claire) et website-internal/
→ 5 pages : index, programme, produit, pour-qui, contact
→ Audience : Marc (consultant indépendant, persona acheteur du programme partenaire)
→ Contrainte : aucun tarif affiché — toutes mentions tarifaires renvoyées au RDV de qualification
→ CTA unique : https://calendar.app.google/SuqHzLZ9sNQvdGtP6 (4 occurrences principales + nav, lien Google Calendar)
→ Design system : harmonisé avec pitch-deck-revendeur (Bricolage Grotesque + DM Sans, #1D4ED8 + #0EA5E9, radius 4px, Trust & Calm)
→ Mobile-first vérifié 320px / 1280px (no horizontal scroll, hamburger fonctionnel, tableau scrollable)
/offer-study-website public revendeurs : ✅ 2026-05-04

2026-05-05 /offer-vsl-script — Cible : Marc (revendeur partenaire) | Format : Mixte (face cam + B-roll/slides) | Durée : 10 min standard + cutdown 90 sec | Trafic : Tiède + Chaud (Product-aware → Most-aware) | CTA : RDV qualifié 30 min calendar.app.google/SuqHzLZ9sNQvdGtP6
→ VSL_SCRIPT.md créé (12 actes long + 6 actes cutdown 90 sec + brief interne + 7 hooks)
→ Big Promise retenue : "Ajoutez 1 700€ de MRR à votre cabinet sans embaucher ni développer" (12 mots, sourcée simulation 10 clients Team)
→ Hook longue : #2 (promesse chiffrée + spécificité, optimal DISC C) | Hook cutdown : #5 (disqualification/réactance)
→ One Big Domino : "Pour productiser, il faut développer ou recruter" → faux
→ Mécanisme : Le Hub Souverain (3 piliers : Centralisation / Interconnexion / IA contextuelle souveraine)
→ Origin story : déclic vidéo cheffe d'entreprise B2B (IA tuant SaaS classiques) + 14 ans construction SaaS B2B
→ Risk reversal : 1er mois offert + sandbox + 0€ entrée + garantie 90 jours premier client (désinscription sans frais sinon)
→ Acte 10 (urgence/rareté) : SUPPRIMÉ (pas de Reason Why crédible, conformément Hormozi). Conservé : coût inaction + pivot temporel marché
→ Stack ratio : ~5,9× (valeur ancrée 6 400€ / coût première année ~1 089€)
→ Zones d'alerte assumées : 0 client payant à ce jour (cas Claire utilisé en projection ROI sourcée, 2 RDV cold call vague 1 utilisés en signal marché récent, pas en cas client)
/offer-vsl-script : ✅ 2026-05-05

2026-05-05 /offer-study-website (itération) — Ajout page /vsl au site interne (website-internal/)
→ vsl.html créé : brief interne (12 fiches), mécanisme 3 piliers, 3 niveaux de douleur, tableau 7 hooks, 12 actes verbatim avec annotations scéniques (visuel/ton/débit/pauses) + open loops + bucket brigades + yes ladders + future pacing, cutdown 90 sec (6 actes), notes de production, checklist tournage interactive (localStorage), tableau diagnostic post-publication
→ Mode lecture téléprompteur (toggle) qui masque les annotations et agrandit le verbatim
→ Nav mise à jour sur 10 pages existantes + nav-grid + pipeline-steps + footer index.html
→ Design system harmonisé avec cold-call.html (Bricolage Grotesque + DM Sans, palette #1D4ED8, classes existantes)
/offer-study-website update VSL : ✅ 2026-05-05

2026-05-05 /ui-ux-pro-max — Refonte design site interne (website-internal/) pour matcher l'offre revendeur (Trust & Authority, institutionnel)
→ Design system généré : pattern Enterprise Gateway, style Trust & Authority. Palette existante #1D4ED8 + #0EA5E9 et fonts Bricolage Grotesque + DM Sans conservées (cohérence cross-supports pitch decks + autres sites)
→ main.css étendu (calque additif, ~280 lignes) : layer Trust & Authority (variables slate-deep #0F172A, ease-smooth, shadow-card/elevated), focus rings accessibles, prefers-reduced-motion, hero sombre avec radial gradients, btn-primary/ghost/outline, trust-strip avec 4 badges (souveraineté, open source, RGPD, déploiement 1j), pillars-row, stat-feature, section-header (eyebrow + h2 + lead), nav-toggle hamburger mobile, nav-grid--polished (icônes 40x40 avec hover scale), cta-band, action-list, reveal-on-scroll
→ index.html refondu : hero institutionnel sombre (eyebrow + title avec em gradient + subtitle + 2 CTAs + 4 hero-stats), trust strip, section "Pourquoi Uccello Hub" avec 4 piliers (souveraineté/hub centralisé/IA contextuelle/modèle clé en main), synthèse exécutive (existant) reformatée avec section-header, pipeline progress 11 étapes (ajout VSL), nav-grid--polished avec 12 cards (ajout VSL + contact), action-list 2 prochaines étapes, CTA band en bas
→ 10 pages existantes : ajout du nav-toggle hamburger pour menu mobile fonctionnel
→ app.js étendu : mobile toggle + reveal-on-scroll IntersectionObserver
→ Pré-delivery checklist appliquée : SVG icons (Lucide), cursor pointer, hover smooth 200ms, focus visible, light mode contrast 4.5:1, responsive 320px/768px/1024px, no emoji icons
/ui-ux-pro-max : ✅ 2026-05-05

2026-05-05 /offer-vsl-script update v1.1 — Naturalisation du verbatim (oral parlé, pas lu)
→ Problème identifié : style Hormozi-punchy avec phrases ultra-courtes ne passait pas en français parlé. Ex : "Dix clients. 168€ net par mois et par client. 1 680€..." sonnait robotique
→ Approche : ajout connecteurs ("et", "parce que", "alors", "et c'est là que"), phrases plus longues et liées, "vous voyez", "hein", "en fait" autorisés, mots gras réduits à 1-2 par phrase max
→ Spécificité préservée : tous les chiffres conservés (168€, 1 680€, 4 800€, 14 ans, 90 jours, etc.), Big Promise, mécanisme 3 piliers, stack 7 livrables avec valeurs ancrées, garantie 90 jours, 5 étapes du CTA
→ 12 actes longue + 6 cutdown + 7 hooks tableau + open loops + bucket brigade + future pacing + disqualification + P.S. tous réécrits
→ VSL_SCRIPT.md v1.1 (v1.0 conservé en historique git)
→ vsl.html dans website-internal/ mis à jour avec verbatim naturalisé
→ Notes de production : ajout du tic "tics de langage Jonathan à intégrer en lecture" (tu peux remplacer "donc" par "alors", inverser, ajouter des 'vous voyez' selon ton parler naturel)
/offer-vsl-script v1.1 : ✅ 2026-05-05

> Les agents notent ici ce qui nécessite une validation humaine avant de continuer.
