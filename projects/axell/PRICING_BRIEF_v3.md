# PRICING_BRIEF_v3.md
- Date : 2026-04-25 | Version : 3.0 | Agent : pricing | Type offre : A (SaaS récurrent)
- Personas : Marc (DG fondateur 10–35 sal.) + Frédéric (DG structuré 80–150 sal.)
- Unité : CANAL | Coûts réels vérifiés : Unipile **5 €/canal/mois** + **0,02 €/crédit**

---

## Corrections v2 → v3

| Anomalie v2 | Valeur v2 | Valeur v3 corrigée |
|---|---|---|
| Coût crédits Growth (estimé) | ~5 € | **~16 €** (800 cr × 0,02 €) |
| Coût crédits Scale | ~11 € | **~36 €** (1 800 cr) |
| Coût crédits Enterprise | ~21 € | **~70 €** (3 500 cr) |
| Marge brute Growth | 49 % | **37 %** |
| Marge brute Scale | 40 % | **30 %** |
| Marge brute Enterprise | 34 % | **30 %** (prix relevé) |
| Prix Scale | 169 € | **179 €** |
| Prix Enterprise | 299 € | **349 €** |
| Canal + (crédits inclus / prix) | +300 cr / 14 € | **+100 cr / 16 €** |
| Recharge 5 000 cr | **79 € ❌** (coût 100 €) | **119 €** |
| Recharge 15 000 cr | **199 € ❌** (coût 300 €) | **349 €** |
| Recharge 50 000 cr | **549 € ❌** (coût 1 000 €) | **1 190 €** |
| Remise revendeur | 40 % (non viable) | **25 %** |

---

## Structure de coûts vérifiée

```
Par canal/mois (coûts directs Axell) :
  Connexion Unipile (fixe)  : 5,00 €
  Usage IA (0,02 €/crédit)  : variable selon consommation
  ─────────────────────────────────────────────
  Coût minimum par canal     : 5,00 € + crédits consommés
```

### Sensibilité à la consommation de crédits

| Profil d'usage | Crédits/canal/mois | Coût IA/canal | Coût total/canal |
|---|---|---|---|
| Léger (~50 messages traités) | ~100 cr | 2,00 € | **7,00 €** |
| Modéré (~150 messages) | ~200 cr | 4,00 € | **9,00 €** |
| Intensif (~300 messages) | ~400 cr | 8,00 € | **13,00 €** |

**Règle de conception des tiers** : les crédits inclus couvrent le profil **léger**. Profil modéré → recharge nécessaire (~1 pack M/trimestre). Profil intensif → recharge mensuelle. Les recharges sont rentables pour Axell (voir section Recharges).

---

## Valeur économique (inchangée depuis v2)

### Pour Marc (4 commerciaux × 2 canaux = 8 canaux)

| Levier | Hypothèse | Valeur/an |
|---|---|---|
| Temps saisie économisé | 4 com × 4h/sem × 25 €/h × 52 sem | **20 800 €** |
| Deals rattrapés | 2 deals/trim × 12 000 € × 30 % marge | **7 200 €** |
| **Valeur totale estimée** | | **~28 000 €/an** |
| **Prix value-based (10–20 %)** | | **233–467 €/mois** |

> Growth 89 € = **64 % sous le plancher value-based**. Fort levier de fidélisation et d'upsell.

### Pour Frédéric (20 commerciaux × 1,5 canal = 30 canaux)

| Levier | Hypothèse | Valeur/an |
|---|---|---|
| Temps saisie économisé | 20 com × 4h/sem × 25 €/h × 52 sem | **104 000 €** |
| Réduction écart forecast | 150 k€ récupérés × 20 % closing × 30 % marge | **9 000 €** |
| **Valeur totale estimée** | | **~113 000 €/an** |
| **Prix value-based (10–20 %)** | | **942–1 883 €/mois** |

> Enterprise 349 € = **largement sous son budget max (300–800 €/mois)**.

---

## Architecture de tiers v3

