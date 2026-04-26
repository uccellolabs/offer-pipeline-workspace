# Offer Pipeline — Workspace

Workspace de travail du pipeline de création d'offres.
Contient tous les fichiers produits par les agents IA : briefs, personas, pricing, pitch decks, listes de prospects...

> **Les skills IA vivent dans [`uccellolabs/Offer-Pipeline`](https://github.com/uccellolabs/Offer-Pipeline).**
> Ce repo ne contient que les outputs et la configuration du workspace.

---

## Démarrage rapide

### 1. Utiliser ce template

Clique sur **"Use this template"** → **"Create a new repository"** sur GitHub,
puis clone ton nouveau repo :

```bash
git clone git@github.com:<toi>/<ton-repo>.git
cd <ton-repo>
```

### 2. Installer les skills pipeline dans Cursor

```bash
git clone git@github.com:uccellolabs/Offer-Pipeline.git
bash Offer-Pipeline/.cursor/skills/install.sh
```

Les skills sont installés via symlinks dans `~/.cursor/skills/` —
disponibles dans **tous tes workspaces Cursor**, mis à jour automatiquement par `git pull`.

### 3. Ouvrir ce dossier dans Cursor

```
File → Open Folder → <ton-repo>/
```

`CLAUDE.md` est chargé automatiquement. Les skills sont prêts.

### 4. Lancer le pipeline

```
/project-manager new mon-projet
```

Remplis `projects/mon-projet/PROJECT_CONTEXT.md` puis suis le pipeline.

---

## Structure

```
workspace/
├── CLAUDE.md                    ← Règles globales du pipeline (auto-chargé par Cursor)
├── templates/                   ← Templates de démarrage
│   ├── PROJECT_CONTEXT.template.md
│   └── SESSION_LOG.template.md
├── projects/                    ← Outputs générés par les agents
│   ├── <projet-1>/
│   │   ├── PROJECT_CONTEXT.md   ← à remplir manuellement
│   │   ├── SESSION_LOG.md
│   │   ├── OFFER_BRIEF.md
│   │   ├── PERSONA_*.md
│   │   ├── COMPETITIVE_BRIEF.md
│   │   ├── PRICING_BRIEF.md
│   │   ├── OFFER_FINAL.md
│   │   ├── PROSPECTION_PLAYBOOK.md
│   │   ├── PROSPECTS_*.csv
│   │   ├── pitch-deck/
│   │   └── website/
│   └── archive/
└── .active-project              ← Projet actif courant (ignoré par git)
```

---

## Pipeline complet

| Commande | Output | Description |
|---|---|---|
| `/project-manager new <nom>` | dossier projet | Initialise un projet |
| `/idea-finder` | `IDEA_BRIEF.md` | Trouve des opportunités réelles |
| `/offer-cadrage` | `OFFER_BRIEF.md` | Cadrage + verdict GO/NO-GO |
| `/persona` | `PERSONA_*.md` | Avatar client détaillé |
| `/market-research` | enrichit OFFER_BRIEF | Marché + canal de distribution |
| `/competitive-intel` | `COMPETITIVE_BRIEF.md` | Analyse concurrentielle |
| `/pricing` | `PRICING_BRIEF.md` | Architecture tarifaire |
| `/offer-final` | `OFFER_FINAL.md` | Offre rédigée + score viabilité |
| `/pitch-deck` | `pitch-deck/` | Pitch deck HTML 12 slides |
| `/prospection-strategy` | `PROSPECTION_PLAYBOOK.md` | Stratégie outbound + templates |
| `/prospection-list` | `PROSPECTS_*.csv` | Liste de prospects qualifiés |
| `/study-website` | `website/` | Site web multi-pages |
| `/orchestrator` | tout | Pipeline complet automatique |

---

## Mettre à jour les skills

Les skills pointent vers ton clone local de `Offer-Pipeline` via symlinks.
Pour mettre à jour :

```bash
cd Offer-Pipeline
git pull
# Les symlinks font le reste — aucune action supplémentaire
```

Si les symlinks sont cassés (nouveau poste, nouvelle machine) :
```bash
bash Offer-Pipeline/.cursor/skills/install.sh
```

---

## Git

Committer les outputs après chaque étape :

```bash
git add projects/mon-projet/
git commit -m "feat(mon-projet): /offer-cadrage — GO validé"
git push
```

---

## Prérequis

- [Cursor](https://cursor.sh) avec accès aux skills (`~/.cursor/skills/`)
- [`uccellolabs/Offer-Pipeline`](https://github.com/uccellolabs/Offer-Pipeline) cloné + `install.sh` exécuté
