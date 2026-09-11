# 1 Laboratorinis Darbas: Temų Modelio Mokymas (LDA)

**Atliko:** Motiejus  
**Dėstytojas:** M. Jankauskas  
**Metodai:** CountVectorizer, Latent Dirichlet Allocation (LDA)

---

## 1 Etapas: Pradinė analizė ir hipotezė

Atlikus pradinį duomenų valymą ir atsitiktinę 1 500 dokumentų atranką (`random_state=42`), išanalizuota 20 atsitiktinių antraščių imtis.

### Įžvalgos ir duomenų triukšmas:
1. **Sintetinis triukšmas:** Antraštėse pastebėti skaičiai pradžioje (pvz., `31`, `78`), miestų pavadinimai skliausteliuose `(Berlin)`, `(Vilnius)` ir pasikartojančios lietuviškos/angliškos frazės (`dėl rinkos reakcijos`, `amid concerns`).
2. **Kalba:** Tekstai pateikti anglų ir lietuvių kalbomis.

### Pradinė hipotezė:
- **Temų skaičius ($K$):** Nustatyta hipotezė $K = 3$ arba $K = 4$.
- **Numatomos temos:**
  1. *Sportas* (rungtynės, trenerių taktika, futbolas).
  2. *Technologijos / DI / Verslas* (Apple, iPhone, startuolių investicijos, ML bibliotekos).
  3. *Sensacijos / Clickbait* ("won't believe", "change life forever").

---

## 2 Etapas: Bazinio LDA modelio mokymas

Apmokytas pirmasis LDA modelis su $K=3$ ir pradiniu anglišku stop-žodžių filtru.

### Gauti rezultatai (K=3):
- **Tema #1:** *amid, concerns, toliau, kas, inflation, buy, reasons, gadget...* (Rinka ir Vartotojai)
- **Tema #2:** *ai, iphone, apple, naują, su, po, markets, kompiuterį...* (Technologijos ir DI)
- **Tema #3:** *believe, wont, record, forever, life, trick, change...* (Clickbait / Sensacijos)

**Išvada:** Modelis patvirtino hipotezę, tačiau išryškėjo problema – angliškas stop-žodžių filtras praleido lietuviškus jungtukus (`su`, `po`, `kas`) bei sintetinio triukšmo frazes (`amid`, `concerns`).

---

## 3 Etapas: Hiperparametrų eksperimentai ir įvertinimas

Įgyvendintas išplėstinis teksto valymas ir išplėstas custom stop-žodžių sąrašas (pašalinti lietuviški jungtukai ir sintetinis triukšmas). Palyginti 3 modeliai matuojant **Perplexity** (mažesnis rodiklis = geresnis matematinis pritaikymas).

### Eksperimentų rezultatai:

| Bandymas | Temų skaičius ($K$) | Perplexity | Temų kokybės vertinimas |
| :--- | :---: | :---: | :--- |
| **Bandymas A** | $K = 2$ | 148.34 | Per daug suplaktos temos (sportas ir infliacija vienoje temoje). |
| **Bandymas B** | $K = 3$ | 117.31 | Aiškios temos atitinkančios 1 etapo hipotezę. |
| **Bandymas C** | $K = 5$ | **94.77** | Geriausias perplexity, grynasis sporto ir trenerių taktikos išskyrimas. |

### Inferencijos testavimas (Naujų tekstų klasifikavimas):
Panaudojus apmokytą modelį nepermokant jo iš naujo, gauti šie rezultatai:
- *„New AI startup raised millions from investors“* $\rightarrow$ **Tema #3 (TIKIMYBĖ: 72.0%)** (Technologijos / DI).
- *„Treneris po rungtynių pakomentavo komandos gynybą“* $\rightarrow$ Atpažinta pagal žodžių struktūras.

---

## Galutinė Išvada

1. Sintetinio triukšmo ir skaičių pašalinimas iš antraščių iš esmės pagerino LDA temų atskyrimo kokybę.
2. $K=3$ hipotezė buvo teisinga bazinei struktūrai, tačiau matuojant pagal *Perplexity*, $K=5$ suteikia tikslesnį temų išskyrimą (atskiria sportą nuo bendrų naujienų).

## 4 Dalies Papildymas: Rekomendacijos ir Modelio Silpnybės

### Modelio silpnybės ir ribotumai:
1. **Konteksto ir žodžių tvarkos nepaisymas (Bag-of-Words apribojimas):** LDA remiasi tik žodžių dažnumu, todėl nesupranta sakinio sintaksės ar žodžių tvarkos.
2. **Daugiakalbiškumo iššūkis:** Duomenų rinkinyje esant ir lietuviškoms, ir angliškoms antraštėms, standartiniai angliški stop-žodžiai nepašalina lietuviškų jungtukų. Reikalingas dvikalbis valymas.
3. **Trumpų tekstų problema:** Antraštės yra trumpi tekstai (mažai žodžių viename dokumente), todėl LDA modeliui sunkiau sudaryti tvirtus statistinius ryšius nei ilguose straipsniuose.

### Rekomendacija tolesniam vystymui:
- Praktiniam naudojimui rekomenduojama rinktis **$K = 3$ arba $K = 5$** modelį su išplėstiniu custom stop-žodžių sąrašu.
- Jei siekiama geresnio konteksto supratimo ateityje, vertėtų išbandyti **BERT / RoBERTa (SBERT)** tekstų embedding'us su **BERTopic** modeliavimu, kuris kur kas geriau tvarkosi su trumpomis, keliakalbėmis antraštėmis.