# PERSONA_ACHETEUR_DIY.md — Marc & Hélène (Do It Yourself)
- Date : 2026-05-06 | Version : 1.0 | Agent : persona (re-run pour gamme 3 portes)
- Projet : market-study
- Archétype : **DIY** — n'achète pas un livrable, achète l'**outil** + son installation
- Pendant : `PERSONA_ACHETEUR_DFY.md` (Julien)

---

## Pourquoi 2 sous-personas dans un même fichier DIY ?

Le DIY recouvre **deux comportements d'achat radicalement différents** :

| Dimension | **Marc** (DIY-Solo) | **Hélène** (DIY-Studio) |
|-----------|---------------------|--------------------------|
| Statut | Freelance / consultant solo | Direction d'un cabinet ou agence |
| Décide | Seul, sur ses revenus | Avec une chaîne (Direction + IT + Ops) |
| Mobile | Autonomie + souveraineté | ROI consultants + souveraineté data |
| Budget | 2-5 k€ | 8-25 k€ + custom |
| Cycle | 14-30 jours | 60-180 jours |

→ Deux messages marketing distincts, deux scripts de vente distincts, deux séquences de prospection
distinctes. Ils sont groupés dans le même fichier parce qu'ils achètent la **même offre backend**
(Pipeline Solo / Pipeline Studio) — mais ils ne se ressemblent pas.

---

# PARTIE A — Marc (DIY freelance / consultant senior)

## A.1 Synthèse express

```
Qui       : Consultant senior / freelance power user IA, 38-50 ans, 12-25 ans d'expérience
Veut      : Son propre pipeline IA installé chez lui pour industrialiser sa pratique
            ou monter une offre packagée pour ses propres clients
Bloqué par: Setups maison ChatGPT/n8n bricolés instables + refus du SaaS opaque
Budget max: 3 000-5 000€ pour un setup pro qui marche dès vendredi
Objection : "Pourquoi payer Jonathan plutôt que monter le setup moi-même en 80h ?"
            "Et si Anthropic change ses prix demain ?"
```

---

## A.2 Canaux d'acquisition

```
### Canaux directs
- LinkedIn :
  * Titre : "Consultant en stratégie / transformation / ops + AI" — varie
  * Tags : "AI for consultants", "indie consultant", "souveraineté IA"
  * Volume FR : 25 000-40 000 profils correspondants (LinkedIn search)
  * Filtre comportemental : poste sur stack IA, partage articles n8n/Make/Claude,
    commente sur la souveraineté, suit Indie Hackers

- Communautés et forums :
  * Indie Hackers FR (Discord, ~3 000 membres)
  * Slack "AI for solopreneurs" / Maker communities
  * NoCode FR (Slack ~5 000 membres) — power users no-code/IA
  * ProductHunt commenters / makers FR
  * Hacker News (commentaires souveraineté IA, anti-SaaS)
  * Reddit r/ChatGPTPro, r/ClaudeAI, r/LocalLLaMA (segment souveraineté)

- Contenu consommé :
  * Newsletters : Ben's Bites, AI Tool Report, Practical AI
  * Newsletters FR : Génération IA, Le Brief IA
  * Podcasts : Lex Fridman, Latent Space, Dwarkesh Patel
  * YouTube : démos n8n, Claude Code, Make.com advanced

### Prescripteurs / intermédiaires
- Communautés de consultants seniors (Coiffeurs Conseil, RéseauPotentiel, Réseau Entreprendre)
- Coachs de cabinets / formateurs IA pour consultants
- Anciens collègues en ESN/cabinet qui sont passés freelance

### Score prospectabilité Marc
Accessibilité : 4/5 (LinkedIn + communautés tech mais cible plus dispersée que Julien)
Volume        : 3/5 (segment niche : 25-40k profils)
Score         : 7/10
Signal        : ✅ Prospectable mais cible plus exigeante
```

---

