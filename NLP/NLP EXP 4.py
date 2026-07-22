def plural_fsm(word):
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"
    else:
        return word + "s"


word = input("Enter a singular noun: ")

plural = plural_fsm(word)

print("Singular:", word)
print("Plural:", plural)
