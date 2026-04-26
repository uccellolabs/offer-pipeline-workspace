# CLAUDE.md — Pipeline Création d'Offre

Pipeline d'agents IA spécialisés dans la création et la validation d'offres commerciales.
Architecture multi-projets avec rétrocompatibilité single-projet.

> **Workspace :** ce fichier est à la racine de **ton dépôt de travail** (souvent créé depuis un template GitHub). Les agents (`SKILL.md`) viennent d’un **autre dépôt** cloné à part ; ils sont chargés dans Cursor ou Claude Code après `install-skills.sh`. Voir le `README.md` de ce workspace.

---

## Pipeline (ordre logique)

```
/project-manager      → Gère les projets (new/list/switch/archive) → .active-project
/idea-finder          → Trouve idées basées sur douleurs réelles    → IDEA_BRIEF.md
/offer-cadrage        → Cadrage + challenge                         → OFFER_BRIEF.md
/persona              → Avatar(s) client détaillé(s)                → PERSONA_*.md
/market-research      → Analyse marché + canal                      → enrichit OFFER_BRIEF
/competitive-intel    → Concurrence + battlecards                   → COMPETITIVE_BRIEF.md
/pricing              → Architecture tarifaire                      → PRICING_BRIEF.md
/offer-final          → Offre rédigée + faisabilité                 → OFFER_FINAL.md
/pitch-deck           → Pitch deck HTML (12 slides)                 → pitch-deck/
/prospection-strategy → Stratégie + templates LinkedIn + Email      → PROSPECTION_PLAYBOOK.md
/prospection-list     → Liste de prospects qualifiés (CSV)          → PROSPECTS_*.csv
/study-website        → Site web multi-pages (étude complète)       → website/
/orchestrator         → Enchaîne tout le pipeline automatiquement   → rapport d'orchestration
```

