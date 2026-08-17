# Experiment 18: Simple FOPC Parser

import re

expression = input("Enter FOPC expression: ")

pattern = r'^([A-Za-z][A-Za-z0-9_]*)\((.*?)\)$'

match = re.match(pattern, expression)

if match:
    predicate = match.group(1)
    arguments = match.group(2).split(",")

    print("\nFOPC Expression")
    print("Predicate:", predicate)

    print("Arguments:")

    for argument in arguments:
        argument = argument.strip()

        if argument.startswith("?"):
            print(argument, "-> Variable")
        else:
            print(argument, "-> Constant")

else:
    print("Invalid FOPC expression.")
