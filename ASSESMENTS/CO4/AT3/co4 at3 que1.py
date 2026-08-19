sentence = ["She", "likes", "music"]

print("Sentence:", " ".join(sentence))

print("\nCFG Tree Structure:")
print("S")
print("|-- NP")
print("|   |-- She")
print("|-- VP")
print("    |-- V")
print("    |   |-- likes")
print("    |-- NP")
print("        |-- music")

print("\nDependency Structure:")
print("likes -> She")
print("likes -> music")

print("\nConclusion:")
print("CFG shows hierarchical sentence structure.")
print("Dependency parsing directly shows word relationships.")
print("Dependency parsing is better for capturing relationships between words.")
