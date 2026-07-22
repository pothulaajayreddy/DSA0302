from collections import defaultdict
import random

text = input("Enter training text: ")

words = text.split()

bigram_model = defaultdict(list)

for i in range(len(words) - 1):
    bigram_model[words[i]].append(words[i + 1])

print("\nBigram Model:")
for word in bigram_model:
    for next_word in bigram_model[word]:
        print(word, "->", next_word)

start_word = input("\nEnter starting word: ")
num_words = int(input("Enter number of words to generate: "))

generated_words = [start_word]
current_word = start_word

for i in range(num_words - 1):
    if current_word in bigram_model:
        next_word = random.choice(bigram_model[current_word])
        generated_words.append(next_word)
        current_word = next_word
    else:
        break

print("\nGenerated Text:")
print(" ".join(generated_words))
