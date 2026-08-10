import re
import math
from collections import Counter, defaultdict


# =========================================================
# PENN TREEBANK TAGSET
# =========================================================

TAG_NAMES = {
    "NN": "Noun",
    "NNS": "Plural Noun",
    "VB": "Verb",
    "VBD": "Past Verb",
    "VBG": "Gerund",
    "VBN": "Past Participle",
    "VBP": "Present Verb",
    "VBZ": "3rd Person Verb",
    "JJ": "Adjective",
    "RB": "Adverb",
    "PRP": "Pronoun",
    "DT": "Determiner",
    "IN": "Preposition",
    "CC": "Conjunction",
    "MD": "Modal",
    "CD": "Number",
    "RP": "Particle"
}


# =========================================================
# TRAINING CORPUS
# =========================================================

training_data = [
    "the/DT student/NN is/VBZ intelligent/JJ",
    "the/DT student/NN is/VBZ hardworking/JJ",
    "the/DT student/NN reads/VBZ books/NNS",
    "the/DT student/NN studies/VBZ computer/NN science/NN",
    "the/DT student/NN writes/VBZ programs/NNS",
    "the/DT student/NN learns/VBZ programming/NN",

    "the/DT teacher/NN is/VBZ intelligent/JJ",
    "the/DT teacher/NN teaches/VBZ computer/NN science/NN",
    "the/DT teacher/NN explains/VBZ the/DT lesson/NN",
    "the/DT teacher/NN helps/VBZ the/DT student/NN",

    "the/DT programmer/NN writes/VBZ programs/NNS",
    "the/DT programmer/NN develops/VBZ software/NN",
    "the/DT programmer/NN tests/VBZ the/DT program/NN",
    "the/DT programmer/NN learns/VBZ python/NN",

    "the/DT computer/NN is/VBZ fast/JJ",
    "the/DT computer/NN is/VBZ powerful/JJ",
    "the/DT computer/NN processes/VBZ data/NN",
    "the/DT computer/NN runs/VBZ programs/NNS",

    "a/DT good/JJ student/NN works/VBZ hard/RB",
    "a/DT good/JJ teacher/NN explains/VBZ lessons/NNS",
    "the/DT intelligent/JJ student/NN solves/VBZ problems/NNS",
    "the/DT young/JJ programmer/NN writes/VBZ code/NN",

    "students/NNS are/VBP learning/VBG programming/NN",
    "teachers/NNS are/VBP teaching/VBG students/NNS",
    "programmers/NNS are/VBP developing/VBG software/NN",

    "the/DT student/NN can/MD learn/VB programming/NN",
    "the/DT programmer/NN can/MD write/VB programs/NNS",
    "the/DT teacher/NN can/MD teach/VB students/NNS",

    "the/DT student/NN works/VBZ in/IN the/DT laboratory/NN",
    "the/DT teacher/NN works/VBZ in/IN the/DT college/NN",
    "the/DT programmer/NN works/VBZ on/IN software/NN",

    "the/DT student/NN reads/VBZ and/CC writes/VBZ",
    "the/DT teacher/NN explains/VBZ and/CC teaches/VBZ",
    "the/DT programmer/NN designs/VBZ and/CC tests/VBZ"
]


# =========================================================
# CONVERT TRAINING DATA
# =========================================================

tagged_sentences = []

for sentence in training_data:

    tokens = sentence.split()
    tagged_sentence = []

    for token in tokens:

        word, tag = token.rsplit("/", 1)

        tagged_sentence.append(
            (word.lower(), tag)
        )

    tagged_sentences.append(tagged_sentence)


# =========================================================
# BUILD COUNTS
# =========================================================

word_tag_counts = defaultdict(Counter)
tag_counts = Counter()
transition_counts = defaultdict(Counter)


for sentence in tagged_sentences:

    previous_tag = "<START>"

    for word, tag in sentence:

        word_tag_counts[word][tag] += 1
        tag_counts[tag] += 1

        transition_counts[previous_tag][tag] += 1

        previous_tag = tag

    transition_counts[previous_tag]["<END>"] += 1


# =========================================================
# MOST FREQUENT TAG
# =========================================================

most_frequent_tag = {}

for word in word_tag_counts:

    most_frequent_tag[word] = (
        word_tag_counts[word]
        .most_common(1)[0][0]
    )


