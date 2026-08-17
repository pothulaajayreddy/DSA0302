# Experiment 13: Parse Tree

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["the"], ["a"]],
    "N": [["boy"], ["dog"], ["cat"]],
    "V": [["sees"], ["likes"], ["runs"]]
}

sentence = input("Enter sentence: ").lower().split()

def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return pos + 1, symbol
        return None, None

    for rule in grammar[symbol]:
        current = pos
        children = []
        success = True

        for item in rule:
            new_pos, child = parse(item, words, current)

            if child is None:
                success = False
                break

            children.append(child)
            current = new_pos

        if success:
            return current, (symbol, children)

    return None, None

def print_tree(tree, level=0):
    if isinstance(tree, str):
        print("  " * level + tree)
        return

    symbol, children = tree
    print("  " * level + symbol)

    for child in children:
        print_tree(child, level + 1)

position, tree = parse("S", sentence, 0)

if tree and position == len(sentence):
    print("\nParse Tree:")
    print_tree(tree)
else:
    print("Sentence cannot be parsed.")
