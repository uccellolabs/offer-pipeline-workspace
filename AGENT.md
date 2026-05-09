# AGENT.md : Pipeline Création d'Offre

> **Cursor** utilise en général **`AGENT.md`** à la racine du workspace comme **instructions projet** pour l’IA. Le corps de ce fichier est **aligné sur `CLAUDE.md`** (mêmes règles). Quand tu modifies les règles dans le dépôt *Offer-Pipeline* ou dans ton workspace template, mets à jour **les deux** fichiers de la même façon.

Pipeline d'agents IA spécialisés dans la création et la validation d'offres commerciales.
Architecture multi-projets avec rétrocompatibilité single-projet.

---

## Pipeline (ordre logique)

```
/offer-project-manager      → Gère les projets (new/list/switch/archive) → .active-project
/offer-idea-finder          → Trouve idées basées sur douleurs réelles    → IDEA_BRIEF.md
/offer-cadrage        → Cadrage + challenge                         → OFFER_BRIEF.md
/offer-persona              → Avatar(s) client détaillé(s)                → PERSONA_*.md
/offer-market-research      → Analyse marché + canal                      → enrichit OFFER_BRIEF
/offer-competitive-intel    → Concurrence + battlecards                   → COMPETITIVE_BRIEF.md
/offer-pricing              → Architecture tarifaire                      → PRICING_BRIEF.md
/offer-final          → Offre rédigée + faisabilité                 → OFFER_FINAL.md
/offer-pitch-deck           → Pitch deck HTML (12 slides)                 → pitch-deck/
/offer-vsl-script           → Script de VSL (Video Sales Letter) verbatim → VSL_SCRIPT.md
/offer-case-study           → Capture et structure un cas client terrain   → CASE_STUDY_*.md
/offer-prospection-strategy → Stratégie + templates LinkedIn + Email      → PROSPECTION_PLAYBOOK.md + DISC_PROFILES.md
/offer-prospection-list     → Liste de prospects qualifiés (CSV)          → PROSPECTS_*.csv
/offer-cold-call            → Script cold call verbatim (DISC × objections) → COLD_CALL_SCRIPT.md
/offer-discovery-call       → Plan d'entretien commercial + recap         → DISCOVERY_CALL_PLAN.md + CALL_RECAP_*.md
/offer-study-website        → Site web multi-pages (étude complète)       → website/
/offer-commercial-proposal  → Proposition commerciale web nominative      → proposals/<slug>/
/offer-orchestrator         → Enchaîne tout le pipeline automatiquement   → rapport d'orchestration

/brand-positioning          → Angle unique, piliers, ton, 15 angles        → BRAND_POSITIONING.md
/brand-interview            → Interview structurée → banque de contenus réels → BRAND_CONTENT_BANK.md
/brand-profile              → Optimisation profils (LinkedIn, Insta, X)    → BRAND_PROFILES.md
/brand-post                 → Rédaction post (LinkedIn / Insta / X)        → POST_<slug>.md
/brand-reel                 → Script verbatim reel / vidéo courte          → REEL_SCRIPT_<slug>.md

/business-coach             → Coach business transversal (objectifs 12 sem, missions, journaling) → coach/ (workspace)
```