# =========================================================
# TOKENIZER
# =========================================================

def tokenize(sentence):

    return re.findall(
        r"[A-Za-z]+|\d+",
        sentence.lower()
    )


# =========================================================
# RULE-BASED POS TAGGER
# =========================================================

def rule_based_tag(sentence):

    words = tokenize(sentence)

    result = []

    dictionary = {

        "the": "DT",
        "a": "DT",
        "an": "DT",

        "i": "PRP",
        "you": "PRP",
        "he": "PRP",
        "she": "PRP",
        "it": "PRP",
        "we": "PRP",
        "they": "PRP",

        "is": "VBZ",
        "am": "VBP",
        "are": "VBP",
        "was": "VBD",
        "were": "VBD",
        "be": "VB",
        "can": "MD",
        "will": "MD",
        "should": "MD",

        "and": "CC",
        "or": "CC",
        "but": "CC",

        "in": "IN",
        "on": "IN",
        "at": "IN",
        "to": "IN",
        "from": "IN",
        "with": "IN",
        "for": "IN",

        "student": "NN",
        "teacher": "NN",
        "programmer": "NN",
        "computer": "NN",
        "program": "NN",
        "software": "NN",
        "data": "NN",
        "science": "NN",
        "book": "NN",
        "lesson": "NN",
        "college": "NN",
        "laboratory": "NN",
        "python": "NN",
        "code": "NN",

        "students": "NNS",
        "teachers": "NNS",
        "programmers": "NNS",
        "programs": "NNS",
        "books": "NNS",
        "problems": "NNS",
        "lessons": "NNS",

        "good": "JJ",
        "intelligent": "JJ",
        "hardworking": "JJ",
        "fast": "JJ",
        "powerful": "JJ",
        "young": "JJ",
        "useful": "JJ",

        "hard": "RB",
        "quickly": "RB",
        "slowly": "RB",

        "read": "VB",
        "write": "VB",
        "learn": "VB",
        "teach": "VB",
        "work": "VB",
        "solve": "VB",
        "develop": "VB",
        "test": "VB",
        "study": "VB",

        "reads": "VBZ",
        "writes": "VBZ",
        "learns": "VBZ",
        "teaches": "VBZ",
        "works": "VBZ",
        "solves": "VBZ",
        "develops": "VBZ",
        "tests": "VBZ",
        "explains": "VBZ",
        "helps": "VBZ",
        "processes": "VBZ",
        "runs": "VBZ",
        "designs": "VBZ",

        "reading": "VBG",
        "writing": "VBG",
        "learning": "VBG",
        "teaching": "VBG",
        "studying": "VBG",
        "developing": "VBG"
    }

    for i, word in enumerate(words):

        if word in dictionary:
            tag = dictionary[word]

        elif word.isdigit():
            tag = "CD"

        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ed"):
            tag = "VBD"

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("ous"):
            tag = "JJ"

        elif word.endswith("ful"):
            tag = "JJ"

        elif word.endswith("ness"):
            tag = "NN"

        elif word.endswith("s"):
            tag = "NNS"

        else:
            tag = "NN"

        result.append((word, tag))

    # -----------------------------
    # GRAMMATICAL RULES
    # -----------------------------

    for i in range(len(result)):

        word, tag = result[i]

        # After modal -> verb
        if i > 0:

            previous_word, previous_tag = result[i - 1]

            if previous_tag == "MD":

                result[i] = (word, "VB")

        # After "to" -> verb
        if i > 0:

            previous_word, previous_tag = result[i - 1]

            if previous_word == "to":

                result[i] = (word, "VB")

        # Adjective before noun
        if i < len(result) - 1:

            next_word, next_tag = result[i + 1]

            if next_tag in ["NN", "NNS"]:

                if tag == "NN" and word not in [
                    "the",
                    "a",
                    "an"
                ]:

                    result[i] = (word, "JJ")

    return result


# =========================================================
# STOCHASTIC POS TAGGER
# =========================================================

def emission_probability(word, tag):

    total = sum(
        word_tag_counts[word].values()
    )

    count = word_tag_counts[word][tag]

    if total == 0:
        return 1e-6

    if count == 0:
        return 1e-6

    probability = count / total

    return max(probability, 1e-6)


# =========================================================
# FIXED TRANSITION PROBABILITY
# =========================================================

