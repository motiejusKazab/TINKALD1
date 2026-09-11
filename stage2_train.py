import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# 1. Užkrauname 1 500 imtį
df = pd.read_csv("working_sample_1500.csv")
text_col = [c for c in df.columns if c != "doc_id"][0]

# 2. Teksto valymo funkcija
def clean_headline(text):
    text = str(text)
    text = re.sub(r'^\d+\s+', '', text)          # Šalina skaičius pradžioje
    text = re.sub(r'\([A-Za-z\s]+\)', '', text)  # Šalina miestus skliausteliuose
    text = re.sub(r'[^\w\s]', '', text)          # Šalina skyrybos ženklus
    return text.lower().strip()

df['cleaned_text'] = df[text_col].apply(clean_headline)

# 3. Vektorizavimas
vectorizer = CountVectorizer(stop_words='english', max_df=0.95, min_df=2)
tf_matrix = vectorizer.fit_transform(df['cleaned_text'])
feature_names = vectorizer.get_feature_names_out()

# 4. LDA modelio mokymas (K = 3 pagal hipotezę)
K_TOPICS = 3
lda = LatentDirichletAllocation(n_components=K_TOPICS, random_state=42, learning_method='online')
lda.fit(tf_matrix)

# 5. Raktinių žodžių išvedimas
print(f"--- LDA MODELIO REZULTATAI (K = {K_TOPICS}) ---\n")
for topic_idx, topic in enumerate(lda.components_):
    top_words = [feature_names[i] for i in topic.argsort()[:-11:-1]]
    print(f"Tema #{topic_idx + 1}: {', '.join(top_words)}")