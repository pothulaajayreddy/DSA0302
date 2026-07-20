import nltk

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

word = input("Enter a word: ")

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stem = stemmer.stem(word)
lemma = lemmatizer.lemmatize(word)

print("Original Word:", word)
print("Stemmed Word:", stem)
print("Lemmatized Word:", lemma)
