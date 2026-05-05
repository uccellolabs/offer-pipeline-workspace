# OFFER_BRIEF.md

- Date : 2026-05-05 | Version : 1.0 | Agent : offer-cadrage | Statut : **GO conditionnel**

## PIPELINE SUMMARY

Idée        : Portail client Mintizy revendu en marque (white-label optionnel) à des intégrateurs ERP français orientés SAV/maintenance, qui l'intègrent à leur ERP via API (à leur charge) et le commercialisent à leurs clients finaux.
Cible       : Intégrateurs ERP français (Cegid XRP Flex, Sage X3, Divalto, Dynamics 365 BC, Odoo Enterprise, Akuiteo, SAP B1) ayant une capacité technique interne et un portefeuille SAV/maintenance, à préciser par /offer-persona et /offer-market-research.
Problème    : Les intégrateurs ERP perdent des deals SAV/maintenance faute d'une brique "portail client professionnel" prête-à-bundler. Leurs clients SAV ont besoin d'exposer leurs interventions à leurs propres clients finaux (transparence, appels d'offres réglementés) sans dev custom.
Valeur      : Pour le revendeur ERP, +30 à 40% de marge sur une brique différenciante sans R&D. Pour le client SAV, portail clé-en-main professionnel à 168 à 420€ HT/mois (vs dev custom 30-80k€ ou portail générique inadapté).
Canal       : **Revendeurs intégrateurs ERP** (modèle B2B2B2C confirmé par /offer-market-research). Focus année 1 : Cegid XRP Flex + Sage X3. Univers cible 50-100 cabinets prioritaires.
Concurrent  : Praxedo (FSM dominant FR, "Portail donneur d'ordres" orienté B2B sous-traitance), Microsoft Dynamics 365 FS Portal (couplé Microsoft uniquement), Sage X3 SAV + portails tiers, Synchroteam (low-cost), Twimm (cible patrimoine immobilier). Mintizy se distingue par : portail B2B2C dédié exposition client final, pricing palier (pas per-user), indépendance ERP, marque blanche optionnelle. Praxedo : complément OU alternative selon le contexte du revendeur, pas un bundle imposé.
Prix cible  : Grille publique Mintizy = grid OCI étendu (120/180/240/300€ HT/mois UCCELLO + remise revendeur 40%) + setup fee 990€ HT par client final perçu par le revendeur + option Quick-Start Passerelle 14 900€ HT (livraison passerelle ERP par UCCELLO) + option white-label 50€/mois ou 4 900€ one-shot.
Verdict     : **VIABLE SOUS CONDITIONS** (4 conditions à activer pour passer à VIABLE FERME, cf. OFFER_FINAL.md)
Pipeline    : Idea : skip (offre déjà signée) | Cadrage : ✅ | Persona : ✅ | Market : ✅ | Competitive : ✅ | Pricing : ✅ | Final : ✅ | Website : ✅ | Statut : DOSSIER COMPLET PRÊT À PRÉSENTER
Prospection : 2026-05-05, vague 1, 100 lignes NAF 62.02A. CSV v3 (Maps + qualif web Cegid) : `PROSPECTS_2026-05-05_integrateurs-erp-naf6202a_v3.csv`. Versions précédentes : `_v2` (Maps), fichier initial sans suffixe. **Liste transversale XRP Flex (30)** : `PROSPECTS_2026-05-05_cegid-xrp-flex-annuaire-presse_gmaps.csv` (preuves A/B/C + API entreprises + Maps).

---

## 1. Idée en une phrase

Le portail client Mintizy aide les intégrateurs ERP français à enrichir leur bundle SAV/maintenance avec une brique "portail client" prête à intégrer (API ouverte) qu'ils revendent en marque Mintizy à leurs propres clients finaux, sans investir en R&D produit.

## 2. Problème résolu

**Principal** : Les intégrateurs ERP qui adressent un marché SAV/maintenance n'ont pas, dans leur ERP cœur, de portail client moderne (transparence interventions, rapports, calendrier, dashboard) à proposer à leurs clients finaux. Sans cette brique, ils perdent des deals face à des concurrents qui bundlent un outil terrain (Praxedo, ClicktoSAV, Mintizy-direct) plus un portail.

**Sans cette offre** : Le revendeur soit développe un portail maison (3 à 12 mois de dev, dette technique à perpétuité), soit oriente le client vers un produit complet concurrent (Praxedo + portail) qui le déloge sur la partie ERP, soit n'adresse pas le besoin et laisse partir le deal.

**Qui souffre le plus (3 niveaux)** :
1. Le revendeur ERP : marge perdue sur un deal mort.
2. L'entreprise SAV cliente : reste sur Excel + emails pour exposer les interventions à ses propres clients, perd des appels d'offres réglementés (cuisine pro avec CERFA, fitness avec preuve d'entretien).
3. Le client final du client (utilisateur du portail) : aucune visibilité sur les interventions sur ses équipements.

## 3. Cible

**Acheteur** (décideur du bundle) : dirigeant ou directeur commercial d'un cabinet d'intégration ERP français de taille moyenne (10 à 80 collaborateurs), avec une practice SAV/maintenance déjà identifiée et une équipe technique capable de dev API. Profil concret : OCI, Eolas (Cegid), intégrateurs Sage X3 type ACG Synergies / Apsia, intégrateurs Divalto, partenaires Dynamics 365 BC type Sygmatec ou Calliope. À préciser par /offer-persona.

**Utilisateur final** (configure et paie le portail) : responsable SAV ou dirigeant d'une PME de maintenance technique (cuisinistes pro, fitness, CVC, ascensoristes, parcs informatiques sur sites distants), 10 à 200 utilisateurs, déjà équipée de l'ERP du revendeur.

**Intermédiaire** : oui, modèle entièrement indirect via revendeur. UCCELLO ne facture jamais le client final.

## 4. Valeur

**Acheteur (revendeur ERP)**
: Brique prête à bundler, marge ~40% (grid OCI), récurrence mensuelle, zéro R&D produit, zéro support N2 à porter, exclusivité territoriale possible (à négocier).

**Utilisateur (entreprise SAV)**
: Portail professionnel sous 48h post-intégration (vs 3 à 12 mois de dev maison), 168 à 420€ HT/mois (vs 30 à 80k€ de dev + maintenance), intégration native à l'ERP existant (pas de double saisie), conformité réglementaire (CERFA, traçabilité), levier appel d'offres.

**Quantifiable estimée** : ROI 6 à 12 mois pour le client final si le portail permet de signer 1 contrat majeur réglementé (cuisine pro, fitness, parc d'équipements). Pour le revendeur, ~67€ à 168€ HT de marge mensuelle par client final, soit ~800 à 2000€/an de marge récurrente sans charge.

## 5. Verdict Devil's Advocate

### ✅ Ce qui tient

1. **Validation empirique réelle** : 4 clients facturés via OCI + 15 en pipeline. Ce n'est pas une hypothèse, c'est une preuve. La douleur existe, le pricing tient, le format "via revendeur" fonctionne. Score douleur 7/10 minimum.
2. **Modèle économique propre** : grid de prix négocié, marge revendeur calibrée, support N1/N2 cloisonné. Pas de bricolage commercial.
3. **Zéro R&D produit** : le portail existe et tourne. Le revendeur fait sa propre passerelle. UCCELLO ajoute des revenus récurrents sans alourdir la roadmap Mintizy.
4. **Effet de levier groupements** : OCI signe Gasel (groupement professionnel multi-membres). Un seul deal commercial peut activer 5 à 20 sociétés. Multiplicateur réel sur l'ARR par revendeur.
5. **Marque Mintizy déjà légitimée** : 1200+ utilisateurs, hébergement France, RGPD, conformité, cas clients (cuisinistes, fitness). Le revendeur ne vend pas une promesse, il vend un produit qui tourne.

### ❌ Ce qui ne tient pas

1. **"Le revendeur fait sa passerelle" filtre brutalement le marché**. Le pré-requis (compétence dev API + bandwidth + volonté d'investir avant le 1er client signé) exclut la majorité des petits cabinets d'intégration (5 à 15 personnes). L'univers cible n'est pas "tous les intégrateurs Sage X3 de France" mais "les intégrateurs Sage X3 disposant d'au moins 1 dev senior pour 2 à 4 semaines de chantier API". À quantifier en /offer-market-research, mais ça réduit probablement de 50 à 70% l'univers initial.
2. **Asymétrie de risque sur le 1er deal** : pour un revendeur, signer le contrat de distribution + dev la passerelle représente ~10 à 30k€ de coût caché avant le 1er euro de revenu. Sans 2 ou 3 prospects fermes côté revendeur, le ROI est incertain. Risque : le revendeur signe et ne se mobilise pas.
3. **Dépendance OCI excessive sur le scénario médian** : si OCI passe à 12 à 20 clients en 12 mois (extrapolation pipeline actuel), il génère seul 60 à 100k€ ARR. C'est l'objectif 12 mois entier. Aucun stress-test sur la diversification.

### ⚠️ Hypothèses non vérifiées

1. **Pourquoi OCI bundle Mintizy + Praxedo simultanément ?** Si Praxedo a déjà un portail, le client paie deux fois. Soit Mintizy résout un cas que Praxedo ne couvre pas (ex : portail propre marque revendeur, ou exposition à des clients finaux non-techniciens), soit OCI sur-vend. À clarifier avant /offer-competitive-intel.
2. **Volumétrie réelle d'intégrateurs ERP français adressables**. Estimation à fournir par /offer-market-research. Si l'univers cible (intégrateurs avec capacité dev + portefeuille SAV) est < 100 acteurs FR, l'objectif "5 à 7 revendeurs / 12 mois" est ambitieux mais pas impossible. Si < 30 acteurs, l'objectif devient critique.
3. **Cycle de vente B2B partenariat sans réseau** : 1,5j/sem de cold outreach par un fondateur sans contacts intégrateurs ERP donne quel ROI ? Hypothèse de travail : 3 à 6 mois pour signer 1 nouveau revendeur. Donc 5 à 7 revendeurs en 12 mois exigent un sourcing très structuré (LinkedIn ciblé, salons CXP / Cegid Connections / Sage Universités, partenariats croisés).
4. **Réaction des éditeurs ERP** : Cegid, Sage, Microsoft peuvent à tout moment développer ou racheter un portail concurrent et fermer le canal. Risque structurel non couvert.

### 🚧 Contraintes projet

- **1,5 j/sem de temps commercial** est la contrainte la plus serrée. C'est ~75 jours/an, soit ~150 prospects en outbound qualifié à 2j par lead. Sur un taux de conversion partenariat B2B de 5 à 10%, ça donne 8 à 15 deals serrés. Réaliste pour atteindre 5 à 7 revendeurs signés mais sans marge d'erreur.
- **Bootstrapped + 0 réseau** : pas de marketing payant, pas de leads chauds. Tout repose sur l'outbound froid + content éventuel + activation d'OCI comme référence.
- **Pas de connecteur ERP côté UCCELLO** : engage le revendeur à porter le coût d'intégration, donc à filtrer les revendeurs sur leur capacité technique.

## 5b. Checkpoint viabilité 1 : Intensité de la douleur

- **Score douleur** : **7/10**
  - Justification : 4 clients facturés OCI + 15 pipeline = douleur prouvée empiriquement. La pression vient de 2 directions : (a) intégrateurs ERP cherchant à différencier leur bundle, (b) entreprises SAV ayant besoin d'un portail pour répondre à des appels d'offres réglementés. Pas 9/10 car la douleur n'est pas "urgente" pour la majorité des intégrateurs ERP français : beaucoup vivent sans, la douleur est latente.
- **Déjà dépensé** : **OUI**
  - Côté client final : oui (Excel, portails maison, abonnements partiels).
  - Côté revendeur : oui (OCI a engagé du dev pour la passerelle Cegid XRP Flex avant le 1er deal, donc willingness to invest prouvée).
- **Signal** : ✅ **Prioritaire** (validation empirique forte, willingness à investir prouvée des 2 côtés).

## 6. Direction recommandée

[X] **GO conditionnel**
[ ] NO-GO
[ ] PIVOT

**Justification** : Le projet est viable et déjà partiellement dérisqué (preuve OCI). Mais 3 conditions doivent être validées avant d'engager 12 mois de prospection à plein régime :

1. **Quantifier l'univers cible** (volume d'intégrateurs ERP français disposant à la fois d'une practice SAV/maintenance ET d'une capacité dev interne). Sortie attendue de /offer-market-research : >50 cibles → GO ferme. 30-50 → GO étroit (focus 2 ERP). <30 → PIVOT vers connecteurs UCCELLO ou vente directe.
2. **Comprendre la coexistence Mintizy + Praxedo dans le bundle OCI**. Si Mintizy = "portail" et Praxedo = "outil terrain technicien", la complémentarité est claire et défendable face à tous les intégrateurs. Si Mintizy chevauche Praxedo, il faut affûter la frontière fonctionnelle. Sortie attendue de /offer-competitive-intel.
3. **Construire un script de sourcing intégrateurs ERP** avec ciblage LinkedIn nominatif et accroche "rejoignez OCI dans la distribution Mintizy". Sortie attendue de /offer-prospection-strategy si lancée.

**Conditions GO ferme** : confirmation des 3 points ci-dessus en pipeline aval. Si /offer-market-research conclut <30 cibles ou /offer-competitive-intel conclut chevauchement Praxedo, retour en cadrage pour PIVOT.

## 7. Questions prioritaires pour /offer-persona

1. **Persona ACHETEUR (intégrateur ERP)** : qui décide vraiment d'ajouter une brique partenaire au bundle ? Le dirigeant, le directeur commercial, le directeur technique, le manager de practice ? Quels sont ses KPI (CA, marge, taux de transformation deals, NPS clients) ? Comment Mintizy l'aide à les atteindre ?
2. **Persona ACHETEUR : objections** : qu'est-ce qui empêche aujourd'hui un intégrateur ERP de signer un partenariat éditeur tiers ? Coût d'intégration ? Peur de la dépendance ? Préférence pour dev maison ?
3. **Persona UTILISATEUR (entreprise SAV cliente du revendeur)** : qui paye et qui utilise le portail ? Le dirigeant signe le contrat, mais qui le configure et le promeut auprès des clients finaux ?
4. **Persona UTILISATEUR : trigger d'achat** : quel événement déclenche l'envie d'avoir un portail client ? Un appel d'offres perdu ? Un client qui réclame de la transparence ? La mise en place d'un nouvel ERP ?
5. **Lien entre les deux personas** : qui propose Mintizy en premier au client SAV : le commercial du revendeur, ou le client SAV qui le réclame en réponse à un cas concret ?

---

## Prochaine étape : /offer-persona

Cible obligatoire : 2 personas (ACHETEUR intégrateur + UTILISATEUR entreprise SAV).

---

## MARKET RESEARCH UPDATE

- Date : 2026-05-05 | Canal : B (Revendeurs intégrateurs ERP) | MCP Datagouv : ✅ Oui (API Recherche d'Entreprises) | MCP INSEE entreprises tiers : non détecté
- **Hypothèses validées** : univers amont 50-100 cibles prioritaires (NAF 62.02A 10-249 sal. = 3 156 ESN totales, dont ~10-15 % intégrateurs ERP métier passant le filtre SAV+dev) ; univers aval 3 550 PME maintenance dont 1 000-1 800 adressables via canal partenaire ; marché éduqué (Praxedo, Twimm, Synchroteam établis depuis 10+ ans) ; budgets dédiés côté revendeur (10-30 k€ setup + marge récurrente) ; cycle 3-9 mois standard partenariat
- **Hypothèses invalidées** : aucune
- **À confirmer terrain** : taux exact "capacité dev senior dispo 3 semaines" (50-70 % estimé), multiplicateur groupements (Gasel-like), différenciation Mintizy vs Praxedo Portail donneur d'ordres
- **Profil prioritaire** : Stéphane Maréchal (intégrateur ERP) : Score **15/20**
- **Checkpoint viabilité 3** : Budget ✅ | Maturité ✅ | Cycle 3-9 mois (médiane 5 mois)
- **TAM/SAM/SOM** : TAM ~8,1 M€ ARR / SAM 2,3-4,1 M€ / SOM 3 ans 114-205 k€ ARR
- **Priorisation ERP année 1** : 🥇 Cegid XRP Flex (proof OCI à dupliquer) + 🥇 Sage X3 (volume + maturité). Année 2 : Dynamics 365 BC + Divalto. Opportuniste : Akuiteo, SAP B1, Odoo.
- **Recommandation produit** : ouvrir une option "passerelle livrée clé-en-main" par UCCELLO pour les intégrateurs sans dev senior dispo (ouvre le marché de 50-100 à 150-200 cibles)
- **Questions pour /offer-competitive-intel** :
  1. Praxedo "Portail donneur d'ordres" : périmètre fonctionnel exact, frontière vs Mintizy ?
  2. Pourquoi OCI bundle Mintizy + Praxedo simultanément ?
  3. Tarifs Praxedo portail client + modèle partenaires
  4. Twimm, Synchroteam, ClicktoSAV, Mobi-G : portail comparable ?
  5. Portails ERP natifs (Dynamics 365 FSM, Sage X3 Service) : concurrence ou complément ?

---

## COMPETITIVE INTEL UPDATE

- Date : 2026-05-05
- **Concurrents directs identifiés** : Praxedo (FSM dominant + Portail donneur d'ordres B2B sous-traitance), Microsoft Dynamics 365 FS Portal (couplé Microsoft, ~95-150€/user/mois), Sage X3 SAV + portails tiers (Weblinks ADSI, ASR SAV), Synchroteam (low-cost multi-vertical), Twimm (cible patrimoine immobilier).
- **Concurrent baseline** : "Ne rien faire / Excel + emails" (statut majoritaire chez les PME maintenance FR).
- **Zone de différenciation gagnée** : portail B2B2C dédié exposition client final + pricing palier client final (pas per-user technicien) + indépendance ERP via API + marque blanche optionnelle.
- **Phrase de positionnement** : *"Mintizy est le portail client B2B2C dédié à l'exposition de la maintenance vers les clients finaux du prestataire : intégrable à n'importe quel ERP via API ouverte, déployable en marque Mintizy ou en marque blanche, à pricing palier client final. Selon le contexte du revendeur, Mintizy s'utilise en complément d'un FSM existant (Praxedo, Synchroteam) ou en alternative quand le besoin est strictement le portail client final."*
- **Verdict différenciation** : MOYENNE-FORTE (forte sur 3 axes pricing/indépendance/rôle, moyenne sur la perception marché car Praxedo plus connu). Pas de PIVOT.
- **Précision utilisateur** : le bundle OCI Praxedo + Mintizy + Cegid Flex est un cas d'usage parmi d'autres, pas un modèle imposé. Mintizy peut aussi se positionner en alternative directe à Praxedo sur le sous-périmètre "portail client final" pour les revendeurs qui n'ont pas (ou pas besoin) d'un FSM dans leur bundle.
- **Questions pour /offer-pricing** :
  1. Le grid OCI tient-il face au pricing per-user technicien des concurrents ? Sur petites tranches (1-10 users), avantage Mintizy moins flagrant.
  2. Faut-il ajouter une option "passerelle livrée par UCCELLO" (5-15k€ one-shot ?) qui ouvrirait le marché aux 50-100 cabinets sans dev senior dispo ?

---

## PRICING UPDATE

- Date : 2026-05-05 | Type offre : A (SaaS récurrent B2B2B revendeur)
- **Modèle** : Hybride (récurrent palier client final + setup fee + options)
- **Tiers récurrents** : Starter 120€ / **Business 180€ ⭐** / Scale 240€ / Enterprise 300€+ HT/mois UCCELLO (par palier d'utilisateurs finaux)
- **Cible majoritaire** : Business (palier 11-50 users finaux), 252€ revendeur HT/mois, 72€ marge
- **Setup fee client final** : 990€ HT one-shot, perçu par revendeur (CRITIQUE pour ROI revendeur sans setup fee : ROI passerelle 4 ans 7 mois ; avec : 14 mois)
- **Option Quick-Start Passerelle UCCELLO** : 14 900€ HT one-shot (livraison passerelle ERP clé-en-main pour cabinets sans dev senior). Ouvre marché de 50-100 à 150-200 cabinets cibles.
- **Option White-label** : +50€/mois HT/client OU 4 900€ HT one-shot global revendeur (modèle au choix)
- **Engagement client final** : 12 mois minimum, renouvellement tacite, préavis 3 mois
- **Engagement revendeur** : 3 clients sur 18 mois pour conserver l'exclusivité territoriale
- **LTV/CAC revendeur** : 5,97x sur palier moyen (LTV 3 582€ / CAC 600€), modèle sain
- **Décision majeure** : la grille OCI devient la grille publique Mintizy pour tous les futurs revendeurs (cohérence + équité), pas de négociation prix au cas par cas
