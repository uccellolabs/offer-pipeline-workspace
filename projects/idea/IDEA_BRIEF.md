# IDEA_BRIEF.md — Shortlist d'opportunités

- **Date** : 2026-04-24 | **Version** : 1.1 | **Agents** : idea-finder + veille web (fusion)
- **Projet** : idea (Uccello Labs) | **MCP SIRENE** : non utilisé — tailles **qualitatives / à valider** en `/market-research`.

---

## Méthode

- **Sources consultées (passe 1)** : Reddit (r/smallbusinessUS, r/SaaS, r/snowflake, r/B2Becommerce_Hub, r/salesforce), synthèses marché PRM (PeerSpot / FitGap / Growann sur Channeltivity, Gartner Peer Insights Impartner).
- **Sources consultées (passe 2 — veille web)** : Reddit (r/smallbusiness, r/Entrepreneurs — **AP / factures fournisseurs**, **friction inter-apps**), articles **PME France** (France Num 2025, Oxelea, Infonet), synthèses **micro-SaaS / vertical B2B** 2026 (niches sous-servies, « missing middle » 10–200 pers.).
- **Plaintes analysées** : ~30 (passe 1) + patterns complémentaires **saisie fournisseurs**, **approbations / écarts PO**, **copy-paste entre outils**, **priorisation transformation numérique PME**.
- **Idées générées** : 8 → **shortlist** : **6** (écartées : refaire un PRM enterprise ; copier Salesforce Data Cloud ; vertical défense ; niches US ultra-réglementées sans levier terrain).

---

## Shortlist (classée par score)

### Idée #1 — **Ticketing / helpdesk « juste assez »** pour PME et équipes qui crèvent sur l’e-mail partagé

**Score : 26/30**

| Critère | /5 |
|---------|----|
| Intensité de la douleur | 5 |
| Volume du segment | 5 |
| Willingness to pay | 4 |
| Fit compétences | 4 |
| Fit orientation projet | 4 |
| Faisabilité ressources | 4 |
| **Total** | **26** |

**La douleur** — *« Zendesk nous a quoté 3k$/mois pour 20 personnes »*, *« les tickets passent à la trappe, doublons, tableurs »*, *« Zendesk / Freshdesk = tank pour un couteau »*.

**Qui souffre** — **TPE / PME** B2B, petites équipes support, **éditeurs** en bootstrap (aligné ton contexte : support encore e-mail).

**Preuves (≥3 citations, 3 sources)**

