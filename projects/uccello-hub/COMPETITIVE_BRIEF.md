# COMPETITIVE_BRIEF.md
- Date : 2026-04-25 | Version : 1.0 | Agent : competitive-intel

---

## Cartographie

### Concurrents directs (même problème, même cible)
1. **ProSuite** — programme partenaire IA PME, même modèle de distribution indirect
2. **Ne rien faire / Excel** — option par défaut de la majorité des PME françaises

### Concurrents indirects (même budget ou problème, approche différente)
3. **Microsoft Copilot Business** — IA dans les apps M365, ~19.70€/user/mois
4. **Make.com** — automatisation cloud visuelle, 100% SaaS, 9-550€/mois
5. **n8n self-hosted** — open source souverain, mais technique
6. **Eliott Menier / "second cerveau IA"** — formation plutôt que produit, prescripteur potentiel

---

## Fiches concurrents directs

### 1. ProSuite (activia.pro)

**Identité**
- Fondateur : Nicolas Korboulewsky
- Positionnement : "Transformez votre expertise en revenus récurrents SaaS métier avec IA"
- Modèle : consultant/agence → devient revendeur d'applications métier IA pour PME
- Actif en 2026, réseau "Activ IA by ProSuite" — 1ère année de déploiement

**Forces réelles**
- Même cible exacte que Uccello Hub (consultants indépendants, agences)
- Messaging fort sur MRR et sortie du "festin ou famine" — copie exacte de la douleur de Marc
- Formule Distribution GRATUITE (zéro coût entrée) — barrière très basse
- Simulateur ROI publié (3 500€ setup + 350€/mois → marge 50%) — très rassurant pour le revendeur
- Formation Builder 3 jours incluse

**Faiblesses documentées**
- ProSuite permet de CRÉER des applications métier from scratch (builder no-code) — ce n'est pas un hub de centralisation de données existantes (source : lecture de la page officielle)
- Aucune mention de souveraineté des données, d'hébergement on-premise ou de modèles open source
- L'IA est "neuro-symbolique" sur leurs serveurs — pas de souveraineté par design
- Les applications créées sont des nouveaux outils, pas une interconnexion des outils déjà en place
- Communauté encore jeune (Année 1) — peu de références clients publiques

**Pricing**
- Distribution : GRATUIT (revendeur au prix catalogue + marge)
- Accompagnement : 490€/mois + 1 720€ setup unique + 50% de réduction sur tout

**Adresse du persona Marc**
✅ Douleur MRR adressée directement / ❌ Ne résout pas la douleur souveraineté / ❌ Ne centralise pas les données existantes

---

### 2. Microsoft Copilot Business