| | **Starter** | **Growth** ⭐ | **Scale** | **Enterprise** |
|---|---|---|---|---|
| **Canaux inclus** | 3 | 8 | 18 | 35 |
| **Crédits inclus/mois** | 300 | 800 | 1 800 | 3 500 |
| **Prix HT/mois** | **59 €** | **89 €** | **179 €** | **349 €** |
| **Coût Unipile** | 15 € | 40 € | 90 € | 175 € |
| **Coût crédits inclus** | 6 € | 16 € | 36 € | 70 € |
| **Coût total** | 21 € | 56 € | 126 € | 245 € |
| **Marge brute** | **64 %** | **37 %** | **30 %** | **30 %** |
| **Pour qui** | 1–2 com, pilote | Marc 3–4 com × 2 canaux | Marc 8+ com / Frédéric pilote | Frédéric 15–17 com |

**Canal supplémentaire :** +16 €/mois, +100 crédits — coût direct ~7 € — **marge 56 %**

> ⚠️ Les marges ci-dessus sont calculées sur les **crédits inclus uniquement**. Si un client consomme 2× les crédits inclus et achète une recharge, la marge Axell reste positive (voir Recharges). Suivre la consommation réelle dès les premiers pilotes.

---

## Recharges v3 (corrigées — toutes rentables)

| Pack | Crédits | Prix HT | Coût réel | Marge |
|---|---|---|---|---|
| Recharge XS | 2 000 | **49 €** | 40 € | 18 % |
| Recharge M | 5 000 | **119 €** | 100 € | 16 % |
| Recharge L | 15 000 | **349 €** | 300 € | 14 % |
| Recharge XL | 50 000 | **1 190 €** | 1 000 € | 16 % |

**Tarif effectif recharge :** 0,0238 €/crédit — légèrement au-dessus du coût de 0,02 €.

> ⚠️ En v2 : 5 000 cr → 79 € (coût 100 €, **perte −21 €**) / 15 000 cr → 199 € (coût 300 €, **perte −101 €**) / 50 000 cr → 549 € (coût 1 000 €, **perte −451 €**). Ces prix sont invalidés et ne doivent pas être communiqués.

---

## Logique crédits IA (inchangée)

1 crédit = 1 action IA (analyse message, détection signal, génération digest)

| Action | Crédits |
|---|---|
| Message WhatsApp traité | 2 cr |
| Message LinkedIn traité | 2 cr |
| Email traité | 2 cr |
| Digest quotidien généré | ~50 cr |
| Détection signal (deal chaud) | 5 cr |

Consommation typique 8 canaux (usage modéré) : ~1 800–2 200 crédits/mois.

> Avec 800 crédits inclus dans Growth (usage léger), un client modéré consommera ~1 000 crédits supplémentaires/mois → 1 Recharge XS à 49 €. Dépense totale : 89 + 49 = **138 €/mois** — toujours < Surfe seul pour 4 users ($196/mois).

---

## Comparatif concurrentiel (4 commerciaux × 2 canaux)

| Solution | Prix/mois | Canaux | Intelligence | Total mensuel |
|---|---|---|---|---|
| **Axell Growth (inclus)** | **89 €** | WA + LI + autres | ✅ Digest + signaux | **89 €** |
| **Axell Growth (usage modéré)** | 89 + 49 | WA + LI + autres | ✅ | **138 €** |
| Surfe (LinkedIn) | $49/user | LinkedIn seul | ❌ | **~196 $** |
| TimelinesAI (WA) | $20/seat | WhatsApp seul | ❌ | **~80 $** |
| Surfe + TimelinesAI | — | 2 canaux séparés | ❌ | **~276 $** |
| SyncIn | ~$15/profil | WA + LI (HubSpot) | ❌ | **~60 $** (sync pur) |

**Argument clé Marc :** Axell Growth à usage modéré (138 €) < Surfe seul LinkedIn ($196) — pour 2 canaux + intelligence incluse.

---

## Frais additionnels (inchangés)

- **Setup (optionnel)** — Config initiale : 290 € one-shot
- **Support premium** — inclus Growth+ ; standard Starter (doc + email)

---

## Pricing revendeur v3