**Parcours standard :**
1. `/offer-project-manager new <nom>` (ou ignorer pour mode single-projet)
2. Remplir `PROJECT_CONTEXT.md`
3. `/offer-idea-finder` (si pas d'idée) ou `/offer-cadrage` directement
4. Suivre le pipeline jusqu'à `/offer-pitch-deck`

---

## Architecture multi-projets

### Mode single-projet (par défaut)
Si aucun dossier `projects/<nom>/` n'existe et aucun fichier `.active-project` :
→ tous les fichiers sont à la racine du pipeline.
→ comportement simple, un seul projet en cours.

### Mode multi-projets (activé par /offer-project-manager)
Si `.active-project` existe et contient un nom de projet :
→ tous les fichiers sont dans `projects/<nom>/`
→ plusieurs offres peuvent être développées en parallèle

**Détection automatique par chaque agent :**
1. Vérifier l'existence de `.active-project` à la racine
2. Si existe → lire le nom du projet actif → travailler dans `projects/<nom>/`
3. Si absent → travailler à la racine (mode single)

**Tous les chemins mentionnés ci-dessous s'entendent "dans le dossier actif"** :
à la racine en mode single, dans `projects/<nom>/` en mode multi.

---

## Fichiers du pipeline (dans chaque projet)

| Fichier | Rôle | Créé par |
|---------|------|----------|
| `PROJECT_CONTEXT.md` | Contexte entreprise + charte visuelle | Utilisateur |
| `SESSION_LOG.md` | Décisions + apprentissages + versions | Tous |
| `IDEA_BRIEF.md` | Shortlist + tableau **Sources utilisées** (liens exacts) | /offer-idea-finder |
| `OFFER_BRIEF.md` | Document central | /offer-cadrage |
| `PERSONA_ACHETEUR.md` | Avatar décideur/acheteur | /offer-persona |
| `PERSONA_UTILISATEUR.md` | Avatar utilisateur final (si ≠ acheteur) | /offer-persona |
| `COMPETITIVE_BRIEF.md` | Concurrence + battlecards | /offer-competitive-intel |
| `PRICING_BRIEF.md` | Architecture tarifaire | /offer-pricing |
| `OFFER_FINAL.md` | Offre finale rédigée | /offer-final |
| `pitch-deck/` | Pitch deck HTML (index.html + style.css + script.js) | /offer-pitch-deck |
| `VSL_SCRIPT.md` | Script de VSL verbatim (12 actes, voyage du héros, open loops) | /offer-vsl-script |
| `CASE_STUDY_[client].md` | Cas client structuré (avant/après, résultats, verbatim) | /offer-case-study |
| `DISC_PROFILES.md` | Référentiel DISC du projet (source de vérité cross-skills) | /offer-prospection-strategy |
| `PROSPECTION_PLAYBOOK.md` | Stratégie + templates outbound | /offer-prospection-strategy |
| `PROSPECTS_YYYY-MM-DD_segment.csv` | Liste de prospects par vague | /offer-prospection-list |
| `COLD_CALL_SCRIPT.md` | Script verbatim cold call (5 blocs × 4 profils DISC) | /offer-cold-call |
| `DISCOVERY_CALL_PLAN.md` | Plan d'entretien commercial structuré | /offer-discovery-call |
| `CALL_RECAP_TBD_<Prospect>.md` | Template compte-rendu pré-rempli (à compléter post-call) | /offer-discovery-call |
| `CALL_RECAP_YYYY-MM-DD_<Prospect>.md` | Compte-rendu post-call complété | Toi |
| `MARKET_RESEARCH.md` | Analyse marché + canal (fichier séparé, toujours) | /offer-market-research |
| `website/` | Site multi-pages (étude) ; **interne** : `/decouverte` si `IDEA_BRIEF*.md` | /offer-study-website |
| `proposals/<slug>/` | Proposition commerciale web nominative (un dossier par prospect) | /offer-commercial-proposal |
| `BRAND_POSITIONING.md` | Angle unique, piliers thématiques, ton, 15 angles d'attaque | /brand-positioning |
| `BRAND_CONTENT_BANK.md` | Banque de contenus véridiques (histoires, résultats, opinions, méthodes) | /brand-interview |
| `BRAND_PROFILES.md` | Profils optimisés (LinkedIn, Instagram, X) prêts à copier | /brand-profile |
| `POST_<slug>.md` | Post verbatim prêt à publier (LinkedIn / Instagram / X) | /brand-post |
| `REEL_SCRIPT_<slug>.md` | Script verbatim reel / vidéo courte avec directions d'acteur | /brand-reel |

---

## Fichiers transversaux (racine workspace, hors `projects/`)

Le coach business vit **au-dessus** des projets. Ses fichiers sont à la racine du workspace, partagés entre toutes les offres.

| Fichier | Rôle | Créé par |
|---------|------|----------|
| `coach/COACH_BRIEF.md` | Spec figée du système coach (cadrage v1.0) | Cadrage initial (utilisateur + Claude) |
| `coach/GOALS.md` | Objectifs cycle 12 semaines + OKR semaine en cours | /business-coach |
| `coach/MISSIONS.md` | Backlog daté + missions cochables alignées sur les KR | /business-coach |
| `coach/COACH_LOG.md` | Changelog des sessions et interventions du coach | /business-coach |
| `coach/JOURNAL/<semaine>/...` | Briefings matin + reviews soir + deep journal hebdo | /business-coach (Phase 2) |
| `coach/REVIEWS/` | Rétros hebdo + fin de cycle 12 semaines | /business-coach (Phase 2) |
| `coach/MEETINGS/` | CR de réunions à ingérer (clients, partenaires, prospects) | Toi (dépôt manuel) |
| `coach/DRAFTS/` | Préparations silencieuses du dimanche (drafts d'OKR) | /business-coach (Phase 2) |
| `coach/OUT_OF_SCOPE.md` | Sujets hors périmètre notés mais non traités | /business-coach |

---

## Règles globales (TOUS les agents)

### Détection du projet actif
1. **En tout début d'étape 0**, vérifier `.active-project` à la racine du pipeline.
2. Si présent → résoudre les chemins relatifs à `projects/<nom>/`
3. Si absent → travailler à la racine

### Lecture systématique au démarrage
4. Lire `SESSION_LOG.md` du projet actif, décisions, statut, apprentissages.
   Si absent : le créer depuis `templates/SESSION_LOG.template.md`.
5. Lire `PIPELINE_SUMMARY` (en-tête `OFFER_BRIEF.md`) : vue 10 secondes.
6. Lire `PROJECT_CONTEXT.md` : ancrer dans la réalité.

### Versioning
7. Lire toujours la version la plus récente (`_v3` > `_v2` > sans suffixe).
8. Ne jamais écraser, nouvelle version = nouveau fichier `_v2`, `_v3`...

### Gestion des fichiers
9. **Fichiers obligatoires** (définis par chaque agent) : absent → stopper et rediriger.
10. **Fichiers recommandés** (définis par chaque agent) : absent → proposer de continuer
    sans (avec impact signalé) ou d'attendre.
11. Fichier incomplet → signaler les sections manquantes, proposer de continuer
    ou compléter d'abord. **Jamais halluciner.**

### Comportement
12. Une question à la fois.
13. Pas de validation par défaut, dire ce qui ne tient pas.
14. Distinguer : vérifié (source) / estimé (méthode) / à confirmer terrain.
15. Verdict tranché, pas de "ça dépend".
16. Corrections intégrées sans tout recommencer.
17. NO-GO de `/offer-cadrage` = arrêt du pipeline.
18. Taille des outputs : concis. Détails dans les fichiers dédiés, pas dans OFFER_BRIEF.
19. Langue : français.
19bis. **Typographie française** : ne JAMAIS utiliser le tiret cadratin « — » (em-dash, U+2014) dans le contenu généré (briefs, copy commerciale, scripts, slides, pages web, emails, posts LinkedIn, comptes-rendus). Le tiret cadratin n'est pas un usage typographique français. Remplacer par :
    - « : » pour une définition (« X : explication »)
    - « , » pour une incise mid-sentence (« mot, incise, suite »)
    - « (…) » pour une parenthèse
    - Pour un titre avec sous-titre : « Titre : sous-titre » ou « Titre. Sous-titre »
    - S'applique également aux scripts verbaux (cold-call, discovery-call) : à l'oral on ne dit pas un em-dash.

### Recommandations de boucle
20. Si un agent découvre une info qui invalide une étape précédente, recommander
    explicitement de relancer l'agent concerné avant de continuer.

### SESSION_LOG
21. À chaque fin d'étape, ajouter une entrée :
    `[DATE] [AGENT] : [décision] : [output produit]`

### Détection des MCP
22. Les MCP sont **optionnels**. Chaque agent qui peut en bénéficier :
    - Tente de détecter la disponibilité au démarrage
    - Si disponible → utiliser et le mentionner dans l'output
    - Si absent → fallback via web search + mention explicite "estimation"

### Maintenance et synchronisation (s'applique aux modifications du dépôt lui-même)
23. **Après toute modification** d'un fichier de ce dépôt, vérifier systématiquement
    si les fichiers suivants doivent aussi être mis à jour :

    **Dans ce dépôt (`offer-pipeline`) :**
    - `README.md` : compteur d'agents, liste des skills, tableau des fichiers générés,
      section "Les agents", structure de dossiers
    - `CLAUDE.md` : pipeline table, fichiers table, structure skills
    - `AGENT.md` : miroir de `CLAUDE.md` (mêmes sections, toujours synchronisé)
    - `templates/SESSION_LOG.template.md` : statut pipeline + tableau versions

    **Dans le workspace (`/Users/jonathan/development/www/agents/offer-pipeline-workspace`) :**
    - `CLAUDE.md` : mêmes sections que ci-dessus
    - `AGENT.md` : miroir de `CLAUDE.md`
    - `README.md` : structure projet, tableau pipeline, notes explicatives
    - `templates/SESSION_LOG.template.md` : même contenu que la version pipeline

    **Règle de décision :** si la modification concerne un agent (ajout, renommage,
    suppression), un fichier de sortie, ou une règle globale → les 8 fichiers
    ci-dessus sont candidats à la mise à jour. Vérifier chacun, mettre à jour
    ceux qui sont impactés, signaler explicitement ceux qui ne le sont pas.

---

## Persona commun

Expert sénior. 20 ans d'expérience. Ne flatte pas. Ne valide pas par politesse.
Avis tranchés basés sur des faits. Factuel, concret, actionnable.

---

## MCP optionnels

### MCP Datagouv (data.gouv.fr, recommandé)
Catalogue officiel de l’open data française : recherche de jeux, ressources tabulaires et dataservices référencés. Permet d’exploiter les fichiers ou APIs publiés sur le portail (dont les jeux relatifs aux entreprises / établissements lorsqu’ils y sont exposés).

**Utilisé par :**
- `/offer-market-research` : ordres de grandeur et segments sourçables depuis des jeux publics
- `/offer-prospection-list` : listes à partir de CSV/XLSX du catalogue (`search_datasets` → `list_dataset_resources` → `query_resource_data`, filtres selon colonnes)
- `/offer-idea-finder` : validation grossière de taille de segment quand une source adaptée existe

**Instance hébergée (sans clé, lecture seule) :** `https://mcp.data.gouv.fr/mcp`

**Cursor** (`~/.cursor/mcp.json`) :

```json
{
  "mcpServers": {
    "datagouv": {
      "url": "https://mcp.data.gouv.fr/mcp",
      "transport": "http"
    }
  }
}
```

**Claude Code :**

```bash
claude mcp add --transport http datagouv https://mcp.data.gouv.fr/mcp
```

**Alternative** (`npx` si le client ne prend pas le HTTP natif) : `npx -y mcp-remote https://mcp.data.gouv.fr/mcp`

**Outils principaux :** `search_datasets` · `list_dataset_resources` · `get_dataset_info` · `get_resource_info` · `query_resource_data` · `search_dataservices` · `get_dataservice_info` · `get_dataservice_openapi_spec` · `get_metrics`

**Référence :** dépôt officiel [datagouv/datagouv-mcp](https://github.com/datagouv/datagouv-mcp).

**Si non installé :** estimation documentée via web search + mention explicite.

### MCP INSEE entreprises, SIRENE (optionnel, tiers)
Serveur communautaire en accès direct au répertoire SIRENE (requêtes type annuaire : NAF, département, effectifs). Complément lorsque tu veux ce mode d’interaction **en plus** de Datagouv.

**Installation Claude Code :**

```bash
claude mcp add --transport stdio insee-entreprises --scope user -- \
  uv --directory <chemin> run insee-entreprises
```

**Outils disponibles :** `search_by_name` / `search_entreprises` / `search_by_siren` / `search_by_siret`

**Si non installé :** préférer le MCP Datagouv ou fallback web search.

### MCP Pappers / API Entreprise (si disponibles)
Alternative pour données entreprises françaises enrichies.

### MCP Google Places / Maps
Utile pour analyse géographique de la distribution et enrichissement GMB (`/offer-prospection-list`).

**Implémentation :** utiliser le serveur local `mcp/google-maps-server/` (Places API **New** pour recherche et fiches lieu).

**Installation (npm, clé API Google, Claude Code, Cursor / `~/.cursor/mcp.json`, chemin absolu) :** voir **`README.md`** : section *« MCP Google Maps, coordonnées prospects »*.

**Outils MCP :** `maps_search_places` / `maps_place_details` (Places New) ; `maps_geocode` / `maps_reverse_geocode` ; optionnellement `maps_distance_matrix`, `maps_directions`, `maps_elevation`.

**Si non installés** : estimation documentée via web search + indication explicite.

### Skill `ui-ux-pro-max` (requis pour `/offer-study-website` et `/offer-commercial-proposal`)

`/offer-study-website` et `/offer-commercial-proposal` délèguent la génération du design à ce skill.
**Doit être installé avant de les lancer.**

**Installation Claude Code :**
```bash
claude plugin install ui-ux-pro-max-skill
```

**Installation Cursor :** Marketplace Cursor → chercher `ui-ux-pro-max`, ou copier manuellement dans `~/.cursor/skills/ui-ux-pro-max/SKILL.md`.

**Vérification :**
```bash
ls ~/.claude/skills/ui-ux-pro-max/SKILL.md   # Claude Code
ls ~/.cursor/skills/ui-ux-pro-max/SKILL.md   # Cursor
```

**Si non installé :** le site est quand même généré, mais les règles de design (responsive, typographie, palettes) seront moins précises.

---

## Structure des dossiers

```
Offer-Pipeline/                  ← dépôt des skills (source de vérité des agents)
├── README.md
├── CLAUDE.md
├── AGENT.md                     ← miroir de CLAUDE.md pour Cursor (même règles)
├── .gitignore
├── install-skills.sh
├── mcp/google-maps-server/     ← MCP Google Maps (Places API New)
├── templates/
│   ├── PROJECT_CONTEXT.template.md
│   └── SESSION_LOG.template.md
├── projects/                    ← optionnel (travail local, souvent gitignored)
└── skills/                      ← les agents (installés en symlinks)
    ├── offer-project-manager/SKILL.md
    ├── offer-orchestrator/SKILL.md
    ├── offer-idea-finder/SKILL.md
    ├── offer-cadrage/SKILL.md
    ├── offer-persona/SKILL.md
    ├── offer-market-research/SKILL.md
    ├── offer-competitive-intel/SKILL.md
    ├── offer-pricing/SKILL.md
    ├── offer-final/SKILL.md
    ├── offer-pitch-deck/SKILL.md
    ├── offer-vsl-script/SKILL.md
    ├── offer-case-study/SKILL.md
    ├── offer-prospection-strategy/SKILL.md
    ├── offer-prospection-list/SKILL.md
    ├── offer-cold-call/SKILL.md
    ├── offer-discovery-call/SKILL.md
    ├── offer-study-website/SKILL.md
    ├── offer-commercial-proposal/SKILL.md
    ├── brand-positioning/SKILL.md
    ├── brand-interview/SKILL.md
    ├── brand-profile/SKILL.md
    ├── brand-post/SKILL.md
    ├── brand-reel/SKILL.md
    ├── business-coach/SKILL.md      ← coach transversal (Phase 1)
    └── …
```

---

## Compatibilité

- **Cursor** : instructions projet via **`AGENT.md`** ou **`CLAUDE.md`** à la racine du workspace ouvert (template) ; les skills dans `~/.cursor/skills/`.
- **Claude Code** : `/offer-…` (nom du skill) ou `@offer-…` ; skills dans `~/.claude/skills/`.
- **Claude Desktop** : charger CLAUDE.md + PROJECT_CONTEXT.md + SESSION_LOG.md +
  SKILL.md de l'agent souhaité au début de chaque session
