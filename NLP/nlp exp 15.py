# Experiment 15: Probabilistic CFG

grammar = {
    "S": [
        (["NP", "VP"], 1.0)
    ],

    "NP": [
        (["Det", "N"], 0.6),
        (["N"], 0.4)
    ],

    "VP": [
        (["V", "NP"], 0.7),
        (["V"], 0.3)
    ],

    "Det": [
        (["the"], 0.5),
        (["a"], 0.5)
    ],

    "N": [
        (["boy"], 0.5),
        (["dog"], 0.5)
    ],

    "V": [
        (["sees"], 0.5),
        (["runs"], 0.5)
    ]
}

sentence = input("Enter sentence: ").lower().split()

def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and symbol == words[pos]:
            return pos + 1, 1.0
        return None, 0

    best_pos = None
    best_prob = 0

    for rule, probability in grammar[symbol]:
        current = pos
        total_prob = probability
        valid = True

        for item in rule:
            result_pos, result_prob = parse(
                item, words, current
            )

            if result_pos is None:
                valid = False
                break

            current = result_pos
            total_prob *= result_prob

        if valid and total_prob > best_prob:
            best_pos = current
            best_prob = total_prob

    return best_pos, best_prob

position, probability = parse("S", sentence, 0)

if position == len(sentence):
    print("Sentence accepted.")
    print("Probability:", probability)
else:
    print("Sentence rejected.")
