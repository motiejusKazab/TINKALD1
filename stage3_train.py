import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# 1. Duomenų užkrovimas
df = pd.read_csv("working_sample_1500.csv")
text_col = [c for c in df.columns if c != "doc_id"][0]

# 2. Išplėstinis teksto valymas ir STOP-WORDS
CUSTOM_STOP_WORDS = [
    # Lietuviški pagalbiniai žodžiai
    'su', 'po', 'kas', 'toliau', 'del', 'dėl', 'ir', 'ne', 'tai', 'nuo', 'iki',
    # Sintetinis triukšmas, pastebėtas 1 ir 2 etapuose
    'amid', 'concerns', 'dėl rinkos reakcijos', 'rinkos', 'reakcijos'
]

def clean_text_advanced(text):
    text = str(text).lower()
    text = re.sub(r'^\d+\s+', '', text)          # Šalina skaičius pradžioje
    text = re.sub(r'\([a-z\s]+\)', '', text)     # Šalina miestus
    text = re.sub(r'[^\w\s]', '', text)          # Šalina skyrybos ženklus
    return text.strip()

df['cleaned_text'] = df[text_col].apply(clean_text_advanced)

# Sujungiame standartinius angliškus stop-žodžius su mūsų papildomais
from sklearn.feature_extraction import text
combined_stop_words = list(text.ENGLISH_STOP_WORDS.union(CUSTOM_STOP_WORDS))

# Vektorizavimas
vectorizer = CountVectorizer(stop_words=combined_stop_words, max_df=0.90, min_df=2)
tf_matrix = vectorizer.fit_transform(df['cleaned_text'])
feature_names = vectorizer.get_feature_names_out()

# 3. HIPERPARAMETRŲ EKSPERIMENTAI (3 Bandymai)
experiments = [
    {"name": "Bandymas A (K=2)", "k": 2},
    {"name": "Bandymas B (K=3 - Hipotezė)", "k": 3},
    {"name": "Bandymas C (K=5)", "k": 5}
]

trained_models = {}

print("==================================================")
print("   3 ETAPAS: HIPERPARAMETRŲ EKSPERIMENTAI")
print("==================================================\n")

for exp in experiments:
    k = exp["k"]
    lda = LatentDirichletAllocation(
        n_components=k, 
        random_state=42, 
        learning_method='online'
    )
    lda.fit(tf_matrix)
    
    # Skaičiuojame Perplexity (mažesnis skaičius = geresnis modelis)
    perplexity = lda.perplexity(tf_matrix)
    trained_models[exp["name"]] = (lda, perplexity)
    
    print(f"--- {exp['name']} | Perplexity: {perplexity:.2f} ---")
    for topic_idx, topic in enumerate(lda.components_):
        top_words = [feature_names[i] for i in topic.argsort()[:-9:-1]]
        print(f"  Tema #{topic_idx + 1}: {', '.join(top_words)}")
    print("-" * 50)

# 4. INFERENCIJA (Gynimo reikalavimas: Naujo teksto klasifikavimas)
print("\n==================================================")
print("   INFERENCIJOS TESTAVIMAS (Naujas tekstas)")
print("==================================================")

best_model = trained_models["Bandymas B (K=3 - Hipotezė)"][0]

def predict_topic(new_text):
    cleaned = clean_text_advanced(new_text)
    vec = vectorizer.transform([cleaned])
    topic_probs = best_model.transform(vec)[0]
    
    print(f"\nNauja antraštė: '{new_text}'")
    for idx, prob in enumerate(topic_probs):
        print(f"  Tema #{idx + 1} tikimybė: {prob:.4f}")

# Testuojame su dviem visiškai naujomis antraštėmis
predict_topic("New AI startup raised millions from investors")
predict_topic("Treneris po rungtynių pakomentavo komandos gynybą")