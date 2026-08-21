# Q3: Constraint-Based Word Sense Disambiguation

sentence = "The bank by the river flooded after the storm, but it was saved by quick action."

senses = {
    "Financial Bank": ["money", "loan", "account", "ATM"],
    "Riverbank": ["river", "flooded", "storm", "water"]
}

context = sentence.lower()

scores = {}

for sense, words in senses.items():
    score = 0

    for word in words:
        if word in context:
            score += 1

    scores[sense] = score

best_sense = max(scores, key=scores.get)

print("INPUT SENTENCE:")
print(sentence)

print("\nAMBIGUOUS WORD:")
print("bank")

print("\nWORD SENSE SCORES:")
for sense, score in scores.items():
    print(sense, "=", score)

print("\nRESOLVED SENSE:")
print(best_sense)

print("\nCONSTRAINTS USED:")
print("1. Contextual constraint")
print("2. Semantic compatibility")
print("3. Discourse coherence")

print("\nPREDICATE LOGIC:")
print("riverbank(x) AND near(x, river)")
print("flood(x) AND after(flood, storm)")
print("saved(x, quick_action)")

print("\nPARAPHRASE:")
print("The riverbank near the river flooded after the storm, but quick action saved it.")

print("\nDISCOURSE RELATION:")
print("CONTRAST")
