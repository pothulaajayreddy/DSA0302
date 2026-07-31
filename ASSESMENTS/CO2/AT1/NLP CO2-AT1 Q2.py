# Morphological Parsing Module for Sentiment Analysis

words = ["unhappy", "happiness", "happily"]

print("-" * 95)
print("{:<15}{:<10}{:<15}{:<10}{:<18}{:<25}{:<10}".format(
    "Word", "Prefix", "Base Form", "Suffix",
    "Type", "Morphological Breakdown", "Root"))
print("-" * 95)

for word in words:

    prefix = "-"
    suffix = "-"
    base = ""
    mtype = "Derivational"

    if word.startswith("un"):
        prefix = "un"
        base = "happy"
        breakdown = "un + happy"

    elif word.endswith("ness"):
        suffix = "ness"
        base = "happy"
        breakdown = "happy + ness"

    elif word.endswith("ly"):
        suffix = "ly"
        base = "happy"
        breakdown = "happy + ly"

    else:
        base = word
        breakdown = word

    print("{:<15}{:<10}{:<15}{:<10}{:<18}{:<25}{:<10}".format(
        word, prefix, base, suffix, mtype, breakdown, base))
