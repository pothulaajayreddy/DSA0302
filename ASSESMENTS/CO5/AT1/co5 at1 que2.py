# Q2: Constraint-Based Dialog Planning

user_input = "I have an important exam tomorrow but I’m not able to concentrate."

responses = [
    "Since your exam is tomorrow, take a short break and then focus on one topic at a time. Stay confident because steady effort can help you prepare well.",
    
    "Your exam is important, so take a short break and remove distractions before studying. This can improve your focus and help you feel confident.",
    
    "If you cannot concentrate for your exam, take a short break and return with a clear focus. You can prepare well and feel confident with regular study."
]

print("USER INPUT:")
print(user_input)

print("\nDIALOG ACT:")
print("Advise + Encourage")

print("\nCONSTRAINTS:")
print("1. Maintain exam and concentrate")
print("2. Use Cause-Effect or Elaboration")
print("3. Include focus, break or confident")
print("4. Response length: 2 sentences")
print("5. Positive and logical response")

print("\nGENERATED RESPONSES:")

for i, response in enumerate(responses, 1):
    print("\nResponse", i, ":")
    print(response)

print("\nEVALUATION:")

for i, response in enumerate(responses, 1):
    keywords = ["focus", "break", "confident"]
    count = sum(word in response.lower() for word in keywords)

    if count >= 2 and len(response.split(". ")) >= 2:
        result = "Satisfies constraints"
    else:
        result = "Needs improvement"

    print("Response", i, ":", result)

print("\nBEST RESPONSE:")
print(responses[0])
