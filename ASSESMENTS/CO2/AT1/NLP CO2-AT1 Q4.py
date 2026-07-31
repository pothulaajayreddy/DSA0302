# Finite-State Morphological Parser

words = ["writes", "writing", "written"]

print("-" * 120)
print("{:<12}{:<25}{:<25}{:<15}{:<22}{:<15}".format(
    "Word", "State Transition", "Morphological Breakdown",
    "Root", "Classification", "Normalized"))
print("-" * 120)

for word in words:

    if word.endswith("ing"):
        transition = "q0 -> q1 -> q3"
        breakdown = "write + ing"
        root = "write"
        mtype = "Regular Inflection"

    elif word.endswith("s"):
        transition = "q0 -> q1 -> q2"
        breakdown = "write + s"
        root = "write"
        mtype = "Regular Inflection"

    elif word == "written":
        transition = "q0 -> q4"
        breakdown = "written -> write"
        root = "write"
        mtype = "Irregular Inflection"

    else:
        transition = "-"
        breakdown = "-"
        root = word
        mtype = "-"

    normalized = root

    print("{:<12}{:<25}{:<25}{:<15}{:<22}{:<15}".format(
        word, transition, breakdown,
        root, mtype, normalized))
