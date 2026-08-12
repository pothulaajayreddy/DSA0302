import math
from collections import Counter

corpus = "Data science is powerful, data science drives innovation, data science is evolving."

words = corpus.lower().replace(",", "").replace(".", "").split()

unigram = Counter(words)
bigram = Counter(zip(words, words[1:]))
trigram = Counter(zip(words, words[1:], words[2:]))

# Q1: MLE P(science | data)
p_science_given_data = bigram[("data", "science")] / unigram["data"]

print("1. MLE P(science | data) =", p_science_given_data)

# Q2: Backoff for "data science improves"
word = "improves"

if trigram[("data", "science", word)] > 0:
    probability = trigram[("data", "science", word)] / bigram[("data", "science")]
elif bigram[("science", word)] > 0:
    probability = bigram[("science", word)] / unigram["science"]
elif unigram[word] > 0:
    probability = unigram[word] / len(words)
else:
    probability = 0

print("2. Backoff P(improves | data science) =", probability)

# Q3: Deleted Interpolation for "data science is"
lambda1 = 0.5
lambda2 = 0.3
lambda3 = 0.2

p_trigram = trigram[("data", "science", "is")] / bigram[("data", "science")]
p_bigram = bigram[("science", "is")] / unigram["science"]
p_unigram = unigram["is"] / len(words)

interpolated_probability = (
    lambda1 * p_trigram +
    lambda2 * p_bigram +
    lambda3 * p_unigram
)

print("3. Deleted Interpolation Probability =", interpolated_probability)

# Q4: Entropy
p_is = 0.66
p_drives = 0.33

entropy = -(p_is * math.log2(p_is) + p_drives * math.log2(p_drives))

print("4. Entropy =", entropy, "bits")
