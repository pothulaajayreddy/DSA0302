# Experiment 10: Transformation-Based Tagging

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

tags = []

# Initial tagging
for word in words:
    if word in ["the", "a", "an"]:
        tags.append("DET")
    elif word in ["is", "am", "are", "was", "were", "to"]:
        tags.append("VERB")
    elif word in ["quickly", "slowly", "very"]:
        tags.append("ADV")
    else:
        tags.append("NOUN")

# Transformation rule:
# Word after "to" is usually a verb
for i in range(1, len(words)):
    if words[i - 1] == "to":
        tags[i] = "VERB"

print("\nTransformation-Based Tags:")
for word, tag in zip(words, tags):
    print(word, "->", tag)
    
