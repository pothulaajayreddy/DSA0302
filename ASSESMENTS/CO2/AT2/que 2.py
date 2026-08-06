# Morphological Parser

words = ["disagree", "agreement", "agreeable"]

for word in words:

    prefix = "None"
    suffix = "None"
    semantic = ""
    category = ""

    if word.startswith("dis"):
        prefix = "dis-"
        root = "agree"
        category = "Derivational"
        semantic = "Negative meaning"

    elif word.endswith("ment"):
        suffix = "-ment"
        root = "agree"
        category = "Derivational"
        semantic = "State or result"

    elif word.endswith("able"):
        suffix = "-able"
        root = "agree"
        category = "Derivational"
        semantic = "Capable of being agreed"

    else:
        root = word
        category = "Base"
        semantic = "Base form"

    print("-----------------------------------------------")
    print("Original Word :", word)
    print("Prefix        :", prefix)
    print("Root Word     :", root)
    print("Suffix        :", suffix)
    print("Category      :", category)
    print("Meaning       :", semantic)
    print("Normalized    :", root)
