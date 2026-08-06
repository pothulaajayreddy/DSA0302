# Inflectional Morphology Normalization

words = ["create", "creates", "creating"]

for word in words:

    if word == "create":
        suffix = "None"
        grammar = "Base Form"
        root = "create"

    elif word.endswith("es"):
        suffix = "-es"
        grammar = "Third Person Singular"
        root = "create"

    elif word.endswith("ing"):
        suffix = "-ing"
        grammar = "Present Participle"
        root = "create"

    else:
        suffix = "Unknown"
        grammar = "Unknown"
        root = word

    print("-----------------------------------------------")
    print("Original Word :", word)
    print("Suffix        :", suffix)
    print("Grammar       :", grammar)
    print("Root Word     :", root)
    print("Normalized    :", root)
