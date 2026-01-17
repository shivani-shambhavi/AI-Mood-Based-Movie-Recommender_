
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend(df, user_text, top_n=None):
    vectorizer = TfidfVectorizer(stop_words='english')
    matrix = vectorizer.fit_transform(df['text'])
    user_vec = vectorizer.transform([user_text])
    scores = cosine_similarity(user_vec, matrix).flatten()
    df = df.copy()
    df['score'] = scores
    df = df.sort_values(by='score', ascending=False)
    return df if top_n is None else df.head(top_n)
