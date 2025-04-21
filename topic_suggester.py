import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

df = pd.read_csv("linkedin_posts.csv")

# Vectorize post content
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["content"].fillna(""))

# Cluster into 5 topic groups (adjustable)
kmeans = KMeans(n_clusters=5, random_state=42)
df["topic_cluster"] = kmeans.fit_predict(X)

# Topic suggestions
def suggest_topics(n=3):
    topic_counts = df["topic_cluster"].value_counts().head(n).index
    topics = []
    for cluster in topic_counts:
        idx = np.where(kmeans.labels_ == cluster)[0]
        cluster_terms = np.mean(X[idx].toarray(), axis=0).argsort()[-5:]
        suggested_terms = [vectorizer.get_feature_names_out()[i] for i in cluster_terms]
        topics.append(", ".join(suggested_terms))
    return topics

# Example
if __name__ == "__main__":
    topics = suggest_topics()
    print("Suggested topics based on top clusters:")
    for topic in topics:
        print(f"- {topic}")
