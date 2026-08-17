# Experiment 20: TF-IDF Information Retrieval

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Natural language processing deals with human language",
    "Machine learning is used in natural language processing",
    "Python is useful for machine learning",
    "Information retrieval searches and ranks documents"
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(
    documents + [query]
)

similarities = cosine_similarity(
    tfidf_matrix[-1],
    tfidf_matrix[:-1]
)

scores = similarities[0]

ranking = sorted(
    enumerate(scores),
    key=lambda x: x[1],
    reverse=True
)

print("\nDocument Ranking:")

for index, score in ranking:
    print(
        "Document", index + 1,
        "Score:", round(score, 3)
    )
    print(documents[index])
    print()
