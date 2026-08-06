# Morphology-Based Normalization

words = ["govern", "government", "governance"]

for word in words:

    if word == "govern":
        root = "govern"
        affix = "None"
        level = "Base"

    elif word.endswith("ment"):
        root = "govern"
        affix = "-ment"
        level = "Level 1 Derivation"

    elif word.endswith("ance"):
        root = "govern"
        affix = "-ance"
        level = "Level 1 Derivation"

    else:
        root = word
        affix = "None"
        level = "Unknown"

    print("-----------------------------------------------")
    print("Original Word :", word)
    print("Root Word     :", root)
    print("Affix         :", affix)
    print("Derivation    :", level)
    print("Normalized    :", root)
