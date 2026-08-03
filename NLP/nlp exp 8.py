import random

# Training data
training_data = {
    "NOUN": ["ram", "boy", "girl", "cat", "dog", "cricket", "apple"],
    "VERB": ["is", "are", "play", "plays", "eat", "eats", "run", "runs"],
    "ADJECTIVE": ["big", "small", "good", "beautiful"],
    "ADVERB": ["quickly", "slowly", "beautifully"]
}

sentence = input("Enter a sentence: ").lower().split()

print("\nPredicted POS Tags:\n")

for word in sentence:
    found = False

    for tag in training_data:
        if word in training_data[tag]:
            print(word, ":", tag)
            found = True
            break

    if not found:
        print(word, ":", random.choice(list(training_data.keys())))
