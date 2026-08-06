# Morphological Parsing and Normalization

words = ["activate", "activation", "reactivation"]

for word in words:

    prefix = "None"
    suffix = "None"
    sequence = ""
    meaning = ""

    if word == "activate":
        root = "activate"
        sequence = "Base"
        meaning = "Perform action"

    elif word == "activation":
        root = "activate"
        suffix = "-ion"
        sequence = "activate + ion"
        meaning = "Process of activating"

    elif word == "reactivation":
        prefix = "re-"
        root = "activate"
        suffix = "-ion"
        sequence = "re + activate + ion"
        meaning = "Activate again"

    print("-----------------------------------------------")
    print("Original Word :", word)
    print("Prefix        :", prefix)
    print("Root Word     :", root)
    print("Suffix        :", suffix)
    print("Sequence      :", sequence)
    print("Meaning       :", meaning)
    print("Normalized    :", root)