## A.3 Profil détaillé

| Dimension | Contenu |
|-----------|---------|
| **Nom & âge** | Marc, 44 ans |
| **Rôle** | Consultant freelance senior — stratégie, ops, transformation, AI advisory |
| **Localisation** | Paris, Lyon, Bordeaux, Lille — ou télétravail full |
| **Revenus actuels** | 12 000 - 22 000€/mois HT (variable) |
| **TJM** | 1 000-1 500€/jour |
| **Ancienneté freelance** | 4-12 ans |
| **Clients actuels** | 3-6 clients en parallèle, missions 2-6 mois, scale-ups + ETI |
| **Canaux utilisés** | Réseau pro + LinkedIn organique + recommandations |
| **Stack IA actuelle** | Claude Pro/Code + ChatGPT Plus + Cursor + Make/n8n bricolé + Notion |
| **Frustrations principales** | Ses prompts/workflows sont éparpillés, perte de temps à recommencer chaque mission, dépendance perçue à OpenAI/Anthropic mal cadrée |
| **Désirs** | Industrialiser sa propre pratique IA pour livrer 2-3x plus vite, monter une offre packagée IA-augmentée pour ses clients |
| **Comportement d'achat** | Compare techniquement, demande des démos, lit les CGU, méfiant des outils flashy |

---

## A.4 Want, Objectif, Fantasme, Situation actuelle

