# Q5: Constraint-Based Natural Language Generation

input_sentence = "The student missed the assignment deadline because the submission portal was unavailable."

responses = [
    "The student missed the assignment deadline because the submission portal was unavailable. The student should contact the instructor and explain the issue politely.",
    
    "Since the submission portal was unavailable, the student could not submit the assignment before the deadline. The student should inform the instructor about the problem.",
    
    "The submission portal was unavailable, so the student missed the assignment deadline. The student can explain the technical problem and request further assistance."
]

print("INPUT:")
print(input_sentence)

print("\nENTITIES:")
print("1. Student")
print("2. Assignment")
print("3. Deadline")
print("4. Submission Portal")

print("\nSEMANTIC RELATION:")
print("Submission portal unavailable")
print("        ↓")
print("Student unable to submit assignment")
print("        ↓")
print("Assignment deadline missed")

print("\nDISCOURSE RELATION:")
print("CAUSE -> EFFECT")

print("\nGENERATED RESPONSES:")

for i, response in enumerate(responses, 1):
    print("\nResponse", i, ":")
    print(response)

print("\nCONSTRAINT EVALUATION:")

required_entities = [
    "student",
    "assignment",
    "deadline",
    "submission portal"
]

for i, response in enumerate(responses, 1):
    text = response.lower()

    satisfied = 0

    for entity in required_entities:
        if entity in text:
            satisfied += 1

    if satisfied == 4:
        print("Response", i, ": All entity constraints satisfied")
    else:
        print("Response", i, ": Some constraints not satisfied")

print("\nBEST RESPONSE:")
print(responses[1])
