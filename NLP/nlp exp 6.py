from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "plays", "studies",
         "studying", "connected", "connection",
         "beautiful", "easily"]

print("Original Word\tStemmed Word")
print("------------------------------")

for word in words:
    print(word, "\t\t", ps.stem(word))
