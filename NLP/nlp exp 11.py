# Experiment 11: Top-Down Parser

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"], ["boy"]],
    "V": [["sees"], ["likes"], ["runs"]]
}

sentence = input("Enter sentence: ").lower().split()

def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and symbol == words[pos]:
            return pos + 1
        return None

    for rule in grammar[symbol]:
        current = pos
        success = True

        for item in rule:
            result = parse(item, words, current)

            if result is None:
                success = False
                break

            current = result

        if success:
            return current

    return None

result = parse("S", sentence, 0)

if result == len(sentence):
    print("Sentence is accepted by the grammar.")
else:
    print("Sentence is rejected by the grammar.")
