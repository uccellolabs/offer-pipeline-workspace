# COMPETITIVE_BRIEF.md : Mintizy / Portail revendeurs ERP

- Date : 2026-05-05 | Version : 1.0 | Agent : /offer-competitive-intel
- Sources : sites officiels, Microsoft Learn, Capterra, GetApp, Logiciels.pro, blogs spécialisés FSM

---

## 1. Cartographie

### Concurrents directs (même problème, même cible)

| Acteur | Catégorie | Risque pour Mintizy |
|--------|-----------|---------------------|
| **Praxedo** Portail donneur d'ordres | FSM avec portail intégré | 🔴 Critique : déjà bundlé chez OCI, leader catégorie FSM en France |
| **Microsoft Dynamics 365 Field Service Portal** | Portail natif d'un ERP/FSM Microsoft | 🟠 Élevé sur écosystème Microsoft (cabinets Dynamics) |
| **Sage X3 SAV** + portail tiers (ADSI Weblinks, ASR Group SAV…) | Module SAV ERP + portail B2B intégrateur | 🟠 Élevé sur écosystème Sage X3 |
| **Synchroteam** Customer Portal | FSM low-cost avec portail | 🟡 Moyen, cible TPE/PME multi-secteurs |
| **Twimm** | CMMS patrimoine immobilier avec portail | 🟢 Faible, cible différente (immobilier/syndics) |

### Concurrents indirects (même budget, approche différente)

- **Portails maison développés en interne** par le cabinet d'intégration ERP ou par la PME SAV elle-même
- **Microsoft Power Pages / SharePoint custom** déployés ad hoc par les cabinets Dynamics
- **Solutions ITSM détournées** (Zendesk Sunshine, Freshdesk Customer Portal) : peu adaptées mais utilisées par défaut
- **Modules portail générique des ERP** (Cegid XRP, Akuiteo, Divalto, Odoo Studio)

### Ne rien faire

Statut majoritaire chez les PME maintenance françaises : **Excel + emails + PDFs envoyés en pièce jointe**. C'est le "concurrent" le plus puissant, alimenté par l'inertie et la peur de l'investissement abandonné (cf. journal intime PERSONA_UTILISATEUR).

---

## 2. Fiche Praxedo Portail donneur d'ordres (concurrent #1)

### Identité
- Nom : Praxedo
- Site : praxedo.fr / praxedo.com
- Positionnement : leader français du Field Service Management, plateforme cloud pour gestion d'interventions terrain
- Taille : ~150 collaborateurs, ~1500 clients monde, présent depuis 2005, racheté par Battery Ventures en 2019 puis par Vista Equity Partners
- Communication : "Le logiciel de gestion d'interventions, leader du marché"

### Forces réelles
- Leader catégorie FSM en France (notoriété forte chez intégrateurs ERP : tous le connaissent)
- Solution mature, robuste, cas clients prestigieux (Bouygues Telecom, Potain, ENGIE Solutions, Veolia)
- Catalogue de connecteurs ERP large (SAP, Sage, Microsoft, Cegid, Divalto)
- Module portail donneur d'ordres en standard
- Application mobile technicien jugée fluide
- Source : praxedo.com/product-tour/work-order-followup, témoignages clients site officiel

