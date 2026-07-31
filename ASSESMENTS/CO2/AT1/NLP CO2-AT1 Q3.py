# Stemming-Based Preprocessing Module

words = ["played", "player", "playing"]

print("-" * 95)
print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
    "Original Word", "Stem", "Removed Affix",
    "Type", "Normalized Form"))
print("-" * 95)

for word in words:

    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        mtype = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        mtype = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        mtype = "Derivational"

    else:
        stem = word
        affix = "-"
        mtype = "-"

    normalized = stem

    print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
        word, stem, affix, mtype, normalized))
