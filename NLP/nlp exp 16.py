# Experiment 16: Named Entity Recognition

import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter text: ")

doc = nlp(text)

print("\nNamed Entities:")

for entity in doc.ents:
    print(entity.text, "->", entity.label_)