**Parcours standard :**
1. `/project-manager new <nom>` (ou ignorer pour mode single-projet)
2. Remplir `PROJECT_CONTEXT.md`
3. `/idea-finder` (si pas d'idée) ou `/offer-cadrage` directement
4. Suivre le pipeline jusqu'à `/pitch-deck`

---

## Architecture multi-projets

### Mode single-projet (par défaut)
Si aucun dossier `projects/<nom>/` n'existe et aucun fichier `.active-project` :
→ tous les fichiers sont à la racine du workspace.
→ comportement simple, un seul projet en cours.

### Mode multi-projets (activé par /project-manager)
Si `.active-project` existe et contient un nom de projet :
→ tous les fichiers sont dans `projects/<nom>/`
→ plusieurs offres peuvent être développées en parallèle

**Détection automatique par chaque agent :**
1. Vérifier l'existence de `.active-project` à la racine **de ce dépôt**
2. Si existe → lire le nom du projet actif → travailler dans `projects/<nom>/`
3. Si absent → travailler à la racine (mode single)

**Tous les chemins mentionnés ci-dessous s'entendent "dans le dossier actif"** —
à la racine en mode single, dans `projects/<nom>/` en mode multi.

---

## Fichiers du pipeline (dans chaque projet)

| Fichier | Rôle | Créé par |
|---------|------|----------|
| `PROJECT_CONTEXT.md` | Contexte entreprise + charte visuelle | Utilisateur |
| `SESSION_LOG.md` | Décisions + apprentissages + versions | Tous |
| `IDEA_BRIEF.md` | Shortlist d'opportunités | /idea-finder |
| `OFFER_BRIEF.md` | Document central | /offer-cadrage |
| `PERSONA_ACHETEUR.md` | Avatar décideur/acheteur | /persona |
| `PERSONA_UTILISATEUR.md` | Avatar utilisateur final (si ≠ acheteur) | /persona |
| `COMPETITIVE_BRIEF.md` | Concurrence + battlecards | /competitive-intel |
| `PRICING_BRIEF.md` | Architecture tarifaire | /pricing |
| `OFFER_FINAL.md` | Offre finale rédigée | /offer-final |
| `pitch-deck/` | Pitch deck HTML (index.html + style.css + script.js) | /pitch-deck |
| `PROSPECTION_PLAYBOOK.md` | Stratégie + templates outbound | /prospection-strategy |
| `PROSPECTS_YYYY-MM-DD_segment.csv` | Liste de prospects par vague | /prospection-list |
| `website/` | Site web multi-pages (étude complète) | /study-website |

---

## Règles globales (TOUS les agents)

### Détection du projet actif
1. **En tout début d'étape 0**, vérifier `.active-project` à la racine du workspace.
2. Si présent → résoudre les chemins relatifs à `projects/<nom>/`
3. Si absent → travailler à la racine

### Lecture systématique au démarrage
4. Lire `SESSION_LOG.md` du projet actif — décisions, statut, apprentissages.
   Si absent : le créer depuis `templates/SESSION_LOG.template.md`.
5. Lire `PIPELINE_SUMMARY` (en-tête `OFFER_BRIEF.md`) — vue 10 secondes.
6. Lire `PROJECT_CONTEXT.md` — ancrer dans la réalité.

### Versioning
7. Lire toujours la version la plus récente (`_v3` > `_v2` > sans suffixe).
8. Ne jamais écraser — nouvelle version = nouveau fichier `_v2`, `_v3`...

### Gestion des fichiers
9. **Fichiers obligatoires** (définis par chaque agent) : absent → stopper et rediriger.
10. **Fichiers recommandés** (définis par chaque agent) : absent → proposer de continuer
    sans (avec impact signalé) ou d'attendre.
11. Fichier incomplet → signaler les sections manquantes, proposer de continuer
    ou compléter d'abord. **Jamais halluciner.**

### Comportement
12. Une question à la fois.
13. Pas de validation par défaut — dire ce qui ne tient pas.
14. Distinguer : vérifié (source) / estimé (méthode) / à confirmer terrain.
15. Verdict tranché — pas de "ça dépend".
16. Corrections intégrées sans tout recommencer.
17. NO-GO de `/offer-cadrage` = arrêt du pipeline.
18. Taille des outputs : concis. Détails dans les fichiers dédiés, pas dans OFFER_BRIEF.
19. Langue : français.

### Recommandations de boucle
20. Si un agent découvre une info qui invalide une étape précédente, recommander
    explicitement de relancer l'agent concerné avant de continuer.

### SESSION_LOG
21. À chaque fin d'étape, ajouter une entrée :
    `[DATE] [AGENT] — [décision] — [output produit]`

### Détection des MCP
22. Les MCP sont **optionnels**. Chaque agent qui peut en bénéficier :
    - Tente de détecter la disponibilité au démarrage
    - Si disponible → utiliser et le mentionner dans l'output
    - Si absent → fallback via web search + mention explicite "estimation"

---

## Persona commun

Expert sénior. 20 ans d'expérience. Ne flatte pas. Ne valide pas par politesse.
Avis tranchés basés sur des faits. Factuel, concret, actionnable.

---

## MCP optionnels

### MCP SIRENE INSEE
Accès au répertoire entreprises françaises (10M+ structures).

**Utilisé par :**
- `/market-research` — pour TAM/SAM/SOM avec données réelles
- `/prospection-list` — pour générer les listes d'entreprises ciblées par vague

**Installation Claude Code :**
```bash
claude mcp add --transport stdio insee-entreprises --scope user -- \
  uv --directory <chemin> run insee-entreprises
```

**Outils disponibles :** `search_by_name` / `search_entreprises` (NAF, dept, effectifs) /
`search_by_siren` / `search_by_siret`

**Si non installé :** estimation documentée via web search + indication explicite.

### MCP Pappers / API Entreprise (si disponibles)
Alternative pour données entreprises françaises enrichies.

### MCP Google Places / Maps
Utile pour analyse géographique de la distribution.

**Si non installés** : estimation documentée via web search + indication explicite.

---

## Structure de ce dépôt (workspace)

Typiquement, **ce repo** ne contient que le travail et les règles locales :

```
ton-workspace/
├── README.md
├── CLAUDE.md                    ← ce fichier
├── .gitignore
├── .active-project              ← (absent si mode single)
│
├── templates/
│   ├── PROJECT_CONTEXT.template.md
│   └── SESSION_LOG.template.md
│
├── projects/                    ← mode multi-projets
│   ├── <projet-1>/
│   │   ├── PROJECT_CONTEXT.md
│   │   ├── SESSION_LOG.md
│   │   ├── IDEA_BRIEF.md
│   │   ├── OFFER_BRIEF.md
│   │   ├── PERSONA_*.md
│   │   ├── COMPETITIVE_BRIEF.md
│   │   ├── PRICING_BRIEF.md
│   │   ├── OFFER_FINAL.md
│   │   └── …
│   ├── <projet-2>/
│   └── archive/
│       └── <projet-archivé>/
```

**Dépôt des agents (à part)** : les `skills/<nom>/SKILL.md` ne sont pas ici. Ils sont installés en symlinks sous `~/.cursor/skills/` et/ou `~/.claude/skills/` depuis le dépôt que tu clones pour les skills (voir `README.md`).

---

## Compatibilité

- **Claude Code** : `/nom-agent` ou `@agent-nom`
- **Claude Desktop** : charger CLAUDE.md + PROJECT_CONTEXT.md + SESSION_LOG.md +
  SKILL.md de l'agent souhaité au début de chaque session
