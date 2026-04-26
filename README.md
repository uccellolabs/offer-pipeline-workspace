# Offer Pipeline — Outputs

Repo de travail pour les projets générés par le pipeline `offer-pipeline`.
Contient tous les fichiers produits par les agents IA (briefs, personas, pricing, pitch decks...).

---

## Prérequis

Les skills pipeline doivent être installés globalement dans Cursor :

```bash
# Depuis le repo offer-pipeline (source de vérité des skills)
bash /chemin/vers/offer-pipeline/.cursor/skills/install.sh
```

Les skills sont alors disponibles dans **tous les workspaces Cursor**.

---

## Structure

```
offer-pipeline-work/
├── CLAUDE.md                    ← Règles globales du pipeline (ne pas modifier)
├── templates/                   ← Templates de démarrage
│   ├── PROJECT_CONTEXT.template.md
│   └── SESSION_LOG.template.md
├── projects/                    ← Outputs générés (tout versionner ici)
│   ├── <projet-1>/
│   │   ├── PROJECT_CONTEXT.md
│   │   ├── SESSION_LOG.md
│   │   ├── OFFER_BRIEF.md
│   │   ├── PERSONA_*.md
│   │   ├── COMPETITIVE_BRIEF.md
│   │   ├── PRICING_BRIEF.md
│   │   ├── OFFER_FINAL.md
│   │   ├── pitch-deck/
│   │   ├── website/
│   │   └── PROSPECTS_*.csv
│   └── archive/
└── .active-project              ← Projet actif courant (ignoré par git)
```

---

## Workflow

### 1. Nouveau projet

Ouvre ce dossier dans Cursor, puis :

```
/project-manager new mon-projet
```

Remplis `projects/mon-projet/PROJECT_CONTEXT.md` puis lance le pipeline.

### 2. Reprendre un projet existant

```
/project-manager switch mon-projet
```

### 3. Pipeline complet (ordre recommandé)

```
/idea-finder          → IDEA_BRIEF.md
/offer-cadrage        → OFFER_BRIEF.md
/persona              → PERSONA_*.md
/market-research      → enrichit OFFER_BRIEF
/competitive-intel    → COMPETITIVE_BRIEF.md
/pricing              → PRICING_BRIEF.md
/offer-final          → OFFER_FINAL.md
/pitch-deck           → pitch-deck/
/prospection-strategy → PROSPECTION_PLAYBOOK.md
/prospection-list     → PROSPECTS_*.csv
/study-website        → website/
```

Ou tout en une fois : `/orchestrator`

---

## Mettre à jour les skills

Les skills vivent dans le repo `offer-pipeline`. Pour mettre à jour :

```bash
# Depuis le repo offer-pipeline
git pull
bash .cursor/skills/install.sh   # recrée les symlinks si nécessaire
```

Comme les symlinks pointent vers la source, un `git pull` suffit en général.

---

## Git

Committer les outputs après chaque étape importante :

```bash
git add projects/mon-projet/
git commit -m "feat(mon-projet): /offer-cadrage — GO validé"
```