def transition_probability(
    previous_tag,
    current_tag
):

    total = sum(
        transition_counts[previous_tag].values()
    )

    count = transition_counts[
        previous_tag
    ][current_tag]

    if total == 0:
        return 1e-6

    if count == 0:
        return 1e-6

    probability = count / total

    return max(probability, 1e-6)


# =========================================================
# STOCHASTIC TAGGER USING VITERBI
# =========================================================

def stochastic_tag(sentence):

    words = tokenize(sentence)

    if not words:
        return []

    tags = list(tag_counts.keys())

    viterbi = []
    backpointer = []

    # -----------------------------------------------------
    # FIRST WORD
    # -----------------------------------------------------

    first_scores = {}
    first_back = {}

    for tag in tags:

        transition = transition_probability(
            "<START>",
            tag
        )

        emission = emission_probability(
            words[0],
            tag
        )

        # Extra protection against log(0)
        transition = max(transition, 1e-6)
        emission = max(emission, 1e-6)

        score = (
            math.log(transition)
            +
            math.log(emission)
        )

        first_scores[tag] = score
        first_back[tag] = None

    viterbi.append(first_scores)
    backpointer.append(first_back)

    # -----------------------------------------------------
    # REMAINING WORDS
    # -----------------------------------------------------

    for i in range(1, len(words)):

        current_scores = {}
        current_back = {}

        for current_tag in tags:

            emission = emission_probability(
                words[i],
                current_tag
            )

            emission = max(emission, 1e-6)

            best_score = float("-inf")
            best_previous = None

            for previous_tag in viterbi[i - 1]:

                transition = transition_probability(
                    previous_tag,
                    current_tag
                )

                transition = max(
                    transition,
                    1e-6
                )

                score = (
                    viterbi[i - 1][previous_tag]
                    +
                    math.log(transition)
                    +
                    math.log(emission)
                )

                if score > best_score:

                    best_score = score
                    best_previous = previous_tag

            current_scores[current_tag] = best_score
            current_back[current_tag] = best_previous

        viterbi.append(current_scores)
        backpointer.append(current_back)

    # -----------------------------------------------------
    # FIND BEST FINAL TAG
    # -----------------------------------------------------

    best_final_tag = max(
        viterbi[-1],
        key=viterbi[-1].get
    )

    best_tags = [best_final_tag]

    # -----------------------------------------------------
    # BACKTRACK
    # -----------------------------------------------------

    for i in range(
        len(words) - 1,
        0,
        -1
    ):

        previous_tag = backpointer[i][
            best_tags[-1]
        ]

        best_tags.append(previous_tag)

    best_tags.reverse()

    return list(zip(words, best_tags))


# =========================================================
# TRANSFORMATION-BASED TAGGER
# =========================================================

def initial_transformation_tags(sentence):

    words = tokenize(sentence)

    result = []

    for word in words:

        if word in most_frequent_tag:

            tag = most_frequent_tag[word]

        else:

            tag = "NN"

        result.append([word, tag])

    return result


def transformation_based_tag(sentence):

    result = initial_transformation_tags(sentence)

    # Rule 1:
    # After pronoun -> verb

    for i in range(len(result)):

        word, tag = result[i]

        if i > 0:

            previous_word, previous_tag = result[i - 1]

            if previous_tag == "PRP":

                if tag in ["NN", "NNS"]:

                    result[i][1] = "VB"

    # Rule 2:
    # After modal -> verb

    for i in range(len(result)):

        word, tag = result[i]

        if i > 0:

            previous_word, previous_tag = result[i - 1]

            if previous_tag == "MD":

                result[i][1] = "VB"

    # Rule 3:
    # After "to" -> verb

    for i in range(len(result)):

        word, tag = result[i]

        if i > 0:

            previous_word, previous_tag = result[i - 1]

            if previous_word == "to":

                result[i][1] = "VB"

    # Rule 4:
    # Adjective before noun

    for i in range(len(result) - 1):

        word, tag = result[i]

        next_word, next_tag = result[i + 1]

        if next_tag in ["NN", "NNS"]:

            if tag == "NN":

                result[i][1] = "JJ"

    # Rule 5:
    # Words ending in ing -> VBG

    for i in range(len(result)):

        word, tag = result[i]

        if word.endswith("ing"):

            result[i][1] = "VBG"

    # Rule 6:
    # Words ending in ly -> RB

    for i in range(len(result)):

        word, tag = result[i]

        if word.endswith("ly"):

            result[i][1] = "RB"

    return [
        tuple(item)
        for item in result
    ]