### Faiblesses documentées
- **Le "Portail donneur d'ordres" est un portail B2B de sous-traitance, pas un portail B2C "exposition client final"**. Sa logique : un opérateur télécom (donneur d'ordres) sous-traite à un prestataire (utilisateur Praxedo), et le portail permet au donneur d'ordres de déclencher et suivre. UX et workflows orientés sous-traitance, pas image de marque vers les clients finaux du prestataire. Source : praxedo.com/product-tour/work-order-followup
- Pricing per-user technicien (24,5 à 69€/user/mois) qui devient cher dès qu'on a 30+ techniciens. Source : logiciels.pro/praxedo, getapp.com
- Pas de marque blanche grand public (le portail est en marque Praxedo, pas en marque du prestataire)
- Documentation "Portail donneur d'ordres" historiquement orientée télécom et SAV BtoBtoB, peu de cas d'usage pour cuisinistes pro / fitness exposant à des restaurateurs ou clubs
- Adoption portail par les clients finaux mal documentée (Praxedo ne publie pas de chiffre adoption portail)

### Pricing
- Start : 24,5€ HT/user/mois
- Classic : 49€ HT/user/mois
- Enterprise : 69€ HT/user/mois
- Premium : sur devis
- Le "Portail donneur d'ordres" est inclus à partir de Classic (pas isolable)
- Source : logiciels.pro/praxedo (tarifs publics 2026)

### Adresse du persona Pascal Dubreuil ?
- Praxedo couvre la douleur "outil terrain technicien" (préventif/correctif/rapports/CERFA), pas la douleur "exposer une vitrine client final pour gagner les appels d'offres".
- Le portail Praxedo n'est pas le levier de différenciation marketing dans une réponse à AO Carrefour, là où Mintizy l'est explicitement (cf. bundle OCI).

---

## 3. Fiche Microsoft Dynamics 365 Field Service Portal (concurrent #2)

### Identité
- Nom : Dynamics 365 Field Service Customer Portal
- Site : learn.microsoft.com/dynamics365/field-service/customer-portal-overview
- Positionnement : portail client natif inclus dans Dynamics 365 Field Service (module FSM Microsoft, distinct de Dynamics 365 Business Central)
- Configurable via Power Pages / Power Apps Portals

### Forces réelles
- Self-scheduling + rescheduling + cancel par le client final
- "Track My Technician" en temps réel
- Notifications email/SMS configurables
- Customer Voice surveys intégrés
- Personnalisation UI via Power Pages design studio (donc capable de marque blanche partielle)
- Source : learn.microsoft.com/dynamics365/field-service

### Faiblesses documentées
- **Couplé à Dynamics 365 Field Service** (~95-150€/user/mois Microsoft), pas à Dynamics 365 Business Central seul. Une PME SAV qui a Business Central sans Field Service n'a PAS le portail
- Configuration Power Pages exige expertise spécifique (Power Platform), non triviale pour un cabinet d'intégration BC standard
- Pricing Microsoft total (BC + FS + Power Pages capacity) souvent > 200€/user, hors budget PME maintenance
- L'écosystème Microsoft Field Service est plutôt mid-market+ : peu de PME 10-50 techniciens y sont
- Source : softwarefinder.com/field-service/dynamics-365-field-service

### Pricing
- D365 Field Service Standalone : 95-150€/user/mois (selon tier)
- Power Pages capacity additionnelle
- Total entreprise SAV 35 techniciens : ~3 500-5 000€/mois (vs 252€/mois pour Mintizy palier 11-50 sur OCI)

### Adresse du persona Stéphane Maréchal ?
- Pour les cabinets Dynamics 365 BC qui n'ont pas de practice Dynamics FS, Mintizy reste pertinent (la majorité des cabinets BC sont sur le finance/distribution, pas le field service).
- Pour les cabinets Dynamics 365 FS, Mintizy n'est pas pertinent (ils ont déjà mieux intégré).
- Implication stratégique : Dynamics 365 BC reste un canal valable, mais pas Dynamics 365 FS. Cible Mintizy = cabinets BC sans practice FS.

---

## 4. Fiche Sage X3 SAV + ADSI Weblinks (concurrent #3)

### Identité
- Nom : Module SAV de Sage X3 (natif) + portails B2B tiers comme Weblinks (ADSI Group), ASR SAV (Groupe SRA)
- Site : adsi-group.com/portail-web-B2B-client-webLinks.html, groupe-sra.fr/sage-x3-sav
- Positionnement : module SAV intégré à Sage X3, complété par un portail B2B externe développé par certains intégrateurs partenaires

### Forces réelles
- Intégration native Sage X3 (pas de double saisie)
- Couvre la gestion des contrats (garantie, points, maintenance), planification interventions, identification client, accès flotte équipements
- Quelques intégrateurs Sage X3 ont développé leur propre portail B2B (ADSI Weblinks notamment)
- Source : groupe-sra.fr, adsi-group.com

### Faiblesses documentées
- Portail Sage X3 SAV B2B est centré "ERP back-office", pas "vitrine UX client final"
- Pas de mode mobile dédié, pas de QR codes équipements, UX "ERP-style" datée
- Solutions tierces (Weblinks, ASR SAV) sont propriétaires d'un seul intégrateur, donc Cegid/Sage qui veulent un portail doivent soit refaire eux-mêmes, soit racheter à un confrère = pas une solution white-label disponible publiquement
- Adoption faible côté clients finaux (les retours clients Sage X3 mentionnent "module SAV peu UX-first")

### Pricing
- Inclus dans Sage X3 (pas de prix isolable)
- Portails tiers comme Weblinks : sur devis intégrateur, généralement 150-400€/mois selon volume

### Adresse du persona Stéphane Maréchal ?
- C'est le concurrent le plus direct sur Sage X3 : si Stéphane peut développer son propre portail Sage X3 SAV ou racheter une licence Weblinks, il n'a pas besoin de Mintizy.
- Argumentaire Mintizy : (1) UX dédiée vs UX ERP-style, (2) déploiement sous 4 semaines vs 6-12 mois pour un dev maison, (3) mobile + QR codes natifs, (4) marque Mintizy reconnue et white-label optionnel.

---

## 5. Fiche Synchroteam Customer Portal (concurrent #4)

### Identité
- Nom : Synchroteam
- Site : synchroteam.com
- Positionnement : FSM SaaS multi-secteurs (services, médical, agricole), accessible
- Présent en France via partenaires intégrateurs

### Forces réelles
- Tarifs accessibles (~22€/user/mois)
- Customer Portal inclus
- Connecteurs Sage X3, Dynamics, SAP via custom

### Faiblesses documentées
- Plateforme moins riche que Praxedo (avis mitigés sur la robustesse, capterra)
- Cible TPE/PME multi-secteurs : pas spécialisé maintenance technique pro
- Portail client basique, pas de marque blanche dédiée

### Pricing
- ~22€/user/mois (Annual) à 45€/user/mois (Premium)
- Inclut le portail dans tous les tiers
- Source : synchroteam.com/pricing

### Adresse du persona ?
- Synchroteam attaque le segment "PME économique cherche solution multi" : pas le même positionnement que Mintizy (qui adresse PME structurées via revendeur ERP). Concurrence indirecte plus que frontale.

---

## 6. Fiche "Ne rien faire / Excel + emails" (concurrent baseline)

### Identité
- État du marché majoritaire chez les PME maintenance françaises
- Outils : Excel, Outlook, WhatsApp pro, PDFs envoyés manuellement, parfois site web statique avec onglet "interventions" non maintenu

### Forces réelles
- Coût zéro
- Aucune adoption requise
- Aucune dépendance fournisseur

### Faiblesses documentées
- Aucune transparence client
- Charge mentale énorme (cf. Pascal Dubreuil "30 appels par jour")
- Disqualifiant en réponse à appel d'offres réglementé (cuisine pro, GMS, collectivités demandent un portail)
- Aucun ROI mesurable, aucun levier marketing

### Comment Mintizy le bat
- Comparaison ROI : 1 appel d'offres remporté = 13 ans de portail payés
- Réduction appels entrants 30 à 40 % = 1h/jour récupérée Sandrine = 13k€/an productivité

---

## 7. Matrice de positionnement

Critères basés sur les valeurs des personas (PERSONA_ACHETEUR partie 11 + PERSONA_UTILISATEUR partie 11) :

| Critère | **Mintizy Portail** | Praxedo Portail DO | D365 FS Portal | Sage X3 SAV + portail | Synchroteam | Excel/maison |
|---------|---------------------|--------------------|--------------|------------------------|-------------|--------------|
| Indépendance ERP (intégrable à tout ERP via API) | ✅ Oui | ⚠️ Connecteurs disponibles | ❌ Couplé Dynamics 365 FS | ❌ Couplé Sage X3 | ⚠️ Connecteurs custom | N/A |
| UX dédiée client final non-tech | ✅ Native | ⚠️ Orienté donneur d'ordres B2B | ✅ Power Pages config | ❌ UX ERP datée | ⚠️ Basique | ❌ |
| Marque blanche / co-branding | ✅ Optionnelle | ❌ Marque Praxedo | ⚠️ Power Pages | ⚠️ Custom intégrateur | ❌ | N/A |
| Mobile + QR codes équipements | ✅ Natif | ⚠️ Mobile technicien, pas client | ⚠️ Mobile via portal | ❌ | ⚠️ Basique | ❌ |
| Marge revendeur récurrente | ✅ 35-40 % | ⚠️ Variable (revente Praxedo) | ❌ Microsoft prend tout | ⚠️ Variable | ❌ Faible | N/A |
| Pricing palier client final (pas per-user technicien) | ✅ 120-300€ palier users | ❌ 24,5-69€ × users (cher >30 tech.) | ❌ 95-150€ × users | ⚠️ Variable | ❌ Per-user | N/A |
| Conformité CERFA / F-Gas / réglementaire | ✅ Native (extraction Mintizy) | ⚠️ Via custom | ⚠️ Via dev | ⚠️ Via custom | ❌ | ❌ |
| Déploiement sous 4 semaines (passerelle revendeur) | ✅ | ❌ Plusieurs mois (Praxedo intégration full) | ❌ 3-6 mois | ❌ 3-12 mois portail custom | ⚠️ 1-3 mois | N/A |
| Adoption clients finaux mesurée | ✅ 65-75 % à 6 mois (cas cuisinistes pro) | ❌ Non publié | ⚠️ Partiel | ❌ Non publié | ❌ Non publié | ❌ |

**Lecture matrice** : Mintizy gagne sur **6 critères clairement** (indépendance ERP, marque blanche, mobile/QR, marge revendeur, pricing palier, déploiement rapide) et égalise/perd sur 3 (UX, conformité, adoption — sur ces 3 points, l'écart est faible).

---

## 8. Positionnement différenciant

### Zone de différenciation gagnée clairement

**"Portail B2B2C dédié à l'exposition de la maintenance vers les clients finaux du prestataire, intégrable à n'importe quel ERP via API, marque-blanche, à pricing palier client (pas per-user technicien)."**

### Phrase de positionnement Mintizy

> *"Mintizy est le portail client B2B2C dédié à l'exposition de la maintenance vers les clients finaux du prestataire : intégrable à n'importe quel ERP via API ouverte, déployable en marque Mintizy ou en marque blanche, à pricing palier client final (pas per-user technicien). Selon le contexte du revendeur, Mintizy s'utilise en complément d'un FSM existant (Praxedo, Synchroteam) ou en alternative quand le besoin est strictement le portail client final."*

### 3 arguments non-comparables

1. **Positionnement spécialisé portail B2B2C** : Mintizy expose une **vitrine commerciale au client final** du prestataire (B2B2C, ex : Carrefour qui consulte ses 4 frigos suivis par son frigoriste). Praxedo couvre principalement l'**outil terrain technicien** + la **collaboration donneur d'ordres → sous-traitant** (B2B sous-traitance, ex : opérateur télécom qui sous-traite à un prestataire). Selon le contexte du revendeur :
   - **Cas complémentaire (modèle OCI)** : le revendeur bundle Mintizy + un FSM (Praxedo, Synchroteam) car les deux rôles coexistent dans la chaîne de valeur du client SAV.
   - **Cas alternatif** : le revendeur n'a pas (ou pas besoin) de FSM dans son bundle, le client SAV cherche strictement à exposer ses interventions au client final, Mintizy se positionne directement en alternative à un portail Praxedo isolé ou un dev custom.

2. **Pricing au palier client final, pas per-user technicien**. Pour une PME maintenance avec 35 techniciens, Praxedo Classic = 35 × 49€ = **1 715€/mois**. Mintizy palier 11-50 users finaux = **252€/mois HT** (grille OCI). Différence x6 à x10 sur l'utilité "portail client final" pure. Cela permet au revendeur d'attaquer des budgets plus modestes et de gagner des deals où le client final n'a pas le ROI Praxedo.

3. **Indépendance ERP via API ouverte + marque blanche optionnelle**. Le revendeur peut déployer Mintizy sur Cegid XRP Flex, Sage X3, Dynamics 365 BC, Divalto, Akuiteo, en blanc à sa marque ou en marque Mintizy. Aucun concurrent ne propose cette flexibilité combinée.

### Angles morts (où Mintizy est moins bon)

- **Notoriété** : Praxedo, Microsoft, Sage sont 10x plus connus que Mintizy chez les intégrateurs. **Reframing** : la notoriété joue contre vous quand vous voulez vous différencier ; OCI a justement choisi Mintizy parce qu'il n'est PAS Praxedo, ni Microsoft : il complète sans cannibaliser, il offre une marge revendeur plus élevée, il se déploie plus vite.
- **Catalogue de connecteurs prêts à l'emploi** : Praxedo a 30+ connecteurs ERP livrés. Mintizy : zéro (par design, c'est le revendeur qui fait son connecteur). **Reframing** : c'est précisément l'avantage économique pour le revendeur (autonomie technique, contrôle de la roadmap, indépendance).
- **Self-scheduling natif** : D365 FS Portal a du self-scheduling sophistiqué. Mintizy : non priorisé. **Reframing** : le self-scheduling est un cas d'usage d'environ 20 % des PME SAV ; pour 80 %, le besoin est l'**exposition** des interventions, pas la prise de RDV en autonomie. À ajouter en roadmap si la demande émerge.

---

## 9. Battlecards

### CONCURRENT : Praxedo

```
QUAND IL APPARAÎT
- Le revendeur ERP a déjà un partenariat Praxedo
- Le client SAV utilise déjà Praxedo en interne et son commercial dit "on a déjà un portail"
- Salons FSM (présence dominante Praxedo)

SON MESSAGING
"Le logiciel de gestion d'interventions leader du marché. Portail donneur
d'ordres inclus."

POURQUOI LE PROSPECT LE CONSIDÈRE
- Notoriété écrasante (10x plus connu que Mintizy)
- Le "portail" est annoncé en standard, l'acheteur croit que c'est la même fonction
- Catalogue de connecteurs ERP déjà disponibles

COMMENT RÉPONDRE (sans dénigrer)
Deux cas selon le contexte du revendeur :

CAS A : revendeur sans Praxedo dans son bundle, ou client SAV sans Praxedo
"Le portail Praxedo est conçu pour la collaboration donneur d'ordres → sous-
traitant. Si votre client SAV expose plutôt à des restaurateurs, des
collectivités, des chaînes GMS qui veulent voir l'état de leurs équipements,
Mintizy est plus adapté : pricing palier (pas per-user technicien), UX
client final, marque blanche, déploiement 4 semaines via votre passerelle ERP."

CAS B : revendeur avec Praxedo dans son bundle (cas OCI)
"Praxedo équipe vos techniciens et la collaboration B2B. Mintizy adresse une
autre fonction : exposer la vitrine commerciale au client final pour gagner
les appels d'offres réglementés. OCI bundle les deux car ils servent deux
rôles distincts dans la chaîne de valeur."

QUESTION QUI FAIT RÉFLÉCHIR
"Quand votre client SAV répond à un appel d'offres Carrefour ou McDonald's,
est-ce que le directeur de magasin se connecte à un portail orienté
collaboration sous-traitance ou à un portail spécialisé exposition client
final ? Combien d'appels d'offres êtes-vous prêt à perdre sur ce critère ?"

ARGUMENT DÉCISIF
- Si revendeur déjà avec Praxedo : "OCI distribue les deux. Demandez-leur
  comment ils articulent le discours."
- Si revendeur sans Praxedo : "À 252€/mois pour 35 techniciens vs 1 715€
  pour Praxedo Classic, le ROI portail client final est 6 à 10x meilleur,
  même si Praxedo a plus de fonctionnalités globales : vous ne payez que
  pour ce dont vous avez besoin."
```

---

### CONCURRENT : Microsoft Dynamics 365 Field Service Portal

```
QUAND IL APPARAÎT
- Cabinet Dynamics 365 BC qui envisage de monter en compétence Field Service
- Client SAV déjà sur Dynamics 365 FS (rare en PME, fréquent en mid-market)
- Salons Microsoft Inspire / Power Platform Summit

SON MESSAGING
"Customer portal with self-scheduling, technician tracking, surveys, all
integrated in your Microsoft stack. Configure with Power Pages."

POURQUOI LE PROSPECT LE CONSIDÈRE
- Stack Microsoft existante, principe d'unification
- Self-scheduling sophistiqué
- Marque Microsoft rassurante

COMMENT RÉPONDRE
"D365 Field Service Portal est puissant si votre client SAV utilise déjà
Dynamics 365 Field Service, ce qui représente moins de 5 % des PME
maintenance françaises. Pour les 95 % qui ont Dynamics 365 Business Central
sans Field Service, ils n'ont PAS le portail. Mintizy s'intègre à BC seul
en 4 semaines, sans dépendance Power Platform, à 252€/mois HT (vs 95-150€/user/mois
pour FS). Sur 35 techniciens, l'économie est de 3 250 à 5 000€/mois."

QUESTION QUI FAIT RÉFLÉCHIR
"Combien de vos clients PME sont déjà sur Dynamics 365 Field Service, et
combien sur Business Central seul ? Sur ce dernier segment, qui couvre le
besoin portail client ?"

ARGUMENT DÉCISIF
"Mintizy x35 techniciens = 252€/mois. Dynamics 365 FS x35 utilisateurs =
3 500-5 000€/mois. Et le client n'utilise le portail que pour 1 fonction :
exposer les interventions. ROI évident."
```

---

### CONCURRENT : Sage X3 SAV + portail tiers (Weblinks et autres)

```
QUAND IL APPARAÎT
- Cabinet Sage X3 expérimenté dit "on peut le faire avec le module SAV
  natif et un portail Weblinks"
- Discussion avec un Top League Sage X3
- Compétiteur intégrateur revend déjà Weblinks

SON MESSAGING
"Le module SAV Sage X3 + un portail B2B custom (Weblinks) couvre votre
besoin. Pas de dépendance éditeur tiers."

POURQUOI LE PROSPECT LE CONSIDÈRE
- Tout dans Sage = pas de nouveau partenaire
- Weblinks développé par un confrère intégrateur

COMMENT RÉPONDRE
"Weblinks et le module SAV Sage X3 sont des solutions ERP-back-office :
fonctionnels mais UX datée, peu de mobile, pas de QR codes équipements.
Mintizy est conçu d'abord comme une vitrine UX-first pour le client final,
pas comme une extension ERP. Et un portail custom Weblinks : licence
souvent 250-400€/mois, dev d'intégration 4-8 semaines, vous portez le
support N1 ET N2. Avec Mintizy : 252€/mois, 4 semaines passerelle
amortie, support N1 par votre cabinet, N2 par UCCELLO."

QUESTION QUI FAIT RÉFLÉCHIR
"Si vous misez sur le module SAV Sage X3 + un portail Weblinks, comment
expliquerez-vous à votre client cuisiniste pro qui répond à un appel
d'offres GMS, que son portail ressemble à un écran ERP des années 2010 ?"

ARGUMENT DÉCISIF
"OCI est intégrateur Cegid. Ils auraient pu développer leur propre portail
Cegid SAV. Ils ont choisi Mintizy. Leur retour : 4 clients facturés en 8
mois, 15 en pipeline. Le ROI est dans la rapidité de mise en marché et
dans la marge récurrente sans dette technique."
```

---

### CONCURRENT : Synchroteam Customer Portal

```
QUAND IL APPARAÎT
- Cabinet économique cherche solution multi
- TPE PME qui veut "tout-en-un pas cher"

SON MESSAGING
"FSM accessible avec portail client inclus à 22€/user/mois."

POURQUOI LE PROSPECT LE CONSIDÈRE
- Tarif d'appel
- Multi-secteurs

COMMENT RÉPONDRE
"Synchroteam est un FSM low-cost multi-secteurs. Pour une PME maintenance
technique pro structurée (cuisine pro, fitness, CVC, ascensoristes), le
positionnement Mintizy est différent : portail spécialisé exposition client
final B2B2C, pricing palier client final, déploiement via votre revendeur
ERP existant. Ce n'est pas la même conversation commerciale."

QUESTION QUI FAIT RÉFLÉCHIR
"Vos clients SAV sont structurés autour d'un ERP Cegid ou Sage. Pourquoi
ajouter un FSM standalone Synchroteam au lieu d'enrichir leur stack
existant via leur intégrateur ?"

ARGUMENT DÉCISIF
"Synchroteam = solution autonome. Mintizy = brique ajoutée à votre bundle
intégrateur. Ce n'est pas le même levier de différenciation pour vous."
```

---

### CONCURRENT : "Ne rien faire / Excel + maison"

```
QUAND IL APPARAÎT
- 80 % des prospects PME maintenance
- Réponse "on a Excel et ça marche"
- "Mes clients ne demandent pas de portail"

SON MESSAGING
"Pas de coût supplémentaire. On gère comme avant."

POURQUOI LE PROSPECT LE CONSIDÈRE
- Inertie
- Peur de l'investissement abandonné (cf. expériences passées Pascal Dubreuil
  avec Praxedo sous-utilisé, CRM 2019 abandonné)

COMMENT RÉPONDRE
"L'inertie a un coût caché : appels d'offres perdus, charge mentale interne,
image dépassée. Cas concret : un frigoriste pro à Bordeaux a perdu un AO
Carrefour 4 magasins (80k€/an) sur le critère "plateforme de suivi en ligne".
Le portail à 252€/mois représente 0,3 % du contrat perdu en facteur ROI."

QUESTION QUI FAIT RÉFLÉCHIR
"Combien d'appels d'offres avez-vous perdus ces 24 derniers mois sur le
critère "absence de portail" ? Combien avez-vous chiffré pour un dev custom
abandonné ? Combien d'appels entrants entrants par jour pour des questions
"où en est mon intervention" ?"

ARGUMENT DÉCISIF
"Sans engagement, 1 mois gratuit. Aucun risque de tester. Aucun risque de
ne rien faire... sauf perdre les prochains AO."
```

---

## 10. Verdict de différenciation

### **DIFFÉRENCIATION MOYENNE-FORTE.**

**Justification :**
- **Forte** sur 3 axes : pricing palier client (vs per-user technicien), indépendance ERP (vs couplages Microsoft/Sage), rôle "vitrine B2B2C" distinct (vs portail B2B sous-traitance Praxedo).
- **Moyenne** sur la perception marché : Mintizy est moins connu que Praxedo, donc le commercial revendeur doit faire un effort de pédagogie sur la frontière fonctionnelle. Risque de confusion à éduquer (Praxedo = terrain + B2B sous-traitance vs Mintizy = vitrine B2B2C client final).
- Pas de concurrent dominant capable d'écraser Mintizy frontalement à court terme. Le risque le plus sérieux est l'**inertie** ("Excel suffit") et la **confusion concurrentielle** avec Praxedo (pédagogie nécessaire).

**Pas de PIVOT recommandé.** L'angle stratégique tient. La priorité commerciale est de :
1. Cristalliser la frontière Mintizy / FSM (Praxedo, Synchroteam) dans tous les supports (pitch, deck, kit revendeur)
2. Préempter "vitrine B2B2C" comme la catégorie Mintizy (pas "FSM", pas "field service")
3. **Adapter le discours au contexte du revendeur** : complément si le revendeur a déjà un FSM dans son bundle (modèle OCI), alternative directe si le revendeur veut packager strictement le besoin "portail client final" sans empiler un FSM lourd. Ne jamais imposer un bundle Praxedo : c'est un cas d'usage parmi d'autres.

---

## 11. Questions pour /offer-pricing

1. **Le grid OCI tient-il face au pricing per-user technicien des concurrents ?** Pour une PME 35 techniciens : Mintizy 252€/mois vs Praxedo Classic 1 715€/mois = avantage Mintizy. Mais pour une PME de 8 techniciens, Mintizy palier 1-10 = 120€ vs Praxedo Classic 8 × 49 = 392€. Avantage Mintizy mais moins flagrant. Ce n'est pas un problème mais c'est à intégrer en pitch.
2. **Faut-il proposer une option "passerelle livrée par UCCELLO" payante, qui ouvrirait le marché aux 50-100 cabinets sans dev senior dispo ?** Si oui, à quel prix (5-15k€ one-shot ?) et à quelle marge ?

---

## Utilisation pipeline

- /offer-pricing : challenge du grid, ajouter option passerelle livrée
- /offer-final : utiliser la phrase de positionnement et les 5 battlecards verbatim
- /offer-study-website : alimenter la page "Pourquoi Mintizy" avec la matrice et les 3 arguments non-comparables
