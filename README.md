# Offer Pipeline — Workspace

Workspace de travail du pipeline de création d’offres.
Contient tous les fichiers produits par les agents IA : briefs, personas, pricing, pitch decks, listes de prospects…

> **Les skills** (les agents du pipeline) vivent dans un **autre dépôt Git** — en général un dépôt nommé `Offer-Pipeline` — que tu clones à part (voir étape 2).  
> **Ce dépôt-ci** ne sert qu’à versionner tes outputs et ta config de workspace.

---

## Démarrage rapide

### 1. Utiliser ce template

Sur la page GitHub de **ce** dépôt, clique sur **« Use this template »** → **« Create a new repository »**,  
puis clone **ton** nouveau dépôt :

```bash
git clone git@github.com:<toi>/<ton-repo>.git
cd <ton-repo>
```

### 2. Installer les skills (Cursor ou Claude Code)

Récupère le dépôt qui contient les skills (remplace `<organisation>` par le compte ou l’orga qui héberge le dépôt — ou l’URL d’un fork) :

```bash
git clone git@github.com:<organisation>/Offer-Pipeline.git
cd Offer-Pipeline
bash install-skills.sh
```

Le menu propose **Cursor** (`~/.cursor/skills/`), **Claude Code** (`~/.claude/skills/`) ou **les deux**. Sans menu : `bash install-skills.sh --cursor`, `--claude` ou `--both`.

**Documentation** : ouvre le fichier `README.md` à la racine de ton clone `Offer-Pipeline` et suis la section sur l’installation des skills (Cursor ou Claude Code).

### 3. Ouvrir ce dossier dans ton IDE

- **Cursor** : `File → Open Folder → <ton-repo>/`
- **Claude Code** : ouvre ce même dossier comme projet

`CLAUDE.md` à la racine charge les règles du pipeline ; les commandes `/…` viennent des skills installés à l’étape 2.

### 4. Lancer le pipeline

```
/project-manager new mon-projet
```

Remplis `projects/mon-projet/PROJECT_CONTEXT.md` puis suis le pipeline.

---

## Structure

```
workspace/
├── CLAUDE.md                    ← Règles globales du pipeline
├── templates/                   ← Templates de démarrage
│   ├── PROJECT_CONTEXT.template.md
│   └── SESSION_LOG.template.md
├── projects/                    ← Fichiers générés par les agents
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
└── .active-project              ← Projet actif courant (souvent ignoré par git)
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

Les skills pointent vers ton clone local de `Offer-Pipeline` via des symlinks.

```bash
cd Offer-Pipeline
git pull
```

Si les symlinks sont cassés (nouveau poste, nouvelle machine) :

```bash
bash Offer-Pipeline/install-skills.sh --both
```

(adapte le chemin si ton clone n’est pas à côté du workspace.)

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

- [Cursor](https://cursor.sh) et/ou **Claude Code**, avec les skills installés (`install-skills.sh`)
- Un clone du dépôt **Offer-Pipeline** (ou équivalent) contenant le dossier `skills/`, puis `bash install-skills.sh`
