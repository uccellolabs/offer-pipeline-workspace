# COMPETITIVE_BRIEF_v2.md
- Date : 2026-04-25 | Version : 2.0 | Agent : competitive-intel
- Personas de référence : Marc (DG fondateur 10–35 sal.) + Frédéric (DG structuré 80–150 sal.)

---

## Cartographie

### Directs (même problème, même cible)
| Concurrent | Canaux couverts | CRM | Pricing |
|---|---|---|---|
| **SyncIn** | WhatsApp perso + LinkedIn | HubSpot (centré) | ~14–20 $/profil/mois (estimé) |
| **Surfe** | LinkedIn uniquement | HubSpot, Salesforce, Pipedrive, Zoho | $17–49/user/mois |
| **TimelinesAI** | WhatsApp uniquement | HubSpot, Pipedrive, Zoho, monday | $8–20/seat/mois |
| **LeadCRM** | LinkedIn uniquement | HubSpot, Pipedrive, Salesforce, Zoho | Free + paid (prix bas) |

### Indirects (même budget ou problème adjacent)
- **HubSpot natif + WhatsApp Business API** — intégration native mais Business API obligatoire (exclut WhatsApp perso de Marc)
- **Lemlist** — multi-canal (email + LinkedIn + WA + appels) mais orienté séquences outbound, pas capture conversations entrantes
- **Folk CRM** — remplace le CRM, ne s'y connecte pas (usage différent)
- **Zapier / Make** — DIY automation, fragile, demande compétences techniques

### Ne rien faire
CRM vide + WhatsApp + LinkedIn + mémoire du commercial. Coût réel estimé : 1–2 deals oubliés/trimestre × ARPA ~12–18k€ × 30% marge = 3 600–10 800 €/trimestre perdus.

---

## Fiches concurrents directs

### SyncIn *(concurrent le plus proche)*

**Identité** — Startup française. Claim : *"zero manual entry, real-time sync, setup 5 min"*. Couvre WhatsApp perso + LinkedIn → HubSpot principalement.

**Forces réelles**
- WhatsApp perso (pas Business API) — différenciant vs HubSpot natif
- LinkedIn inclus dans le même produit
- Français → RGPD rassurant pour Marc et Frédéric
- Installation rapide

**Faiblesses documentées**
- HubSpot-centric — support Pipedrive/Salesforce secondaire (pages produit SyncIn 2026)
- Pricing opaque — pas de page publique claire
- Sync pur : pas de couche intelligence (signaux, digest, priorisation)

**Pricing** — ~14–20 $/profil/mois (estimé via mentions blog/Capterra) — **à confirmer**

**Adresse Marc** — ⚠️ Partiellement. Couvre les canaux, s'arrête au sync. Ne dit pas quoi faire ensuite.

---

### Surfe *(référence LinkedIn → CRM)*

**Identité** — Extension Chrome LinkedIn → CRM. Européen. G2 4.6/5, top 10 sales tools. Bien financé.

**Forces réelles**
- UX reconnue (G2 + Capterra 2025–2026)
- Enrichissement données contact qualité (profil LinkedIn complet → CRM)
- 15–30h économisées/mois/user (sourcé G2)
- Multi-CRM solide (HubSpot, Salesforce, Pipedrive, Zoho)

**Faiblesses documentées**
- **LinkedIn uniquement** — pas WhatsApp, pas Instagram (Surfe.com/pricing 2026)
- **Per seat** ($17–49/user/mois) — cher à l'échelle : 4 users × $49 = $196/mois pour 1 seul canal
- Pas de digest ni d'intelligence commerciale

