sentences = [
    "Book a flight ticket now.",
    "This book is interesting."
]

pos_tags = {
    "Book": "VB",
    "a": "DT",
    "flight": "NN",
    "ticket": "NN",
    "now": "RB",
    "This": "DT",
    "book": "NN",
    "is": "VBZ",
    "interesting": "JJ"
}

for sentence in sentences:
    print("\nSentence:", sentence)
    print("POS Tags:")

    for word in sentence.replace(".", "").split():
        print(word, "->", pos_tags[word])

p_book_VB = 0.6
p_book_NN = 0.4
p_start_VB = 0.5
p_start_NN = 0.5

prob_VB = p_start_VB * p_book_VB
prob_NN = p_start_NN * p_book_NN

print("\nHMM Calculation")
print("----------------")
print("P(Book, VB) =", prob_VB)
print("P(Book, NN) =", prob_NN)

if prob_VB > prob_NN:
    print("Book is predicted as: VB (Verb)")
else:
    print("Book is predicted as: NN (Noun)")

total = prob_VB + prob_NN

print("\nNormalized Probability")
print("P(VB | Book) =", prob_VB / total)
print("P(NN | Book) =", prob_NN / total)