| Partenaire | Remise | Prix revendeur Growth | Marge Axell | Marge revendeur |
|---|---|---|---|---|
| Revendeur actif | **25 %** | **67 €** | 11 € **(20 %)** | 22 € |
| Apporteur | 15 % | 75,65 € | 20 € (35 %) | 13,35 € |
| Prescripteur | 5–10 % | 80–85 € | 24–28 € (43–50 %) | 4–9 € |

> ⚠️ En v2 la remise revendeur était de 40 %, calculée sur des marges erronées. À 40 %, Axell recevait 53 € pour Growth (coût 56 €) → **perte de 3 €/client/mois**. La remise est ramenée à **25 %** pour préserver une marge minimale de 20 % après remise.

**Projection MRR revendeur (Growth 89 €, remise 25 %) :**

| Clients équipés | Pack moyen | MRR revendeur | MRR Axell net |
|---|---|---|---|
| 10 clients | Growth | **220 €/mois** | 110 €/mois |
| 20 clients | Growth | **440 €/mois** | 220 €/mois |
| 30 clients | Growth | **660 €/mois** | 330 €/mois |

---

## Points de vigilance

1. **Consommation crédits réelle** : les crédits inclus couvrent le profil léger. Mesurer dès les premiers pilotes le pourcentage de clients qui dépassent le quota inclus — si > 50 %, relever les inclusions ou baisser le seuil de déclenchement de recharge.

2. **Enterprise marge sensible** : 30 % de marge sur crédits inclus, mais Frédéric est un utilisateur intensif probable (15–20 com, multi-canaux). Anticiper un achat de Recharge L régulier → marge additionnelle de ~49 € (14 %) par recharge.

3. **Programme revendeur** : mettre à jour `OFFER_FINAL_REVENDEUR_v2.md` — les tableaux de marges revendeur (36 €/mois sur Growth) et la remise 40 % sont invalidés. Nouveau chiffre : **22 €/mois sur Growth** à remise 25 %.

4. **Alerte Scale > 18 canaux** : au-delà de 20 commerciaux × 2 canaux = 40 canaux, il faudra un tier Grands Comptes ou pricing custom. Conserver la règle v2 : anticiper avant de prospecter Frédéric activement.

---

## Justifications prêtes (mises à jour)

**ROI Marc :**
*"Pour un DG avec 4 commerciaux, Axell économise ~4h de saisie/sem/commercial — soit 20 800 €/an en temps libéré, plus les deals rattrapés. ROI atteint en moins de 4 jours de travail économisé."*

**Comparaison concurrence (avec recharge) :**
*"À usage modéré, Axell + une recharge mensuelle = 138 €. Surfe pour LinkedIn seul pour 4 personnes = 196 $. Pour deux canaux, intelligence incluse, et un seul outil."*

**Argument canal vs siège :**
*"La plupart des outils facturent par utilisateur. Nous facturons par canal. Avec 4 commerciaux sur 2 canaux, tu paies 8 canaux — pas 4 sièges."*

---

## Réponses objections prix (mises à jour)

| Objection | Réponse |
|---|---|
| *"Trop cher"* | À usage modéré (89 + 49 recharge) = 138 €. Surfe seul pour 4 users = 196 $. |
| *"SyncIn est moins cher"* | SyncIn sync pur, HubSpot-centric, pas d'intelligence. Axell te dit quoi faire, pas juste ce qui s'est passé. |
| *"Pas de budget"* | 89 € = 3,5h de temps commercial économisé/mois. 1 deal rattrapé = 12 mois d'Axell payés. |
| *"Je fais avec Zapier"* | Zapier ne comprend pas les signaux commerciaux. Et tu maintiens les zaps toi-même. |
| *"Trop cher pour Frédéric"* | Enterprise 349 € pour 35 canaux. Surfe pour 20 users = 980 $/mois. |

---

## Utilisation pipeline

- `/offer-final` — Mettre à jour les prix Scale (179 €) et Enterprise (349 €) dans `OFFER_FINAL_v2.md` ; Growth 89 € inchangé
- `OFFER_FINAL_REVENDEUR_v2.md` — Mettre à jour : remise 25 % (vs 40 %), MRR revendeur 22 €/mois (vs 36 €) sur Growth
- `/competitive-intel` — Argument pricing conservé (Growth 89 € vs Surfe ~196 $)
