Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============= RESTART: C:/Users/ajayk/Downloads/nlp/co3 at3 que1.py ============
Sentence: She likes music

CFG Tree Structure:
S
|-- NP
|   |-- She
|-- VP
    |-- V
    |   |-- likes
    |-- NP
        |-- music

Dependency Structure:
likes -> She
likes -> music

Conclusion:
CFG shows hierarchical sentence structure.
Dependency parsing directly shows word relationships.
Dependency parsing is better for capturing relationships between words.

============ RESTART: C:/Users/ajayk/Downloads/nlp/co4 at3 que 2.py ============
Enter a sentence: i like

Input Words:
['i', 'like']

Top-Down Parsing:
Starts from the start symbol and tries to generate the input.
It may have difficulty with ambiguity and incomplete input.

Earley Parsing:
Scans the input from left to right.
It can handle ambiguous and incomplete grammatical structures.

Input is incomplete.
Earley parsing is more suitable for this condition.

Conclusion:
Earley parsing is more suitable for real-time dynamic input.

============ RESTART: C:/Users/ajayk/Downloads/nlp/co4 at3 que 3.py ============
Sentence:
She saw the man with a telescope.

Possible Interpretations:

Interpretation 1:
She used a telescope to see the man.
Structure: saw -> with a telescope

Interpretation 2:
The man had a telescope.
Structure: man -> with a telescope

CFG:
Generates both possible interpretations.

PCFG:
Assigns probabilities to the possible interpretations.

Probability of Interpretation 1: 0.75
Probability of Interpretation 2: 0.25

PCFG Selected Interpretation 1.

Neural Parsing:
Learns ambiguity resolution from large training data.

Conclusion:
Neural parsing is generally more effective for real-world NLP.

============ RESTART: C:/Users/ajayk/Downloads/nlp/co4 at3 que 4.py ============
Enter subject: she 
Enter verb: runs

Feature Structure:
Subject: she 
Verb: runs
Subject Number: unknown
Verb Number: singular

Result: Grammatical Error

Subcategorization:
Verb requires appropriate arguments to form a valid sentence.

Conclusion:
Feature structures provide better support for enforcing grammatical constraints.
>>> 
============ RESTART: C:/Users/ajayk/Downloads/nlp/co4 at3 que 5.py ============
Enter a sentence: I love natural language processing

Sentence:
I love natural language processing

Transition-Based Parsing:
SHIFT -> I
SHIFT -> love
SHIFT -> natural
SHIFT -> language
SHIFT -> processing

Final Stack:
['I', 'love', 'natural', 'language', 'processing']

Dependency Relations:
love -> I
love -> natural
love -> language
love -> processing

Graph-Based Parsing:
Creates possible dependency relationships.
Evaluates different possible dependency trees.
Selects the highest-scoring tree.

Comparison:
Transition-Based: Fast and makes decisions step-by-step.
Graph-Based: More global analysis but computationally expensive.

Conclusion:
Transition-based parsing is more suitable for large-scale applications
because it provides faster parsing performance.