**Identité**
- Éditeur : Microsoft
- Positionnement : IA dans les apps M365 (Word, Excel, Outlook, Teams)
- Tarif : ~19.70€/user/mois (jusqu'à 300 utilisateurs) — baissé en décembre 2025
- Copilot Chat inclus sans surcoût pour abonnés M365 éligibles

**Forces réelles**
- Marque de confiance absolue — aucun DSI n'a jamais été licencié pour avoir choisi Microsoft
- Déjà dans l'environnement de travail (M365 est souvent déjà payé)
- Progressif : Copilot Chat gratuit → Copilot Business payant → Agents Azure
- Gestion des identités et droits d'accès via Microsoft Entra

**Faiblesses documentées**
- Données traitées sur cloud Microsoft (Azure/AWS) — soumises au CLOUD Act américain (source : planetewebmaster.com 2026)
- Limité à l'écosystème M365 — ne synchronise pas HubSpot, Notion, Monday, Pipedrive, etc.
- Pas de sync temps réel avec les outils tiers non-Microsoft
- ROI difficile à mesurer : "la plupart des clients en sont encore à des projets pilotes" (source : Le Monde Informatique)
- Gouvernance complexe : droits, classification, Azure requis pour les agents
- Pour une agence 12 personnes à 19.70€/user = ~236€/mois mais sans connexion aux outils métier

**Pricing**
- Copilot Chat : inclus (M365 éligible)
- Copilot Business : ~19.70€/user/mois annuel
- Agents : Azure à la consommation (coût variable non maîtrisable)

**Adresse du persona Claire**
⚠️ Partiellement — couvre les apps M365 mais pas les autres outils / ❌ Souveraineté compromise / ❌ Pas de sync temps réel inter-outils

---

### 3. Make.com

**Identité**
- Éditeur : Make (ex-Integromat), fondé 2012, basé en République tchèque
- Positionnement : automatisation visuelle no-code, 1 500+ connecteurs
- Public : PME, marketeurs, équipes non-techniques

**Forces réelles**
- Interface la plus intuitive du marché — premier scénario en 30 minutes
- 1 500+ connecteurs natifs — couverture maximale des apps SaaS
- Très populaire en France — forte communauté et ressources francophones
- Prisé par les consultants type Marc (qui l'utilisent déjà)

**Faiblesses documentées**
- 100% cloud — aucune option self-hosted, données sur serveurs Make (AWS US possible) — risque CLOUD Act (source : maketime.fr 2026)
- Coût variable : basculé sur système de "Crédits" en 2025 — hausse déguisée pour utilisateurs avancés, jusqu'à 550€/mois pour une agence (source : planetewebmaster.com)
- Pas d'interface chat pour les utilisateurs finaux — Marc doit construire et maintenir les flux
- Aucune centralisation des données — chaque automatisation est un flux isolé
- Nécessite un technicien pour créer et maintenir — pas autonome côté client final
- Timeout 40 minutes sur plan Pro — limitations opérationnelles

**Pricing**
- Core : 9€/mois (2 000 opérations)
- Pro : ~16€/mois + crédits supplémentaires
- Agence usage intensif : 300-550€/mois

**Adresse du persona Marc**
⚠️ Marc l'utilise déjà mais il ne peut pas le revendre facilement — pas un produit packagé / ❌ Souveraineté compromise

---

### 4. n8n self-hosted

**Identité**
- Open source (fair-code), lancé 2019
- Positionnement : automatisation flexible, self-hosted ou cloud, agents IA natifs
- Public : développeurs, équipes techniques, entreprises avec exigences sécurité

**Forces réelles**
- Souveraineté totale en self-hosted — données sur infrastructure propre, RGPD natif (source : bradroit-solutions.fr)
- Coût fixe prévisible (~15€/mois VPS) pour volumes illimités
- Agents IA natifs (LangChain, Ollama, OpenAI) — intégration IA avancée
- ~400 connecteurs natifs + personnalisation totale (code Node.js)

**Faiblesses documentées**
- Courbe d'apprentissage réelle — pas accessible à un utilisateur non-technique (source : maketime.fr, automatisation-intelligence-artificielle.fr)
- Nécessite installation, maintenance, mises à jour Docker — charge technique
- Pas d'interface chat clé-en-main pour utilisateurs finaux
- Pas de centralisation des données — flux isolés, pas de hub unifié
- Marc devrait installer et maintenir lui-même l'infrastructure de chaque client

**Pricing**
- Self-hosted : ~5-15€/mois (VPS uniquement)
- Cloud : 20€/mois + frais exécutions

**Adresse du persona Marc**
❌ Trop technique pour Marc comme produit à revendre / ✅ Souveraineté / ❌ Pas un produit packagé

---

### 5. Ne rien faire / Excel

**Réalité terrain**
La majorité des PME françaises (74% n'investissent rien ou moins de 1 000€/an dans le numérique — France Num 2025) gèrent leurs données manuellement via Excel, emails et des outils non connectés.

**Pourquoi c'est dangereux à ignorer**
- C'est le concurrent N°1 en volume
- Le coût de l'inaction est invisible : 1 mois/an de travail perdu (exemple agence immo)
- Sans urgence perçue, il n'y a pas de décision d'achat

**Comment le traiter**
Rendre le coût de l'inaction visible et chiffré dès la première conversation : "Combien d'heures par semaine vos équipes passent-elles à ressaisir des données ?"

---

## Matrice de positionnement

Critères basés sur les valeurs de Marc (souveraineté, MRR, déployable sans dev) et Claire (souveraineté, déploiement rapide, ROI mesurable) :

| Critère | Uccello Hub | ProSuite | Microsoft Copilot | Make.com | n8n | Rien faire |
|---------|-------------|----------|-------------------|----------|-----|------------|
| Souveraineté données (on-premise) | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ (pas de données partagées) |
| Sync temps réel tous outils | ✅ | ❌ | ❌ (M365 only) | ⚠️ (flux isolés) | ⚠️ (flux isolés) | ❌ |
| Chat IA contextuel par collaborateur | ✅ | ❌ | ⚠️ (M365 only) | ❌ | ❌ | ❌ |
| Déployable par consultant non-dev | ✅ | ✅ | ⚠️ | ⚠️ | ❌ | ✅ |
| Modèle MRR revendeur clé-en-main | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| ROI mesurable dès semaine 1 | ✅ | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| Coût d'entrée revendeur | ~3 000€ | Gratuit→490€ | N/A | N/A | N/A | 0€ |

---

## Positionnement différenciant

**Zone gagnée : la seule solution qui combine souveraineté + hub centralisé + IA chat + modèle revendeur clé-en-main**

ProSuite adresse la même douleur de Marc (MRR) mais construit des apps from scratch sans souveraineté.
Microsoft Copilot adresse l'IA mais reste dans M365 et envoie les données aux USA.
Make/n8n automatisent mais nécessitent un technicien et ne centralisent pas.
Personne ne combine les quatre piliers simultanément.

**Phrase de positionnement :**
"Contrairement à Microsoft Copilot (limité à M365, données aux USA) ou Make (technicien requis, données hors UE), Uccello Hub est le seul hub IA souverain clé-en-main qui centralise TOUS vos outils en temps réel et donne à chaque collaborateur une IA contextuelle depuis un chat — déployé en 1 journée par votre consultant, sans que vos données ne quittent jamais votre infrastructure."

**3 arguments non-comparables :**
1. **Souveraineté par design** — modèles IA open source hébergés on-premise, aucune donnée ne sort de l'infrastructure cliente
2. **Chat contextuel avec droits d'accès** — chaque collaborateur interroge l'IA selon ses droits, depuis un chat unifié (dashboard, mails, RDV, requêtes...)
3. **Modèle revendeur packagé** — le consultant deploie en 1 journée, assure le support N1, facture un abonnement mensuel à son client sans jamais revenir vers l'éditeur

**Angles morts (où les concurrents sont meilleurs)**
- **Notoriété** : Microsoft écrase en crédibilité institutionnelle → Reframing : "Nos clients choisissent Uccello Hub précisément parce que ce n'est pas Microsoft — leurs données restent chez eux."
- **Volume de connecteurs** : Make a 1 500+ connecteurs vs Uccello Hub qui ajoute ~24h par connecteur → Reframing : "Nous priorisons les connecteurs de vos outils réels — chaque connecteur est fait sur mesure pour votre stack, pas un template générique."
- **Coût d'entrée ProSuite** : ProSuite propose une formule Distribution GRATUITE → Reframing : "Uccello Hub est un vrai produit technique avec hébergement souverain — l'investissement couvre l'infrastructure et la formation, pas juste un accès à un builder."

---

## Battlecards

```
CONCURRENT : ProSuite
QUAND IL APPARAÎT : Quand Marc compare les programmes partenaires revendeur IA PME
SON MESSAGING : "Transformez votre expertise en revenus récurrents sans développement"
POURQUOI LE PROSPECT LE CONSIDÈRE : Formule Distribution gratuite, simulateur ROI rassurant, même discours MRR
COMMENT RÉPONDRE : "ProSuite vous permet de construire des applications from scratch pour vos clients.
Uccello Hub centralise les outils qu'ils ont déjà et leur donne une IA sur leurs propres données.
Ce sont deux approches complémentaires, pas les mêmes clients."
QUESTION QUI FAIT RÉFLÉCHIR : "Vos clients veulent-ils un nouvel outil à apprendre, ou une IA sur leurs données actuelles ?"
ARGUMENT DÉCISIF : Souveraineté on-premise — ProSuite héberge sur ses serveurs, Uccello Hub héberge chez le client.
```

```
CONCURRENT : Microsoft Copilot Business
QUAND IL APPARAÎT : Quand Claire compare les solutions IA pour son agence
SON MESSAGING : "L'IA dans vos apps Microsoft, sécurisée, pour les PME"
POURQUOI LE PROSPECT LE CONSIDÈRE : Marque de confiance, déjà dans l'environnement M365, prix réduit à 19.70€/user
COMMENT RÉPONDRE : "Microsoft Copilot est excellent dans M365. Mais vos données passent quand même
par des serveurs américains soumis au CLOUD Act. Et HubSpot, Notion, Monday —
vos vrais outils métier — Copilot ne les connaît pas."
QUESTION QUI FAIT RÉFLÉCHIR : "Quand votre équipe cherche une information sur un client, elle cherche dans Outlook ou dans HubSpot ?"
ARGUMENT DÉCISIF : Sync temps réel de TOUS les outils + données hébergées sur votre infrastructure, pas chez Microsoft.
```

```
CONCURRENT : Make.com
QUAND IL APPARAÎT : Quand Marc propose déjà Make à ses clients ou quand Claire a entendu parler de l'automatisation
SON MESSAGING : "Automatisez tout sans coder, 1 500 connecteurs"
POURQUOI LE PROSPECT LE CONSIDÈRE : Interface simple, très connu, connecteurs nombreux
COMMENT RÉPONDRE : "Make est excellent pour automatiser des flux ponctuels.
Uccello Hub centralise les données et donne à chaque collaborateur une IA contextuelle depuis un chat.
Ce n'est pas la même chose qu'une automatisation — c'est un hub de connaissance vivant."
QUESTION QUI FAIT RÉFLÉCHIR : "Quand votre équipe pose une question sur un client, qui répond — Make ou un collaborateur qui cherche dans 5 outils ?"
ARGUMENT DÉCISIF : Données hébergées sur votre infrastructure (CLOUD Act inapplicable) + interface chat unifiée vs flux isolés.
```

```
CONCURRENT : Ne rien faire
QUAND IL APPARAÎT : Toujours — c'est la décision par défaut
SON MESSAGING : "On gère avec ce qu'on a"
POURQUOI LE PROSPECT LE CONSIDÈRE : Aucun coût apparent, aucun risque de projet raté
COMMENT RÉPONDRE : Sans dénigrer : "Je comprends — un nouveau projet ça prend du temps.
Avant qu'on en parle, une question : combien d'heures par semaine vos équipes passent-elles
à chercher une information dans vos outils ?"
QUESTION QUI FAIT RÉFLÉCHIR : "Si vous récupériez 1 heure par collaborateur et par jour, qu'est-ce que vous en feriez ?"
ARGUMENT DÉCISIF : Rendre le coût de l'inaction visible et chiffré — exemple : 1 mois/an de travail perdu sur les attestations d'assurance seules.
```

---

## Utilisation pipeline

- **/pricing** → Le coût d'entrée 3 000€ est à challenger face à ProSuite gratuit — justifier ou revoir
- **/pricing** → La marge revendeur doit être suffisamment attractive vs ProSuite (50% de marge SaaS)
- **/offer-final** → Utiliser la phrase de positionnement + les battlecards dans le pitch
- **/pitch-deck** → Slide concurrence : matrice de positionnement + phrase différenciante
