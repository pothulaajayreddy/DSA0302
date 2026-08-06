# Morphological Processing System

words = ["analyzing", "analysis", "analytical"]

for word in words:

    if word.endswith("ing"):
        root = "analyze"
        affix = "-ing"
        transformation = "Inflectional"
        normalized = "analyze"

    elif word.endswith("sis"):
        root = "analyze"
        affix = "-sis"
        transformation = "Derivational"
        normalized = "analyze"

    elif word.endswith("ical"):
        root = "analyze"
        affix = "-ical"
        transformation = "Derivational"
        normalized = "analyze"

    else:
        root = word
        affix = "None"
        transformation = "Base"
        normalized = word

    print("-----------------------------------------------")
    print("Original Word :", word)
    print("Root Word     :", root)
    print("Affix         :", affix)
    print("Type          :", transformation)
    print("Normalized    :", normalized)