**Pricing** — Starter $17 / Essential $29 / Pro $49 — per user/mois, annual ([surfe.com/pricing](https://www.surfe.com/pricing/))

**Adresse Marc** — ❌ 1 canal sur 2 (oublie WhatsApp) + $196/mois pour 4 users LinkedIn only

---

### TimelinesAI *(spécialiste WhatsApp)*

**Identité** — WhatsApp → CRM. Per seat. Shared inbox + automation.

**Forces réelles**
- WhatsApp perso fonctionnel, multi-device
- Prix d'entrée bas ($8/seat)
- Shared inbox utile pour équipes avec gestion collective
- 10j trial sans CB

**Faiblesses documentées**
- **WhatsApp uniquement** — pas LinkedIn ([timelines.ai/pricing](https://timelines.ai/timelinesai-pricing))
- Per seat — scalabilité limitée pour Frédéric (20 seats × $20 = $400/mois pour WA seul)
- Pas d'intelligence commerciale

**Pricing** — Automation $8/seat → CRM Integration $20/seat → Shared Inbox $40/mois → Mass Messaging $60/mois

**Adresse Marc** — ❌ 1 canal sur 2 (oublie LinkedIn) + $80/mois pour 4 users WA only

---

### LeadCRM *(entrée de gamme LinkedIn)*

**Identité** — Extension Chrome LinkedIn → CRM. Moins connu que Surfe.

**Forces** — Free plan ; intègre HubSpot, Pipedrive, Salesforce, Zoho, Google Sheets

**Faiblesses** — LinkedIn seulement ; moins mature que Surfe ; pas de WhatsApp

**Pricing** — Free (10 contacts/mois) + paid (prix exact non public, bas selon Capterra)

**Adresse Marc** — ❌ LinkedIn seulement, utile pour entrée de gamme uniquement

---

## Matrice de positionnement *(axée sur valeurs Marc)*

| Critère | **Axell** | SyncIn | Surfe | TimelinesAI | Ne rien faire |
|---|---|---|---|---|---|
| WhatsApp perso | ✅ | ✅ | ❌ | ✅ | ✅ |
| LinkedIn → CRM | ✅ | ✅ | ✅ | ❌ | ✅ |
| Multi-canal en 1 produit | ✅ | ⚠️ HubSpot only | ❌ | ❌ | ❌ |
| Intelligence (digest, signaux, priorisation) | ✅ | ❌ | ❌ | ❌ | ❌ |
| Tarifé par canal (pas par siège) | ✅ | ❌ | ❌ | ❌ | — |
| Multi-CRM | ✅ | ⚠️ | ✅ | ✅ | — |
| Prix < 90€ pour 4 users × 2 canaux | ✅ | ⚠️ | ❌ | ⚠️ | ✅ |
| RGPD / données UE | ✅ | ✅ | ⚠️ | ⚠️ | — |

---

## Positionnement différenciant

**Zone gagnée** — Multi-canal + intelligence commerciale dans un seul produit, au prix d'un seul canal concurrent

**Phrase de positionnement**
*"Contrairement à empiler Surfe ($196/mois, LinkedIn seulement) + TimelinesAI ($80/mois, WhatsApp seulement) pour 4 commerciaux — Axell connecte tous tes canaux à ton CRM existant pour 89€/mois et te dit chaque matin quels deals relancer en premier."*

**3 arguments non-comparables**
1. Seul outil qui couvre WhatsApp perso + LinkedIn + Instagram dans un même flux CRM sans changer de CRM
2. Intelligence commerciale native (signaux chaleur, digest priorisé) — pas juste du sync
3. Tarifé par canal : plus tu connectes de canaux, plus tu paies — pas plus tu recrutes

**Angles morts honnêtes**
- Surfe enrichit les données de contact mieux qu'Axell (profil LinkedIn complet → CRM) → reframing : Axell capture les *conversations*, Surfe enrichit les *profils* — complémentaires, pas concurrents
- SyncIn est connu en France, pricing potentiellement plus bas → reframing : sync pur sans intelligence = tu sais ce qui s'est passé, pas quoi faire ensuite

---

## Battlecards

```
CONCURRENT : Surfe
QUAND IL APPARAÎT : prospect mentionne LinkedIn + Pipedrive/HubSpot, connaît Surfe
SON MESSAGING : "Sync LinkedIn → CRM, enrichis les données, gagne 15h/mois"
POURQUOI LE PROSPECT LE CONSIDÈRE : réputation G2, spécialiste LinkedIn reconnu
COMMENT RÉPONDRE : "Surfe est excellent pour LinkedIn — mais tes commerciaux
  ferment aussi des deals sur WhatsApp. Pour 4 personnes, Surfe seul = $196/mois
  pour un seul canal. Axell couvre les deux canaux pour 89€ — et te dit en plus
  quels deals prioriser chaque matin."
QUESTION QUI FAIT RÉFLÉCHIR : "Tes deals se closent uniquement sur LinkedIn,
  ou aussi sur WhatsApp ?"
ARGUMENT DÉCISIF : 4 commerciaux × 2 canaux → Axell 89€ vs Surfe+TimelinesAI ~$276/mois
```

```
CONCURRENT : TimelinesAI
QUAND IL APPARAÎT : prospect parle de WhatsApp CRM, shared inbox
SON MESSAGING : "WhatsApp professionnel, partagé, connecté au CRM"
POURQUOI LE PROSPECT LE CONSIDÈRE : prix bas ($8/seat), fonctionnel sur WA
COMMENT RÉPONDRE : "Pour WhatsApp c'est correct. Mais tes commerciaux prospectent
  aussi sur LinkedIn — et là il faut un deuxième outil, une deuxième intégration,
  un deuxième abonnement."
QUESTION QUI FAIT RÉFLÉCHIR : "Combien de tes deals initiés sur LinkedIn ? Tu peux
  te permettre de ne pas les tracer ?"
ARGUMENT DÉCISIF : Axell = WhatsApp + LinkedIn + intelligence commerciale, même prix
```

```
CONCURRENT : SyncIn
QUAND IL APPARAÎT : prospect connaît SyncIn, cherche WA + LinkedIn → CRM en 1 outil
SON MESSAGING : "Zéro saisie manuelle, sync temps réel, setup 5 min"
POURQUOI LE PROSPECT LE CONSIDÈRE : couvre les 2 canaux, français, installation rapide
COMMENT RÉPONDRE : "SyncIn synchronise — et s'arrête là. Axell ajoute ce qui
  manque : quels deals sont chauds, qui relancer, ton digest du matin. Tu ne
  sais plus juste ce qui s'est passé — tu sais quoi faire après."
QUESTION QUI FAIT RÉFLÉCHIR : "Ton problème c'est que les données ne sont pas
  dans le CRM, ou c'est aussi que tu ne sais pas quels deals prioriser ?"
ARGUMENT DÉCISIF : SyncIn = miroir du passé. Axell = copilote du futur.
```

```
CONCURRENT : Ne rien faire
QUAND IL APPARAÎT : "ça marche comme ça depuis longtemps"
SON MESSAGING : pas de risque, pas de changement
POURQUOI LE PROSPECT LE CONSIDÈRE : peur d'un nouvel échec outil, habitude
COMMENT RÉPONDRE : "OK. Le deal LinkedIn de février — celui à 18k€ dans tes DM
  que tu as failli perdre. Ça arrive combien de fois par trimestre ?"
QUESTION QUI FAIT RÉFLÉCHIR : "Si tu rattrapais 1 deal oublié par trimestre,
  ça ferait quoi sur ton CA annuel ?"
ARGUMENT DÉCISIF : 1 deal rattrapé = ROI annuel Axell payé en un seul closing.
  Le coût du statu quo est invisible — pas nul.
```

---

## Utilisation pipeline

- `/pricing` — Pricing par canal validé vs concurrence per seat ; argument ROI battlecard → justification
- `/offer-final` — Phrases positionnement + battlecards à adapter pour one-pager et démo Marc
