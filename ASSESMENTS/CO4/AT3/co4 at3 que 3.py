sentence = "She saw the man with a telescope."

print("Sentence:")
print(sentence)

print("\nPossible Interpretations:")

print("\nInterpretation 1:")
print("She used a telescope to see the man.")
print("Structure: saw -> with a telescope")

print("\nInterpretation 2:")
print("The man had a telescope.")
print("Structure: man -> with a telescope")

print("\nCFG:")
print("Generates both possible interpretations.")

print("\nPCFG:")
print("Assigns probabilities to the possible interpretations.")

probability1 = 0.75
probability2 = 0.25

print("\nProbability of Interpretation 1:", probability1)
print("Probability of Interpretation 2:", probability2)

if probability1 > probability2:
    print("\nPCFG Selected Interpretation 1.")
else:
    print("\nPCFG Selected Interpretation 2.")

print("\nNeural Parsing:")
print("Learns ambiguity resolution from large training data.")

print("\nConclusion:")
print("Neural parsing is generally more effective for real-world NLP.")
