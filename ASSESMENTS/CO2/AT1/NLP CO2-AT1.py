# Morphological Analysis Pipeline

words = ["connected", "connecting", "connection"]

print("-" * 75)
print("{:<15}{:<15}{:<10}{:<18}{:<15}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))
print("-" * 75)

for word in words:

    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        mtype = "Inflectional"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        mtype = "Inflectional"

    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        mtype = "Derivational"

    else:
        root = word
        suffix = "-"
        mtype = "-"

    normalized = "connect"

    print("{:<15}{:<15}{:<10}{:<18}{:<15}".format(
        word, root, suffix, mtype, normalized))
