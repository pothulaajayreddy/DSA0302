subject = input("Enter subject: ").lower()
verb = input("Enter verb: ").lower()

singular_subjects = ["he", "she", "it"]
plural_subjects = ["they", "we", "students"]

singular_verbs = ["runs", "eats", "plays"]
plural_verbs = ["run", "eat", "play"]

print("\nFeature Structure:")
print("Subject:", subject)
print("Verb:", verb)

if subject in singular_subjects:
    subject_number = "singular"
elif subject in plural_subjects:
    subject_number = "plural"
else:
    subject_number = "unknown"

if verb in singular_verbs:
    verb_number = "singular"
elif verb in plural_verbs:
    verb_number = "plural"
else:
    verb_number = "unknown"

print("Subject Number:", subject_number)
print("Verb Number:", verb_number)

if subject_number == verb_number:
    print("\nResult: Grammatically Correct")
else:
    print("\nResult: Grammatical Error")

print("\nSubcategorization:")
print("Verb requires appropriate arguments to form a valid sentence.")

print("\nConclusion:")
print("Feature structures provide better support for enforcing grammatical constraints.")
