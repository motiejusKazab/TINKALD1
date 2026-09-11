import os
import pandas as pd

TRAIN_FILE = "headlines_train.csv"
RANDOM_STATE = 42
SAMPLE_SIZE = 1500
MANUAL_SAMPLE_SIZE = 20

def run_stage_1():
    if not os.path.exists(TRAIN_FILE):
        print(f"KLAIDA: Failas {TRAIN_FILE} nerastas.")
        return

    df = pd.read_csv(TRAIN_FILE)
    print(f"Pradinis įrašų skaičius: {len(df)}")

    # Pašaliname tarpus iš stulpelių pavadinimų (pvz., ' headline_text ' -> 'headline_text')
    df.columns = df.columns.str.strip()

    # Automatiškai ieškome teisingo stulpelio
    text_col = None
    possible_names = ["headline_text", "headline", "text", "title", "content"]
    
    for name in possible_names:
        if name in df.columns:
            text_col = name
            break
            
    # Jei neradome pagal pavadinimą, paimame pirmąjį tekstinį stulpelį
    if not text_col:
        text_col = df.columns[0]
        print(f"ĮSPĖJIMAS: Nerastas tikslus stulpelio pavadinimas. Naudojamas stulpelis: '{text_col}'")
    else:
        print(f"Rastas teksto stulpelis: '{text_col}'")

    # Duomenų valymas
    df[text_col] = df[text_col].astype(str).str.strip()
    df = df[df[text_col] != ""].drop_duplicates(subset=[text_col])
    cleaned_count = len(df)
    print(f"Po valymo liko įrašų: {cleaned_count}")

    # 1 500 atsitiktinė imtis
    if cleaned_count < SAMPLE_SIZE:
        df_sample = df.copy()
    else:
        df_sample = df.sample(n=SAMPLE_SIZE, random_state=RANDOM_STATE).reset_index(drop=True)

    df_sample["doc_id"] = [f"ID_{i}" for i in range(len(df_sample))]
    df_sample.to_csv("working_sample_1500.csv", index=False)
    print("Imtis išsaugota: 'working_sample_1500.csv'")

    # 20 antraščių rankinei analizei
    manual_sample = df_sample.sample(n=MANUAL_SAMPLE_SIZE, random_state=RANDOM_STATE).reset_index(drop=True)

    # Generuojame Markdown failą
    md_content = f"""# Pradinė analizė prieš mokymą (1 Etapas)

**Naudotas random_state:** {RANDOM_STATE}  
**Pradinis duomenų skaičius:** {len(df)}  
**Išvalytas duomenų skaičius:** {cleaned_count}  
**Darbinė imtis:** {len(df_sample)} dokumentų  

---

## Rankinė 20 atsitiktinių antraščių analizė

| Unikalus ID | Antraštė | Siūloma tema / Kategorija | Pastabos |
| :--- | :--- | :--- | :--- |
"""

    for _, row in manual_sample.iterrows():
        safe_text = str(row[text_col]).replace("|", "/")
        md_content += f"| {row['doc_id']} | {safe_text} |  |  |\n"

    md_content += """
---

## Pradinės hipotezės
- **Protu suvokiamas temų skaičius (K):** 
- **Galimos pagrindinės temos:**
  1. 
  2. 
  3. 
"""

    with open("initial-analysis.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    print("Sėkmingai sugeneruotas 'initial-analysis.md'!")

if __name__ == "__main__":
    run_stage_1()