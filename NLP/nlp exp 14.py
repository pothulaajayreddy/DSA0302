# Experiment 14: Subject-Verb Agreement

singular_subjects = ["boy", "girl", "cat", "dog", "student"]
plural_subjects = ["boys", "girls", "cats", "dogs", "students"]

singular_verbs = ["runs", "eats", "plays", "likes"]
plural_verbs = ["run", "eat", "play", "like"]

sentence = input("Enter a simple sentence: ").lower().split()

if len(sentence) != 3:
    print("Please enter a sentence in the form: The boy runs")
else:
    determiner = sentence[0]
    subject = sentence[1]
    verb = sentence[2]

    if subject in singular_subjects and verb in singular_verbs:
        print("Agreement is correct.")

    elif subject in plural_subjects and verb in plural_verbs:
        print("Agreement is correct.")

    else:
        print("Agreement error.")
