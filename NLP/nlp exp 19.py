# Experiment 19: Lesk Word Sense Disambiguation

from nltk.corpus import wordnet as wn

def simple_lesk(sentence, word):

    context = set(sentence.lower().split())

    best_sense = None
    max_overlap = 0

    for sense in wn.synsets(word):

        definition_words = set(
            sense.definition().lower().split()
        )

        overlap = len(context.intersection(definition_words))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense, max_overlap


sentence = input("Enter a sentence: ")
word = input("Enter ambiguous word: ")

sense, score = simple_lesk(sentence, word)

if sense:
    print("\nSelected Sense:")
    print("Synset:", sense.name())
    print("Definition:", sense.definition())
    print("Overlap Score:", score)
else:
    print("No suitable sense found.")
