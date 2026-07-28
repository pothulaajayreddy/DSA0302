states = ['q0', 'q1', 'q2']
alphabet = ['a', 'b']

transition = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

start_state = 'q0'
final_states = ['q2']

string = input("Enter input string: ")

current_state = start_state
path = current_state

for symbol in string:
    if symbol in alphabet:
        current_state = transition[current_state][symbol]
        path = path + " → " + current_state
    else:
        print("Invalid Symbol")
        break
else:
    print("Transition Path:")
    print(path)

    if current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")
