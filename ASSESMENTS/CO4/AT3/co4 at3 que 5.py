sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nSentence:")
print(sentence)

print("\nTransition-Based Parsing:")

stack = []
buffer = words.copy()

while buffer:
    word = buffer.pop(0)
    stack.append(word)
    print("SHIFT ->", word)

print("\nFinal Stack:")
print(stack)

print("\nDependency Relations:")

if len(words) >= 2:
    root = words[1]

    for word in words:
        if word != root:
            print(root, "->", word)

print("\nGraph-Based Parsing:")
print("Creates possible dependency relationships.")
print("Evaluates different possible dependency trees.")
print("Selects the highest-scoring tree.")

print("\nComparison:")
print("Transition-Based: Fast and makes decisions step-by-step.")
print("Graph-Based: More global analysis but computationally expensive.")

print("\nConclusion:")
print("Transition-based parsing is more suitable for large-scale applications")
print("because it provides faster parsing performance.")