# =========================================================
# DISPLAY RESULT
# =========================================================

def display_result(title, result):

    print("\n")
    print("=" * 70)
    print(title)
    print("=" * 70)

    print(
        f"{'WORD':<20}"
        f"{'TAG':<10}"
        f"MEANING"
    )

    print("-" * 70)

    for word, tag in result:

        description = TAG_NAMES.get(
            tag,
            "Other"
        )

        print(
            f"{word:<20}"
            f"{tag:<10}"
            f"{description}"
        )


# =========================================================
# RULE-BASED ONLY
# =========================================================

def run_rule_based():

    print("\nRULE-BASED POS TAGGING")

    sentence = input(
        "Enter an English sentence: "
    )

    result = rule_based_tag(sentence)

    display_result(
        "RULE-BASED POS TAGGER",
        result
    )


# =========================================================
# STOCHASTIC ONLY
# =========================================================

def run_stochastic():

    print("\nSTOCHASTIC POS TAGGING")

    sentence = input(
        "Enter an English sentence: "
    )

    result = stochastic_tag(sentence)

    display_result(
        "STOCHASTIC POS TAGGER",
        result
    )


# =========================================================
# TRANSFORMATION BASED ONLY
# =========================================================

def run_transformation():

    print("\nTRANSFORMATION-BASED POS TAGGING")

    sentence = input(
        "Enter an English sentence: "
    )

    result = transformation_based_tag(sentence)

    display_result(
        "TRANSFORMATION-BASED POS TAGGER",
        result
    )


# =========================================================
# COMPARE ALL THREE
# =========================================================

def compare_taggers():

    print("\n")
    print("=" * 70)
    print("COMPARISON OF THREE POS TAGGING METHODS")
    print("=" * 70)

    sentence = input(
        "\nEnter an English sentence: "
    )

    print(
        "\nInput Sentence:",
        sentence
    )

    # Rule Based
    rule_result = rule_based_tag(sentence)

    display_result(
        "1. RULE-BASED POS TAGGER",
        rule_result
    )

    # Stochastic
    stochastic_result = stochastic_tag(sentence)

    display_result(
        "2. STOCHASTIC POS TAGGER",
        stochastic_result
    )

    # Transformation Based
    transformation_result = (
        transformation_based_tag(sentence)
    )

    display_result(
        "3. TRANSFORMATION-BASED POS TAGGER",
        transformation_result
    )


# =========================================================
# DISPLAY PENN TREEBANK TAGSET
# =========================================================

def display_tagset():

    print("\n")
    print("=" * 70)
    print("PENN TREEBANK TAGSET")
    print("=" * 70)

    for tag, meaning in TAG_NAMES.items():

        print(
            f"{tag:<10} {meaning}"
        )


# =========================================================
# MAIN PROGRAM
# =========================================================

print("\n")
print("=" * 70)
print("PYTHON POS TAGGING SYSTEM")
print("=" * 70)

print(
    "\nTraining corpus loaded successfully."
)

print(
    "Number of training sentences:",
    len(tagged_sentences)
)

print(
    "Vocabulary size:",
    len(word_tag_counts)
)

print(
    "\nPenn Treebank POS tags are used."
)


while True:

    print("\n")
    print("-" * 70)
    print("MAIN MENU")
    print("-" * 70)

    print("1. Rule-Based POS Tagger")
    print("2. Stochastic POS Tagger")
    print("3. Transformation-Based Tagger")
    print("4. Compare All Three Taggers")
    print("5. Display Penn Treebank Tagset")
    print("6. Exit")

    choice = input(
        "\nEnter your choice: "
    )

    if choice == "1":

        run_rule_based()

    elif choice == "2":

        run_stochastic()

    elif choice == "3":

        run_transformation()

    elif choice == "4":

        compare_taggers()

    elif choice == "5":

        display_tagset()

    elif choice == "6":

        print(
            "\nProgram terminated successfully."
        )

        break

    else:

        print(
            "\nInvalid choice. Please enter 1 to 6."
        )
