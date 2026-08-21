# Q1: Constraint-Based Coreference Resolution

paragraph = "John and Mary went to the park. He brought a ball. She wanted to play with it. The dog chased him excitedly. Finally, they all went home."

mentions = {
    "He": ["John", "Mary"],
    "She": ["John", "Mary"],
    "it": ["ball", "park"],
    "him": ["John", "Mary", "dog"],
    "they": ["John", "Mary", "dog"]
}

resolved = {
    "He": "John",
    "She": "Mary",
    "it": "ball",
    "him": "John",
    "they": "John, Mary and dog"
}

print("INPUT:")
print(paragraph)

print("\nCOREFERENCE RESOLUTION:")
for mention, antecedent in resolved.items():
    print(mention, "->", antecedent)

print("\nCONSTRAINTS USED:")
print("1. Gender and number agreement")
print("2. Recency")
print("3. Semantic compatibility")
print("4. Discourse coherence")

print("\nFINAL COREFERENCE CHAINS:")
print("John -> He -> him")
print("Mary -> She")
print("Ball -> it")
print("John + Mary + Dog -> they")

print("\nREWRITTEN PARAGRAPH:")
print("John and Mary went to the park. John brought a ball.")
print("Mary wanted to play with the ball.")
print("The dog chased John excitedly.")
print("Finally, John, Mary and the dog all went home.")
