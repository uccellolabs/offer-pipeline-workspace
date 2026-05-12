# Offer Pipeline — Workspace

Ce dépôt est un **template d’espace de travail** : tu y versions uniquement **tes livrables** (briefs, personas, pitch decks, listes de prospects, etc.).

Les **agents IA** du pipeline (commandes `/offer-idea-finder`, `/offer-cadrage`, etc.) ne sont **pas** dans ce dépôt. Ils sont fournis par un **autre dépôt**, à cloner à part et à installer une fois sur ta machine.

---

## Ce dépôt vs dépôt des skills

| | **Ce dépôt (template workspace)** | **[Offer-Pipeline](https://github.com/uccellolabs/Offer-Pipeline)** — dépôt principal |
|---|---|---|
| **Rôle** | Ton projet Git : `projects/`, `CLAUDE.md`, `templates/` | Catalogue des **skills** (`skills/*/SKILL.md`), script `install-skills.sh`, doc complète |
| **Tu le forks / dupliques ?** | Oui — via « Use this template » pour **ton** repo | Tu le **clones** (ou tu en fais un fork si tu veux figer ta version) |
| **Fréquence de mise à jour** | Souvent (chaque étape du pipeline) | Rarement ; `git pull` met à jour les agents pour tout le monde |

**Lien direct du dépôt principal :** [github.com/uccellolabs/Offer-Pipeline](https://github.com/uccellolabs/Offer-Pipeline)

**Documentation détaillée** (installation Cursor / Claude Code, dépannage, liste des agents) : [README du dépôt Offer-Pipeline](https://github.com/uccellolabs/Offer-Pipeline/blob/main/README.md).

En résumé : **ouvre ton workspace dans l’IDE** (ce repo-ci) ; **installe les skills une fois** depuis Offer-Pipeline ; les fichiers générés par les agents vont dans `projects/<nom>/` ici.

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

Clone le **dépôt principal** qui contient les skills (même emplacement que le tableau ci-dessus) :

```bash
git clone https://github.com/uccellolabs/Offer-Pipeline.git
cd Offer-Pipeline
bash install-skills.sh
```

*(En SSH : `git clone git@github.com:uccellolabs/Offer-Pipeline.git`.)*

Le menu propose **Cursor** (`~/.cursor/skills/`), **Claude Code** (`~/.claude/skills/`) ou **les deux**. Sans menu : `bash install-skills.sh --cursor`, `--claude` ou `--both`.

Si tu utilises **un fork** d’Offer-Pipeline, remplace l’URL par celle de ton fork ; le principe reste le même : un clone du repo qui contient le dossier `skills/` et le script `install-skills.sh`.

### 3. Ouvrir ce dossier dans ton IDE

- **Cursor** : `File → Open Folder → <ton-repo>/` (le repo créé à l’étape 1, pas obligatoirement `Offer-Pipeline`)
- **Claude Code** : ouvre ce même dossier comme projet

**`AGENT.md`** et **`CLAUDE.md`** à la racine du workspace reprennent les mêmes règles du pipeline (**Cursor** charge en priorité `AGENT.md` ; garde les deux fichiers alignés). Les commandes `/…` viennent des skills installés à l’étape 2.

### 4. Lancer le pipeline

```
/offer-project-manager new mon-projet
```

Remplis `projects/mon-projet/PROJECT_CONTEXT.md` puis suis le pipeline (voir le README d’Offer-Pipeline pour l’ordre des étapes).

---

## Structure

```
workspace/
├── CLAUDE.md                    ← Règles globales du pipeline
├── AGENT.md                     ← Même contenu pour Cursor (instructions projet)
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
│   │   ├── DISCOVERY_CALL_PLAN.md   ← /offer-discovery-call (plan d’entretien)
│   │   ├── CALL_RECAP_*.md          ← compte-rendu post-call (rempli après le RDV)
│   │   ├── pitch-deck/
│   │   ├── website/
│   │   ├── BRAND_POSITIONING.md     ← /brand-positioning
│   │   ├── BRAND_CONTENT_BANK.md    ← /brand-interview (obligatoire avant posts/reels)
│   │   ├── POST_*.md                ← /brand-post
│   │   └── REEL_SCRIPT_*.md         ← /brand-reel
│   └── archive/
├── coach/                       ← Fichiers transversaux du /business-coach
│   ├── COACH_BRIEF.md           ← Spec figée du système coach (v1.0)
│   ├── GOALS.md                 ← Objectifs cycle 12 semaines + OKR semaine
│   ├── MISSIONS.md              ← Backlog daté + missions cochables
│   ├── COACH_LOG.md             ← Changelog des sessions du coach
│   ├── JOURNAL/                 ← Phase 2 : briefings matin + reviews soir + deep journal
│   ├── REVIEWS/                 ← Phase 2 : rétros hebdo + fin de cycle
│   └── MEETINGS/                ← CR de réunions à ingérer (clients, partenaires)
├── .claude/
│   └── scripts/                 ← Scripts utilitaires (auto-sync GitHub, etc.)
│       ├── autosync-pull.sh
│       └── autosync-push.sh
└── .active-project              ← Projet actif courant (souvent ignoré par git)
```

---

## Pipeline complet

| Commande | Output | Description |
|---|---|---|
| `/offer-project-manager new <nom>` | dossier projet | Initialise un projet |
| `/offer-idea-finder` | `IDEA_BRIEF.md` | Trouve des opportunités réelles |
| `/offer-cadrage` | `OFFER_BRIEF.md` | Cadrage + verdict GO/NO-GO |
| `/offer-persona` | `PERSONA_*.md` | Avatar client détaillé |
| `/offer-market-research` | enrichit OFFER_BRIEF | Marché + canal de distribution |
| `/offer-competitive-intel` | `COMPETITIVE_BRIEF.md` | Analyse concurrentielle |
| `/offer-pricing` | `PRICING_BRIEF.md` | Architecture tarifaire |
| `/offer-final` | `OFFER_FINAL.md` | Offre rédigée + score viabilité |
| `/offer-pitch-deck` | `pitch-deck/` | Pitch deck HTML 12 slides |
| `/offer-prospection-strategy` | `PROSPECTION_PLAYBOOK.md` | Stratégie outbound + templates |
| `/offer-prospection-list` | `PROSPECTS_*.csv` | Liste de prospects qualifiés |
| `/offer-discovery-call` | `DISCOVERY_CALL_PLAN.md` + `CALL_RECAP_YYYY-MM-DD_<prospect>.md` | Plan d’entretien commercial (SPICED, MEDDIC, adaptation DISC) + modèle de compte-rendu après le call |
| `/offer-study-website` | `website/` | Site web multi-pages |
| `/offer-orchestrator` | tout | Pipeline complet automatique |
| `/brand-positioning` | `BRAND_POSITIONING.md` | Angle unique, piliers, ton, 15 angles |
| `/brand-interview` | `BRAND_CONTENT_BANK.md` | Banque de contenus réels (obligatoire avant posts) |
| `/brand-profile` | `BRAND_PROFILES.md` | Profils optimisés LinkedIn / Instagram / X |
| `/brand-post` | `POST_<slug>.md` | Post verbatim prêt à publier |
| `/brand-reel` | `REEL_SCRIPT_<slug>.md` | Script de reel / vidéo courte |
| `/business-coach` | `coach/GOALS.md` + `coach/MISSIONS.md` + `coach/COACH_LOG.md` (workspace root) | **Coach transversal** : objectifs 12 sem, OKR hebdo, missions cochables, journaling. Sous-commandes : `init`, `session`, `status` |

**`/offer-discovery-call`** — à lancer quand l’offre est figée : il exige en général `OFFER_FINAL.md`, `PERSONA_ACHETEUR.md`, `PRICING_BRIEF.md` (et idéalement `COMPETITIVE_BRIEF.md`). Il produit d’abord **`DISCOVERY_CALL_PLAN.md`** (trame du call), puis tu utilises le gabarit **`CALL_RECAP_…`** pour noter ce qui s’est passé après l’entretien.

---

## Mettre à jour les skills

Les skills installés pointent en général vers ton clone local d’**Offer-Pipeline** via des symlinks.

```bash
cd Offer-Pipeline
git pull
```

Si les symlinks sont cassés (nouveau poste, nouvelle machine) :

```bash
bash /chemin/vers/Offer-Pipeline/install-skills.sh --both
```

---

## Git

Committer les outputs après chaque étape :

```bash
git add projects/mon-projet/
git commit -m "feat(mon-projet): /offer-cadrage : GO validé"
git push
```

---

## Auto-sync GitHub (optionnel)

Le template embarque 2 scripts dans `.claude/scripts/` qui, branchés sur des **hooks Claude Code**, synchronisent automatiquement le workspace avec GitHub. Utile si tu veux pouvoir consulter / éditer tes briefs depuis le téléphone (Working Copy iOS, GitHub Mobile) ou bosser sur plusieurs machines sans penser à `git push`.

| Hook | Script | Quand | Effet |
|---|---|---|---|
| `SessionStart` | `autosync-pull.sh` | Au démarrage de Claude Code | `git pull --rebase --autostash origin main` (récupère les commits faits depuis une autre machine ou le téléphone) |
| `Stop` | `autosync-push.sh` | À chaque fin de tour Claude | Si dirty : `git add -A && git commit && git push origin main` |

**Protections du push** (anti-erreur classique) : skip si `node_modules/` détecté dans les changements, skip si un fichier > 10 MB est en jeu. Logs : `~/Library/Logs/<nom-du-workspace>-autosync.log` (le nom dérive automatiquement du dossier).

**Portabilité** : les scripts dérivent le chemin du workspace de leur propre emplacement (via `BASH_SOURCE`), pas de path hardcodé. Ils marchent dès le clone, sur n'importe quelle machine.

### Activer

1. Clone ton workspace (issu de ce template), puis assure-toi que les scripts sont exécutables :

   ```bash
   chmod +x .claude/scripts/autosync-*.sh
   ```

2. Crée `.claude/settings.local.json` à la racine du workspace. Ce fichier est **gitignored** (perso, jamais committé), donc à recréer sur chaque machine.

   ```json
   {
     "hooks": {
       "SessionStart": [
         {
           "hooks": [
             {
               "type": "command",
               "command": "/CHEMIN/ABSOLU/VERS/ton-workspace/.claude/scripts/autosync-pull.sh",
               "timeout": 30,
               "statusMessage": "Pulling remote changes..."
             }
           ]
         }
       ],
       "Stop": [
         {
           "hooks": [
             {
               "type": "command",
               "command": "/CHEMIN/ABSOLU/VERS/ton-workspace/.claude/scripts/autosync-push.sh",
               "timeout": 60,
               "async": true
             }
           ]
         }
       ]
     }
   }
   ```

   Remplace `/CHEMIN/ABSOLU/VERS/ton-workspace` par le chemin réel (ex. fais `pwd` depuis la racine du workspace pour l'obtenir).

3. Dans Claude Code, tape `/hooks` une fois pour recharger la config (ou ferme/relance Claude Code).

4. Vérifie que les hooks fonctionnent après quelques tours :

   ```bash
   tail -f ~/Library/Logs/$(basename "$PWD")-autosync.log
   ```

   Tu dois voir des entrées `Stop push: N files` (auto-commit) ou `SessionStart pull` (auto-pull).

### Désactiver

- Soit `/hooks` dans Claude Code, retire les hooks
- Soit supprime la section `"hooks"` de `.claude/settings.local.json`
- Soit supprime le fichier complet pour repartir à zéro

### Limites à connaître

- Les hooks `Stop` ne fire **que** quand tu travailles avec Claude Code. Une édition manuelle dans Cursor / un IDE / le Finder n'est pas pushée immédiatement. Elle sera capturée au **prochain `Stop`** (au premier tour Claude suivant) puisque `git add -A` ramasse tout l'état dirty.
- Pas de relecture humaine avant push : une boulette part en quelques secondes sur GitHub. Le `.gitignore` du template bloque déjà `.env`, secrets, `node_modules/` ; les protections du script blo­quent les fichiers > 10 MB. Mais ça reste un push automatique, pas un workflow de PR.
- Historique git plus bruité (commits `auto: <timestamp> (N files)`). Si tu veux un historique propre pour publier ce repo, préfère du commit manuel.

### Pour le téléphone

- **GitHub Mobile** (gratuit, iOS/Android) : lecture des `.md` partout
- **Working Copy** (iOS, ~22€) : clone + édition + commit depuis le téléphone

Avec l'auto-pull au `SessionStart`, toute modif faite depuis le téléphone est récupérée à la prochaine session Claude.

---

## Prérequis

- [Cursor](https://cursor.sh) et/ou **Claude Code**
- Clone de **[uccellolabs/Offer-Pipeline](https://github.com/uccellolabs/Offer-Pipeline)** puis exécution de `bash install-skills.sh` (voir [README](https://github.com/uccellolabs/Offer-Pipeline/blob/main/README.md))
