import re

sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nRule-Based POS Tags:\n")

for word in words:

    if re.fullmatch(r"\d+", word):
        tag = "NUMBER"

    elif re.fullmatch(r".*ing", word):
        tag = "VERB"

    elif re.fullmatch(r".*ed", word):
        tag = "VERB"

    elif re.fullmatch(r".*ly", word):
        tag = "ADVERB"

    elif re.fullmatch(r".*(ous|ful|able|ive|al|ic)", word):
        tag = "ADJECTIVE"

    elif word.lower() in ["is", "am", "are", "was", "were", "be", "has", "have", "do", "does"]:
        tag = "VERB"

    elif word.lower() in ["a", "an", "the"]:
        tag = "ARTICLE"

    elif word.lower() in ["in", "on", "at", "with", "to", "from", "of", "for"]:
        tag = "PREPOSITION"

    elif word.lower() in ["and", "or", "but"]:
        tag = "CONJUNCTION"

    elif word.lower() in ["he", "she", "it", "they", "we", "i", "you"]:
        tag = "PRONOUN"

    else:
        tag = "NOUN"

    print(word, ":", tag)
