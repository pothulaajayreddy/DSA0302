import math

sentence = ["economic", "growth", "increases", "employment"]

initial_tags = ["JJ", "NN", "NNS", "NN"]

print("INITIAL POS TAGS")
for word, tag in zip(sentence, initial_tags):
    print(word, "->", tag)

# Transformation-Based Tagging
corrected_tags = initial_tags.copy()

for i in range(1, len(corrected_tags)):
    if corrected_tags[i] == "NNS" and corrected_tags[i - 1] == "NN":
        corrected_tags[i] = "VBZ"

print("\nCORRECTED POS TAGS")
for word, tag in zip(sentence, corrected_tags):
    print(word, "->", tag)

# Frequency Analysis
frequency = {
    "economic": 120,
    "growth": 450,
    "increases": 210,
    "employment": 380
}

total = sum(frequency.values())

print("\nWORD FREQUENCY DISTRIBUTION")
for word, count in frequency.items():
    probability = count / total
    print(word, ":", count, "Probability =", round(probability, 4))

print("\nTOTAL WORD FREQUENCY =", total)

# Entropy of frequency distribution
entropy = 0

for count in frequency.values():
    p = count / total
    entropy -= p * math.log2(p)

print("\nENTROPY OF WORD DISTRIBUTION =", round(entropy, 4), "bits")

# Simple uncertainty before and after tagging
before = [0.5, 0.5]
after = [0.9, 0.1]

entropy_before = -sum(p * math.log2(p) for p in before)
entropy_after = -sum(p * math.log2(p) for p in after)

print("\nTAG UNCERTAINTY")
print("Before transformation =", round(entropy_before, 4), "bits")
print("After transformation  =", round(entropy_after, 4), "bits")

if entropy_after < entropy_before:
    print("Uncertainty decreased after transformation.")
else:
    print("Uncertainty did not decrease.")