- « **Zendesk quoted us 3k monthly which is absurd for our 20 person company** handling maybe 100 tickets a week » — r/smallbusinessUS (https://www.reddit.com/r/smallbusinessUS/comments/1q642i5/whats_the_best_customer_support_software_2026/ ).
- « **tickets slip through, duplicates happen, and tracking who owns what takes forever**. zendesk and freshdesk feel overkill and get expensive fast » — r/SaaS (https://www.reddit.com/r/SaaS/comments/1r7z3yf/best_ticketing_system_for_small_teams_ai_helpdesk/ ).
- « **Zendesk is great until you scale even a little then it’s just billing surprises** » — r/SaaS (https://www.reddit.com/r/SaaS/comments/1qknybh/zendesk_pricing_jumped_again_what_alternatives/ ).

**Preuve willingness to pay** — Freshdesk, Help Scout, Zoho Desk, BoldDesk, Monday Service, etc. : le segment **paie** ; la douleur est **prix + complexité**, pas l’absence de budget.

**Solution potentielle (esquisse)** — Produit **MVP** (complexité **3/10**) : e-mail → tickets, assignation, priorités, base de connaissances légère, **webhooks** ; **lots** 2–3 pour automations / IA déflection. **Vente indirecte** : cabinets, ESN, partenaires qui installent déjà du stack client.

**Pourquoi toi** — Full-stack + **hybride** SaaS / sur-mesure + besoin interne (« outil support à mettre en place » dans ton contexte).

**Risques / angles morts** — Marché **dense** ; différenciation = **prix prévisible** + **onboarding 1 jour** + **francophone** + intégrations ciblées.

**SPICED** — Situation ✅ · Pain ✅ · Impact ✅ · Critical Event ✅ (stack support qui explose avec la croissance) · Decision ✅.

---

### Idée #2 — **Santé des flux partenaire → client** (diagnostic + connecteurs par lots) — aligné douleur **données incomplètes** type Mintizy / OCI

**Score : 25/30**

| Critère | /5 |
|---------|----|
| Intensité de la douleur | 4 |
| Volume du segment | 4 |
| Willingness to pay | 5 |
| Fit compétences | 5 |
| Fit orientation projet | 5 |
| Faisabilité ressources | 2 |
| **Total** | **25** |

**La douleur** — *« punchout + EDI = workflows et data mapping »*, *« intégration ERP / portail pas un site vitrine »*, *« données analytics bloquées 6 mois entre SAP et entrepôt »*.

**Qui souffre** — **Éditeurs** et **intégrateurs** en **vente indirecte** ; PME qui passent par distributeurs (ton **OCI** / grille partenaire).

**Preuves**

- « **punchout catalogs plus EDI keep coming up as major pain points**… **data mapping, and making sure orders sync flawlessly between systems** » — r/B2Becommerce_Hub (https://www.reddit.com/r/B2Becommerce_Hub/comments/1o15t9n/how_do_you_handle_punchout_catalogs_and_edi_in.json ).
- « **The challenge is finding a development partner that understands vendor portals specifically** — not agencies that build generic web applications and apply a vendor portal label » — contenu hub B2B (r/B2Becommerce_Hub, même sub — fil d’annuaire / guide ; **traiter comme signal marché** sur le gap partenaire/portail).
- « **maintenance overhead was going to be brutal with every SAP update** potentially breaking something » — r/snowflake / intégration SAP→Snowflake (https://www.reddit.com/r/snowflake/comments/1r6sqjl/sap_ariba_data_into_snowflake_after_six_months_of/ ) — **métaphore** dette d’intégration.

**Preuve willingness to pay** — Budgets **portails fournisseurs / B2B** et **connecteurs** (Elogic, ScienceSoft, etc. cités dans l’écosystème) ; chez toi la douleur est **déjà vécue** côté Mintizy (données manquantes selon flux partenaire).

**Solution potentielle** — **Lot 1** : audit flux + tableau de bord **SLA données** (retards, champs manquants, rejets) ; **Lots suivants** : connecteurs ciblés (API, fichiers, webhooks). Position **co-pilotage** avec l’intégrateur.

**Pourquoi toi** — Intégrations **ERP/CRM** + **réseau partenaires** + expérience **canal indirect**.

**Risques** — Scope **consulting** qui dérive ; besoin d’un **packaging** produit très clair pour rester en **3/10** technique au départ.

---

### Idée #3 — **Factures fournisseurs : circuit d’approbation + file des exceptions** (complément OCR / compta)

**Score : 24/30**

| Critère | /5 |
|---------|----|
| Intensité de la douleur | 5 |
| Volume du segment | 4 |
| Willingness to pay | 4 |
| Fit compétences | 4 |
| Fit orientation projet | 4 |
| Faisabilité ressources | 3 |
| **Total** | **24** |

**La douleur** — Saisie fournisseurs encore **manuelle ou semi-automatisée** ; surtout : **qui approuve ?**, **écart PO / crédit**, **relances**, **où ça bloque avant compta** — le commentaire terrain : *« le vrai temps perdu n’est pas la frappe, c’est le va-et-vient »*. Secondaire : formats fournisseurs hétérogènes → OCR qui **casse** (lignes, taxes, tableaux).

**Qui souffre** — **PME** avec volume moyen de factures (seuil souvent cité **50–200+/mois** où le manuel devient « taxe sur la croissance »), directions financières / opés sans outil de workflow unifié.

**Preuves**

- « **The real time drain isn’t the typing. It’s the back-and-forth**… **Who actually approves this?**… **Matching + exceptions eat the most time** » — r/smallbusiness (https://www.reddit.com/r/smallbusiness/comments/1qz5yzt/small_business_owners_are_you_still_manually/ ).
- « **Spent 6 hours manually entering supplier invoices**… OCR **missed line items**, **weird PDF formats** » — r/Entrepreneurs (https://www.reddit.com/r/Entrepreneurs/comments/1ppgnd0/spent_6_hours_manually_entering_supplier_invoices/ ).
- **France** : écart persistant entre **usage d’outils numériques** et **automatisation des processus financiers** ; enjeu d’**intégration** et de **passage à l’échelle** sans complexité excessive — baromètre et analyses **France Num 2025** / relayés par [economie.gouv.fr](https://www.economie.gouv.fr/actualites/transformation-numerique-des-tpepme-les-enseignements-du-barometre-2025-de-france-num), [Infonet](https://infonet.fr/actualite/articles-sur-lactualite-technologique/digitalisation-pme-gains-productivite-2025/).

**Preuve willingness to pay** — Marché **OCR + pré-compta** (Dext, Hubdoc, offres QuickBooks/Xero, etc.) : les PME **paient** ; la **niche** = couche **workflow + exceptions** lisible, pas refaire un Dext.

**Solution potentielle (esquisse)** — Email / dossier → **brouillon** vers compta (ou lien API) + **file d’approbation** + **règles** (montants, comptes) + **file « à traiter humain »** pour cas limites. **Lots** : règles par fournisseur récurrent, rapprochement PO simple, tableaux de bord retards.

**Pourquoi toi** — Intégrations, **hybride** produit / mise en place, **francophonie** + PME ; complexité **3/10** si périmètre **workflow** avant **IA extraction** profonde.

**Risques** — Chevauchement avec modules natifs ERP ; besoin d’**intégrations compta** (Sage, Pennylane, etc.) pour adoption ; conformité **facture électronique** à anticiper selon cible.

---

### Idée #4 — **Couche PRM / portail partenaire allégée** pour éditeurs **sans budget Channeltivity / Impartner**

**Score : 23/30**

| Critère | /5 |
|---------|----|
| Intensité de la douleur | 4 |
| Volume du segment | 3 |
| Willingness to pay | 4 |
| Fit compétences | 4 |
| Fit orientation projet | 5 |
| Faisabilité ressources | 3 |
| **Total** | **23** |

**La douleur** — PRM **cher**, **courbe d’apprentissage**, **support lent**, **analytics peu exploitables** selon retours acheteurs.

**Qui souffre** — **Éditeurs B2B** qui lancent ou scalent un **programme partenaires** (toi : objectif **3–5 partenaires**, **vente indirecte**).

**Preuves**

- « **The pricing is slightly above average** » + attentes longues sur évolutions — PeerSpot / Channeltivity (https://www.peerspot.com/vendors/channeltivity ).
- « **Edition | $1,899 per month** » (positionnement mid-market / enterprise) — FitGap (https://us.fitgap.com/products/channeltivity ).
- « **Channeltivity might not be suitable for smaller businesses or those with tight budgets** » — Growann (https://www.growann.com/review/channeltivity ).

**Preuve willingness to pay** — Le marché PRM existe ; la **niche** est : **sous-PRM** pour PME éditrices / francophonie / **setup en semaines**.

**Solution potentielle** — Portail **minimal** : onboarding partenaire, ressources, **deal reg** simple, **webhooks** vers CRM ; pas tout-in-one Impartner.

**Pourquoi toi** — Aligné **canal indirect** + **hybride** + **lots**.

**Risques** — Feature creep ; conflit avec **Salesforce PRM** sur gros comptes ; besoin **juridique** (MDF, conformité).

---

### Idée #5 — **Diagnostic maturité numérique PME + feuille de route intégrations** (produit d’entrée)

**Score : 21/30**

| Critère | /5 |
|---------|----|
| Intensité de la douleur | 3 |
| Volume du segment | 5 |
| Willingness to pay | 3 |
| Fit compétences | 4 |
| Fit orientation projet | 4 |
| Faisabilité ressources | 2 |
| **Total** | **21** |

**La douleur** — Dirigeants et PME **ne savent pas par où commencer** ; **trop d’outils** sans orchestration ; **copy-paste** et **ponts fragiles** entre CRM, facturation, planning (*« rien ne parle entre eux »* — [r/smallbusiness](https://www.reddit.com/r/smallbusiness/comments/1ry01nd/is_it_just_me_or_is_automated_software_still.json)). Besoin de **hiérarchiser** (cyber, collab, automatisations simples, CRM…) sans **sur-accumulation**.

**Qui souffre** — **TPE/PME** France / francophones en phase **structuration** (niveaux 2–3 type France Num : CRM, facturation, puis **intégrations**).

**Preuves**

- « **46 %** des dirigeants de PME **ne savent pas par où commencer** ou comment hiérarchiser » — synthèses **transformation digitale PME** (ex. [Oxelea](https://www.oxelea.fr/transformation-digitale-pme-2025/), [Pulse SXM 2026](https://pulse.sxm-success-training.com/article/transformation-digitale-pme-france-bilan-2025-perspectives-2026/)).
- Levier **automatisation ciblée** + **intégrations** sans complexité excessive — [Oxelea leviers 2026](https://www.oxelea.fr/leviers-digitaux-pme-2025-ia-automatisation/).
- Friction **inter-apps** = signal complémentaire pour un **diagnostic** qui aboutit à **2–3 quick wins** mesurables.

**Preuve willingness to pay** — Diagnostics **2–4 k€** cités dans l’écosystème conseil PME ; **packaging** fixe + option **mise en œuvre** (lots) = aligné **hybride**.

**Solution potentielle** — **Score maturité** (questionnaire + entretien court) + **cartographie outils / flux** + **top 3 actions** (90 j) + **devis types** pour connecteurs. Produit **porte d’entrée** vers idées **#1**, **#3**, **#2** selon contexte.

**Pourquoi toi** — Position **expertise + delivery** ; réseau **partenaires / ESN** ; cohérent avec **ambition 20–50 k€ MRR** si **récurrent** (abonnement pilotage léger) ou **réachat** conseil.

**Risques** — Risque **prestation pure** si pas de **produit** (grille, rapport, suivi) ; CAC si marketing trop large — **niche** (vertical ou taille) recommandée.

---

### Idée #6 — **Couche « data mapping guardrails »** pour stacks marketing / CRM (éviter les pièges type multi-PK / migrations)

**Score : 20/30**

| Critère | /5 |
|---------|----|
| Intensité de la douleur | 4 |
| Volume du segment | 3 |
| Willingness to pay | 4 |
| Fit compétences | 4 |
| Fit orientation projet | 3 |
| Faisabilité ressources | 2 |
| **Total** | **20** |

**La douleur** — Plateformes **data cloud** rigides, erreurs de mapping en prod, **pas de sandbox**, facturation crédits.

**Qui souffre** — Équipes **revops / marketing ops** mid-market (souvent **hors** cœur TPE/PME du contexte).

**Preuves**

- « **Overall, Data Cloud is not flexible at all.... It feels like you’re not allowed to make mistakes** » — r/salesforce (https://www.reddit.com/r/salesforce/comments/1r2sy0q/salesforce_data_cloud_my_experience_so_far_its/ ).
- « **SFTP file ingestion nightmare** » / métadonnées incohérentes — même fil (ibid.).
- « **mistakes happen**… **stuck** » — même fil (ibid.).

**Preuve willingness to pay** — **Consultants** revops + outils ETL ; budget **enterprise** plutôt que PME pure.

**Solution potentielle** — **Prestation** + petit **outil** de validation de schémas / checks pré-prod — utile si tu **montes en complexité** plus tard (**> 3/10**).

**Pourquoi toi** — Full-stack + intégrations ; **contre** : moins aligné **TPE/PME** et **complexité cible 3/10**.

**SPICED** — Impact ✅ chez la cible enterprise · **Fit volume segment** ⚠️.

---

## Recommandation

**À creuser en priorité : Idée #1** (helpdesk / ticketing **simple**, prévisible, pour PME + ton usage interne).

**Pourquoi** — Triangulation **forte** sur Reddit (prix Zendesk, chaos inbox + tableurs, « overkill »), **WTP** clair, **faisabilité** cohérente avec **3/10** et **lots** successifs, **canal indirect** possible via partenaires IT.

**Alternative très proche du terrain PME (veille web)** — **Idée #3** (factures fournisseurs : **approbations + exceptions**) : douleur **validée** (y compris France : retard d’**automatisation financière**), **complément** des gros OCR plutôt que remplacement, **intégrations** = ton cœur de métier.

**Alternative stratégique Uccello** — **Idée #2** si tu veux capitaliser sur la douleur **données partenaires** déjà dans ton contexte Mintizy — à trancher en `/offer-cadrage` (produit vs service).

**Levier commercial** — **Idée #5** peut servir de **porte d’entrée** packagée vers **#1**, **#3** ou **#2** selon le diagnostic.

---

## Prochaine étape

→ **`/offer-cadrage`** sur **Idée #1**, **#3** ou **#2** (expliciter : cible francophone, différenciation, partenaires prescripteurs).

---

## Note

`SESSION_LOG.md` du projet **`idea`** : journal initialisé le **2026-04-25** ; ce brief intègre en **1.1** (2026-04-24) la **veille web** sans fichier séparé `v2`.
