import nltk
nltk.download('wordnet')
# Experiment 17: WordNet

from nltk.corpus import wordnet as wn

word = input("Enter a word: ")

synsets = wn.synsets(word)

if len(synsets) == 0:
    print("No synsets found.")

else:
    print("\nWord Meanings:")

    for synset in synsets:
        print("\nSynset:", synset.name())
        print("Definition:", synset.definition())
        print("Examples:", synset.examples())

        print("Synonyms:",
              [lemma.name() for lemma in synset.lemmas()])
