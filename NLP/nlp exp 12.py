# Experiment 12: Simple Earley Parser

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["the"], ["a"]],
    "N": [["boy"], ["girl"], ["dog"], ["cat"]],
    "V": [["sees"], ["likes"], ["runs"]]
}

sentence = input("Enter sentence: ").lower().split()
n = len(sentence)

chart = [[] for _ in range(n + 1)]

def add(state, index):
    if state not in chart[index]:
        chart[index].append(state)

# State format:
# (lhs, rhs, dot, start)

for rule in grammar["S"]:
    add(("S", tuple(rule), 0, 0), 0)

for i in range(n + 1):
    changed = True

    while changed:
        changed = False

        for state in chart[i].copy():
            lhs, rhs, dot, start = state

            if dot < len(rhs):
                next_symbol = rhs[dot]

                # Predictor
                if next_symbol in grammar:
                    for rule in grammar[next_symbol]:
                        new_state = (
                            next_symbol,
                            tuple(rule),
                            0,
                            i
                        )
                        if new_state not in chart[i]:
                            chart[i].append(new_state)
                            changed = True

                # Scanner
                elif i < n and next_symbol == sentence[i]:
                    new_state = (
                        lhs,
                        rhs,
                        dot + 1,
                        start
                    )
                    add(new_state, i + 1)

            else:
                # Completer
                for old_state in chart[start].copy():
                    old_lhs, old_rhs, old_dot, old_start = old_state

                    if old_dot < len(old_rhs):
                        if old_rhs[old_dot] == lhs:
                            new_state = (
                                old_lhs,
                                old_rhs,
                                old_dot + 1,
                                old_start
                            )

                            if new_state not in chart[i]:
                                chart[i].append(new_state)
                                changed = True

accepted = False

for state in chart[n]:
    lhs, rhs, dot, start = state

    if lhs == "S" and dot == len(rhs) and start == 0:
        accepted = True

if accepted:
    print("Sentence is accepted by Earley Parser.")
else:
    print("Sentence is rejected by Earley Parser.")