**Want (ce qu'il dit vouloir) :**
"Mon propre stack IA propre, qui ne dépend pas d'un SaaS qui peut me lâcher demain."

**Objectif réel :**
Avoir un pipeline professionnel installé chez lui, qu'il maîtrise, qu'il peut démontrer
à ses clients, et qui le différencie sur le marché du conseil senior.

**Fantasme (vision à 12 mois) :**
Marc a un setup pipeline IA opérationnel, il livre ses missions client en 50% du temps qu'avant,
il a packagé une offre "stratégie IA-augmentée" qu'il vend 8-15k€ à ses propres clients.
Il commence à recevoir des demandes de cabinets qui veulent l'embaucher comme expert IA externe.

**Situation actuelle :**
Marc bricole depuis 18 mois un setup ChatGPT custom + n8n. Ça marche à 70%. Il a essayé
quelques GPTs custom, il a regardé ChatGPT Enterprise pour son use case mais il ne veut pas
mettre les données de ses clients dans un environnement opaque. Il a vu passer des stacks
sur Indie Hackers, il a presque acheté un cours "AI for consultants" à 1500€ mais il s'est
rendu compte que c'était de la formation pas un outil. Il veut payer pour avoir l'outil
opérationnel chez lui — pas pour apprendre à le construire.

---

## A.5 Incarnation (1ère personne)

**Douleurs :**
"J'ai passé 80h sur 6 mois à essayer de monter mon stack. Ça marche mais c'est fragile.
Quand un client me demande une étude marché complète, je remplis 5 prompts à la main, je
recopie dans Notion, je reformate. Le temps que je gagne avec l'IA, je le perds en
plomberie."

**Frustrations :**
"Tous les outils 'AI for consultants' que je vois, c'est soit du SaaS qui voit mes données
clients, soit du contenu/formation pour m'apprendre à faire. Je sais déjà faire — je veux
qu'on me le livre opérationnel."

**Anecdote :**
"L'an dernier j'ai acheté un cours 'Build Your Own AI Stack' à 1 290€. J'ai fini les
modules à moitié. Le formateur disait 'maintenant à toi de l'adapter à ton métier'. C'est
exactement ce que je voulais éviter."

**Anxiétés :**
"Si Anthropic ferme demain ou triple ses prix, je fais quoi ? Si OpenAI sort GPT-5 dans
3 mois et que mes prompts cassent, je recommence ?"

**Problèmes tus :**
"Je vends de l'IA à mes clients, mais en fait mon setup est branlant. Si un client me
demandait de voir comment je travaille, j'aurais un peu honte de mon Notion."

---

## A.6 Journal intime (~400 mots)

*Mardi soir, 23h.*

J'ai relancé mon setup pour la mission Stellar. Le workflow Make qui devait orchestrer
les 4 prompts de l'analyse concurrentielle m'a lâché à la troisième étape. J'ai recodé
en Python, Claude m'a aidé, ça marche maintenant. Mais c'est de la rustine. J'ai 3 missions
en parallèle, je peux pas continuer comme ça.

J'ai vu le post de Jonathan SARDO sur LinkedIn la semaine dernière. Il parle d'un pipeline
de création d'offres B2B qu'il a construit pour son propre usage. Il l'utilise pour tester
des idées d'offres. Ça m'a tilté parce que c'est exactement le problème que j'ai sur Stellar :
ils veulent que je leur cadre 3 nouvelles offres en 4 semaines. À l'ancienne ça me prend
2 semaines pour bien faire une seule.

Je me suis dit : si je pouvais avoir SON pipeline chez moi, installé, opérationnel, même
en y collant ma terminologie cabinet et mes templates — je ferais Stellar en 5 jours au
lieu de 4 semaines.

Je l'ai checké. 21 ans de dev, fondateur d'Uccello Labs. Pas un coach LinkedIn. Un mec qui
construit. Je commence à me demander si je peux pas lui acheter le truc directement.

Le souci : je veux pas un SaaS. Je veux pas que mes prompts, mes données clients, mes
analyses de marché passent par un serveur qui m'appartient pas. Je veux ça chez MOI. Sur
ma machine. Que je puisse débrancher l'internet et que ça marche.

Et je veux pas une formation en 12 modules. Je sais déjà faire — j'ai juste pas le temps,
et je veux pas réinventer ce que quelqu'un a déjà bien construit.

Je vais lui envoyer un message demain. Question simple : est-ce qu'il vend l'install ?
Combien ? Est-ce qu'il peut connecter à mon Notion / Hubspot / mon Drive ? Est-ce que
si Anthropic change un truc demain, c'est lui qui me remet d'aplomb ou je dois recoder ?

Si la réponse tient en 3 jours, je signe.

---

## A.7 Solutions rêvées + budget Marc

**Solution rêvée :**
"Quelqu'un qui vient (en visio, peu importe), installe le pipeline sur ma machine,
me le démontre sur un cas client réel, me passe la doc, et est joignable pendant 30 jours
si un truc ne marche pas. Au-delà, je m'en sors seul."

**Alternatives déjà envisagées (et pourquoi non) :**
- Setup maison : "essayé 18 mois, fragile"
- Cours / formation : "je veux pas apprendre, je veux l'outil"
- ChatGPT Enterprise : "données clients dans un cloud opaque, je signe pas"
- Embaucher un freelance n8n : "ils savent faire des workflows, pas un pipeline métier"

**Budget max Marc :** 3 000-5 000€ pour un setup pro + 30 jours de support.
Au-delà, soit la mission est pro (cabinet → ticket plus haut), soit ça rentre dans
le cadre d'un contrat de support annuel à part.

---

## A.8 Objections Marc + réponses

| Objection | Réponse à préparer |
|-----------|-------------------|
| "Pourquoi pas le faire moi-même en 80h ?" | "Tu peux. Tu as essayé 18 mois. Tu peux racheter ce temps pour 3 000€, ou le mettre sur 3 missions client à 1 200€/jour." |
| "Et si Anthropic change ses CGU / prix ?" | "Les skills sont open. Tu maintiens le pipeline en interne. Le contrat de support annuel (590€/an) couvre les mises à jour si l'API évolue." |
| "Pourquoi pas un setup n8n générique ?" | "n8n c'est l'orchestration. Le pipeline c'est la méthodologie + les prompts éprouvés. Tu peux les recoder, mais 2 ans de raffinage en production t'arrivent en 5 jours." |
| "Et si je veux le revendre à mes clients ?" | "C'est explicitement autorisé pour ton usage solo. Si tu veux installer chez tes clients, il faut une licence revendeur (clause séparée)." |
| "3 000€ c'est cher pour un setup" | "C'est le prix de 2,5 jours de mission à ton TJM. 1 mission gagnée par mois grâce à la rapidité = ROI 5x." |

---

# PARTIE B — Hélène (DIY agence / cabinet)

## B.1 Synthèse express Hélène

```
Qui       : Direction stratégie / innovation / ops dans un cabinet conseil ou agence
            5-30 consultants, 40-55 ans, 15-25 ans d'expérience
Veut      : Industrialiser la production d'offres / propositions / études marché clients
            avec un outil interne souverain connecté à leur CRM
Bloqué par: Outils SaaS opaques pour data clients + Big4 IA hors budget +
            consultants seniors qui passent 40% de leur temps en tâches répétitives
Budget max: 8 000-25 000€ setup + 2-5k€/an maintenance + custom selon scope
Objection : "Pourquoi pas développer en interne avec notre dev senior ?"
            "Et si on change d'éditeur d'IA dans 2 ans ?"
```

---

## B.2 Canaux d'acquisition

```
### Canaux directs
- LinkedIn :
  * Titre cible : "Directeur(rice) Strategy / Innovation / Operations / Consulting"
                 dans cabinet 5-30 personnes
  * Mots-clés profil : "strategy consulting", "transformation", "operations excellence"
  * Volume FR : ~3 000-5 000 profils dirigeants cabinets cibles
  * Filtre comportemental : engage avec contenu "AI in consulting", suit Bain/BCG/McKinsey
    sur l'IA, partage des articles Cigref/France Stratégie

- Réseau pro / introductions :
  * Le canal #1 — entrée par recommandation ou ancien collègue
  * Anciens cadres ESN/cabinet qui connaissent Jonathan
  * Communautés de DG cabinets (Syntec, AFCM, France Conseil)

- Contenu consommé :
  * HBR, McKinsey Quarterly, BCG Henderson, Cigref publications
  * Newsletters : Lenny's Newsletter, Stratechery, Sifted (FR)
  * Podcasts : Génération Do It, La Story du Conseil, Open IA Cigref

- Events :
  * Salon / conférences : Big Data & AI Paris, Transform / Stratégie Digitale,
    AI Mastery Day, Cigref Symposium

### Prescripteurs
- Cabinets d'avocats spécialisés tech / IA (KGA, August Debouzy)
- Cabinets RH/transformation (Mercer, Korn Ferry)
- DG ESN à taille humaine (entrent en relation avec leurs propres clients-cabinets)
- Réseaux DG : APM, Réseau Entreprendre, Croissance Plus

### Score prospectabilité Hélène
Accessibilité : 3/5 (cible exigeante, accessible via réseau et événements)
Volume        : 3/5 (segment niche : 1 500-2 500 cabinets cibles)
Score         : 6/10
Signal        : ⚠️ Prospectable mais long cycle — idéal après preuve sociale DFY
```

---

## B.3 Profil détaillé Hélène

| Dimension | Contenu |
|-----------|---------|
| **Nom & âge** | Hélène, 47 ans |
| **Rôle** | Directrice associée / COO / Head of Innovation dans cabinet 5-30 consultants |
| **Type cabinet** | Conseil stratégie B2B, agence stratégie marketing, studio innovation produit |
| **CA cabinet** | 1,5 - 12 M€ |
| **Effectif** | 5-30 consultants seniors + 2-5 supports |
| **Pricing cabinet** | TJM 1 000-1 800€, missions 30-150 k€ |
| **Stack actuelle** | Hubspot ou Salesforce, Notion ou Confluence, Slack/Teams, Office 365, parfois Pipedrive |
| **Initiatives IA déjà engagées** | ChatGPT Enterprise testé, formation IA équipe (1-2 jours), GPT custom internes mis sur étagère car "pas industriel" |
| **Frustrations principales** | Consultants seniors passent 30-40% du temps à structurer offres/propositions/études — coût caché énorme |
| **Désirs** | Outil interne, souverain, qui s'intègre au CRM existant, formation rapide de l'équipe, ROI mesurable |
| **Comportement d'achat** | Achat consultatif — discovery 1-2 calls, demande de POC ou démo, validation IT, comité de direction |

---

## B.4 Want, Objectif, Fantasme, Situation Hélène

**Want (ce qu'elle dit vouloir) :**
"Un outil interne IA pour nos consultants, qui s'intègre à notre Hubspot, qui ne mette pas
nos données clients dans un cloud opaque."

**Objectif réel :**
Récupérer 2 jours/consultant/mission sur les phases répétitives (cadrage, recherche, structuration)
pour libérer du temps facturable à plus haute valeur — ou augmenter la marge à isoCA.

**Fantasme (vision à 18 mois) :**
Le cabinet a un outil pipeline interne dont parlent les concurrents. Les consultants livrent
des cadrages d'offres B2B en 2 jours au lieu de 5. Le cabinet a remporté 2 deals importants
sur la promesse "on a une stack IA souveraine". Hélène est passée d'une initiative IA "test"
à une vraie capacité différenciante. Elle peut le pitcher au comex.

**Situation actuelle :**
Hélène a engagé une initiative IA il y a 12 mois. Elle a fait tester ChatGPT Enterprise à
3 consultants, formé 8 personnes 1 jour avec un consultant externe, lancé 2-3 GPTs internes
qui marchent à 50%. Elle voit que l'IA est un sujet, mais elle n'a pas réussi à passer du
gadget au levier industriel. Elle a vu Capgemini Invent et Onepoint sur des projets IA cabinet,
les devis sont à 80-200k€ — hors budget. Elle cherche un acteur sénior, agile, qui parle
opérationnel et qui ne lui vend pas un projet de transformation à 6 mois.

---

## B.5 Incarnation (1ère personne) Hélène

**Douleurs :**
"On a 12 consultants seniors qui passent un tiers de leur temps à structurer des cadrages,
des notes de positionnement, des études marché qu'on a faites 50 fois. Mes meilleurs profils
font 80% leur valeur ajoutée sur les 20% finaux — mais on ne leur achète pas le temps des 80%."

**Frustrations :**
"On a fait passer la formation IA, on a payé un consultant externe, on a lancé 3 GPTs custom.
Tout le monde dit 'c'est super', personne ne l'utilise vraiment. On n'arrive pas à faire passer
ça en outil quotidien."

**Anecdote :**
"L'an dernier j'ai eu un devis Capgemini Invent à 180k€ pour un 'AI Assistant for Consultants'.
Le scope était énorme, le délai 9 mois. J'ai dit non. J'ai gardé le besoin sous le coude.
Si je trouve un acteur qui me livre un truc opérationnel en 2 mois pour 15-20k€, je signe."

**Anxiétés :**
"Si on choisit la mauvaise stack et qu'on en sort dans 18 mois, je me suis fait griller. Et
si on continue à ne rien faire, on prend du retard sur les cabinets qui ont déjà bougé."

**Problèmes tus :**
"Mes consultants seniors sont en surcharge. Si on ne les outille pas, certains vont partir.
Et notre marge se dégrade parce que les missions prennent trop de temps."

---

## B.6 Journal intime (~400 mots) Hélène

*Mardi 21h, sur le canapé après la réunion projet.*

J'ai relu le compte-rendu de la réunion stratégie de 17h. Cinq sujets sur la table, et quatre
d'entre eux contenaient le mot "IA" — et aucun ne donnait le sentiment d'avancer vraiment.

L'initiative ChatGPT Enterprise lancée en septembre, on en est où ? À une utilisation moyenne
de 2-3 prompts/semaine/consultant. Autant dire rien. Le coach formateur est venu, a fait son
job, est reparti. Les GPTs custom qu'on a lancés en novembre — Damien et Sophie les utilisent,
les autres non. Pourquoi ? Parce que c'est gadget. Ça aide pour des notes mais pas pour
le cœur du métier : structurer un cadrage d'offre B2B, faire une étude de marché propre,
construire une note de positionnement.

J'ai vu passer un post LinkedIn d'un mec, Jonathan SARDO, fondateur d'Uccello Labs. Il parle
d'un pipeline IA qu'il a construit pour ses propres offres. Il l'a utilisé en production
2 ans. Profil intéressant : 21 ans de dev, pas un coach LinkedIn, pas un Capgemini.

Ce que je veux n'est pas compliqué. Un outil interne qui prend les phases répétitives de
nos missions de conseil — cadrage, persona, étude marché, concurrence, pricing — et qui les
produit en 1-2 jours au lieu de 5-7. Connecté à notre Hubspot pour pas dupliquer la donnée.
Souverain — pas dans un cloud opaque. Que mes consultants utilisent vraiment.

Le devis Capgemini à 180k€ je l'ai laissé dans un tiroir. C'est un projet de transformation,
pas un outil. Je veux un outil.

Si Jonathan peut me livrer ça en 8-10 semaines pour 12-18k€ + un peu de custom Hubspot,
je signe. La condition : que mes consultants seniors trouvent ça aussi puissant que ce
qu'ils auraient construit eux-mêmes — sinon ils ne l'utiliseront pas.

Je vais demander à Pierre de regarder son profil et son site demain matin.
Et je veux une démo en visio dans les 15 jours, sur un cas réel — pas un PowerPoint.

---

## B.7 Solutions rêvées + budget Hélène

**Solution rêvée :**
"Un acteur sénior, agile, qui me livre en 8-12 semaines un pipeline IA installé chez nous,
connecté à notre Hubspot, formé à 5-10 consultants, et qui reste joignable 60 jours.
Ensuite on est autonomes. On peut signer un contrat de support annuel pour les mises à jour."

**Alternatives écartées :**
- Big4 / Capgemini Invent / Onepoint : "60-180k€, scope énorme, 6-12 mois → non"
- ChatGPT Enterprise : "data sensible, pas industriel"
- Développer en interne : "notre dev IT n'est pas un AI engineer, on perdra 6 mois"
- Continuer avec les GPTs custom : "ça ne décolle pas, faut autre chose"

**Budget Hélène :**
- Setup : 8 000-15 000€ acceptable, idéalement validé en CODIR
- Custom (intégrations Hubspot + Notion par ex) : +2 000-5 000€
- Formation équipe : intégrée ou +1 500€
- Maintenance annuelle : 2 000-4 000€/an raisonnable

→ Total mission type : **12-22 k€**, validable par CODIR sans escalade comex.

---

## B.8 Chaîne de décision Hélène (B2B classique)

| Rôle | Influence | Préoccupation principale |
|------|:---------:|--------------------------|
| **Hélène** (directrice associée / COO) | Décideur économique | ROI consultants + cohérence stratégique |
| **CEO / Managing Partner** | Sponsor | Différenciation marché + investissement raisonnable |
| **CIO / Lead Tech** | Validateur technique | Sécurité, RGPD, intégration Hubspot, dépendance Anthropic |
| **Lead consultant senior** | Utilisateur final | "Est-ce que ça m'aide vraiment ou ça me ralentit ?" |
| **DAF / contrôleur** | Validateur budget | ROI mesurable, prix par rapport au benchmark Big4 |

**Implication vente :**
- Discovery call : 1h avec Hélène
- POC ou démo cas réel : 30-60 min, idéalement avec 1 consultant senior présent
- Réponse FAQ technique : envoi document à Hélène pour CIO
- Validation budget : devis structuré (setup + custom + maintenance), ROI chiffré
- Signature : contrat avec clauses dépendance Anthropic

---

## B.9 Objections Hélène + réponses

| Objection | Réponse à préparer |
|-----------|-------------------|
| "Pourquoi pas notre dev IT en interne ?" | "Vous pouvez. Mais vous payez son temps + 6 mois d'apprentissage. Le pipeline est issu de 2 ans de raffinage en production — vous l'avez en 8-10 semaines, opérationnel." |
| "Et si Anthropic change ses CGU dans 18 mois ?" | "Le pipeline est conçu pour être portable (skills + agents). Le contrat de support annuel inclut la migration si l'API change. Vous n'êtes pas bloqués." |
| "Pourquoi pas Capgemini / Onepoint ?" | "Ils livrent un projet de transformation. Je livre un outil. Délai et budget sont 5-10x différents — et la valeur perçue par vos consultants est très différente." |
| "Comment garantir que mes consultants vont l'utiliser ?" | "Formation 1 demi-journée + adoption checklist sur 30 jours + 2 sessions de revue à J+30 et J+60. Si les consultants ne l'utilisent pas, on ajuste." |
| "12-18k€ c'est cher pour un setup" | "À votre TJM 1 200€, c'est 10-15 jours de mission consultant. Si l'outil libère 1 jour/mois/consultant sur 10 consultants — c'est amorti en 1 mois." |
| "Souveraineté data : où sont stockés les prompts et données ?" | "Sur votre infrastructure. L'API Anthropic est appelée pour la génération mais aucune donnée client n'est stockée chez Uccello. RGPD ok." |

---

## B.10 Reframing en 5 étapes Hélène

1. **Identifier la croyance :** "On peut développer en interne ou attendre que ça mûrisse"
2. **Reconnaître la légitimité :** "C'est vrai, vous avez les ressources techniques"
3. **Pointer la réalité :** "Vous avez engagé l'initiative IA il y a 12 mois et l'usage moyen
   est de 2-3 prompts/semaine. Le problème n'est pas la techno, c'est la mise en production."
4. **Proposer un nouveau cadre :** "Vous n'achetez pas une techno — vous achetez une mise en
   production éprouvée. C'est ce qui transforme un outil en levier."
5. **Ancrer :** "8-10 semaines, opérationnel, vos consultants l'utilisent vraiment.
   Et vous restez propriétaires."

---

## Score Checkpoint viabilité 2 — Prospectabilité (par sous-persona)

```
Marc (DIY freelance)
Accessibilité : 4/5
Volume        : 3/5
Total         : 7/10
Signal        : ✅ Prospectable mais cible exigeante

Hélène (DIY agence)
Accessibilité : 3/5
Volume        : 3/5
Total         : 6/10
Signal        : ⚠️ Prospectable via réseau pro + événements + recommandations
              (cycle long — pas de cold outbound efficace)

Score combiné DIY : 6,5/10 (vs 9/10 pour DFY Julien)
```

**Implications :**
- Le DFY (Julien) reste le **produit d'appel** : c'est le canal LinkedIn massif, prospectable.
- Le DIY (Marc + Hélène) demande des canaux différents : contenu expert long format, réseau pro,
  recommandations, événements ciblés.

---

## Utilisation pipeline aval

- `/market-research v2` : compléter SAM/SOM pour Marc et Hélène (le SAM v1 ne couvrait que Julien)
- `/competitive v2` : ajouter pan SaaS/setup IA (Marc) + Big4 IA cabinet (Hélène)
- `/pricing v2` : modèle DFY (existant) + DIY-Solo (Marc) + DIY-Studio (Hélène) — no SaaS
- `/offer-final v2` : 3 propositions de valeur distinctes, partagent un backend pipeline commun
