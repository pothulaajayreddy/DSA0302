sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nInput Words:")
print(words)

print("\nTop-Down Parsing:")
print("Starts from the start symbol and tries to generate the input.")
print("It may have difficulty with ambiguity and incomplete input.")

print("\nEarley Parsing:")
print("Scans the input from left to right.")
print("It can handle ambiguous and incomplete grammatical structures.")

if len(words) < 3:
    print("\nInput is incomplete.")
    print("Earley parsing is more suitable for this condition.")
else:
    print("\nInput contains multiple words.")
    print("Earley parsing is suitable for dynamic and ambiguous input.")

print("\nConclusion:")
print("Earley parsing is more suitable for real-time dynamic input.")
