# Q4: Constraint-Based Syntactic and Semantic Interpretation

sentence = "The student saw the professor with the telescope."

print("INPUT SENTENCE:")
print(sentence)

print("\nPOSSIBLE INTERPRETATIONS:")

print("\nInterpretation 1:")
print("The student used the telescope to see the professor.")

print("\nInterpretation 2:")
print("The professor had the telescope.")

print("\nCONSTRAINT ANALYSIS:")

interpretation1 = {
    "syntax": "with the telescope modifies the action saw",
    "semantic": "student uses telescope",
    "role": "Instrument"
}

interpretation2 = {
    "syntax": "with the telescope modifies professor",
    "semantic": "professor possesses telescope",
    "role": "Possession"
}

print("\nInterpretation 1:")
for key, value in interpretation1.items():
    print(key, ":", value)

print("\nInterpretation 2:")
for key, value in interpretation2.items():
    print(key, ":", value)

print("\nCONSTRAINTS USED:")
print("1. Syntactic attachment")
print("2. Semantic compatibility")
print("3. Contextual interpretation")
print("4. Semantic role labeling")

print("\nSELECTED INTERPRETATION:")
print("The student used the telescope to see the professor.")

print("\nSEMANTIC ROLES:")
print("Agent     : Student")
print("Action    : Saw")
print("Patient   : Professor")
print("Instrument: Telescope")
