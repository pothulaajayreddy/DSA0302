# Porter Stemmer-Based Preprocessing Module

words = ["relational", "relation", "relate"]

print("-" * 110)
print("{:<15}{:<25}{:<25}{:<15}".format(
    "Word", "Applied Rule", "Intermediate Form", "Final Stem"))
print("-" * 110)

for word in words:

    if word == "relational":
        rule = "ational -> ate"
        intermediate = "relate"
        final = "relat"

    elif word == "relation":
        rule = "ion removed"
        intermediate = "relate"
        final = "relat"

    elif word == "relate":
        rule = "Remove final e"
        intermediate = "relate"
        final = "relat"

    else:
        rule = "-"
        intermediate = word
        final = word

    print("{:<15}{:<25}{:<25}{:<15}".format(
        word, rule, intermediate, final))
