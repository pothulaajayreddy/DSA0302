import re
import math
from collections import Counter


# =========================================================
# TRAINING CORPUS
# =========================================================

training_corpus = """
The student is intelligent.
The student is hardworking.
The student is reading a book.
The student is learning programming.
The student is studying computer science.
The student is writing a program.
The student is solving problems.

The teacher is intelligent.
The teacher is hardworking.
The teacher is teaching computer science.
The teacher is explaining the lesson.
The teacher is reading a book.
The teacher is helping the student.

The computer is fast.
The computer is powerful.
The computer is running a program.
The computer is processing data.
The computer is connected to the network.

The programmer is writing a program.
The programmer is learning Python.
The programmer is solving problems.
The programmer is developing software.
The programmer is testing the program.

The class is interesting.
The class is useful.
The class is learning programming.
The class is studying computer science.
"""


# =========================================================
# SEPARATE TEST CORPUS
# =========================================================

test_corpus = """
The student is intelligent.
The student is learning programming.
The teacher is reading a book.
The computer is processing data.
The programmer is writing a program.
"""


# =========================================================
# PREPROCESSING
# =========================================================

def preprocess(text):

    text = text.lower()

    raw_sentences = re.split(
        r'[.!?]+',
        text
    )

    sentences = []

    for sentence in raw_sentences:

        words = re.findall(
            r'[a-z]+',
            sentence
        )

        if words:

            words = ['<s>'] + words + ['</s>']

            sentences.append(words)

    return sentences


training_sentences = preprocess(
    training_corpus
)

test_sentences = preprocess(
    test_corpus
)


# =========================================================
# BUILD N-GRAM COUNTS
# =========================================================

unigram_counts = Counter()
bigram_counts = Counter()
trigram_counts = Counter()


for sentence in training_sentences:

    # Unigram
    for word in sentence:

        unigram_counts[word] += 1

    # Bigram
    for i in range(
        len(sentence) - 1
    ):

        bigram = (
            sentence[i],
            sentence[i + 1]
        )

        bigram_counts[bigram] += 1

    # Trigram
    for i in range(
        len(sentence) - 2
    ):

        trigram = (
            sentence[i],
            sentence[i + 1],
            sentence[i + 2]
        )

        trigram_counts[trigram] += 1


# =========================================================
# PROBABILITY FUNCTIONS
# =========================================================

def unigram_probability(word):

    total = sum(
        unigram_counts.values()
    )

    if total == 0:

        return 0

    return (
        unigram_counts[word]
        / total
    )


def bigram_probability(
    word1,
    word2
):

    numerator = bigram_counts[
        (word1, word2)
    ]

    denominator = unigram_counts[
        word1
    ]

    if denominator == 0:

        return 0

    return numerator / denominator


def trigram_probability(
    word1,
    word2,
    word3
):

    numerator = trigram_counts[
        (word1, word2, word3)
    ]

    denominator = bigram_counts[
        (word1, word2)
    ]

    if denominator == 0:

        return 0

    return numerator / denominator


# =========================================================
# ADD-ONE SMOOTHING
# =========================================================

def smoothed_unigram_probability(
    word
):

    vocabulary_size = len(
        unigram_counts
    )

    total = sum(
        unigram_counts.values()
    )

    return (
        unigram_counts[word] + 1
    ) / (
        total + vocabulary_size
    )


def smoothed_bigram_probability(
    word1,
    word2
):

    vocabulary_size = len(
        unigram_counts
    )

    numerator = (
        bigram_counts[
            (word1, word2)
        ] + 1
    )

    denominator = (
        unigram_counts[word1]
        + vocabulary_size
    )

    return numerator / denominator


def smoothed_trigram_probability(
    word1,
    word2,
    word3
):

    vocabulary_size = len(
        unigram_counts
    )

    numerator = (
        trigram_counts[
            (word1, word2, word3)
        ] + 1
    )

    denominator = (
        bigram_counts[
            (word1, word2)
        ]
        + vocabulary_size
    )

    return numerator / denominator


# =========================================================
# CALCULATE ENTROPY
# =========================================================

def calculate_entropy(
    n,
    use_smoothing=False
):

    total_log_probability = 0
    word_count = 0

    zero_probability_count = 0

    for sentence in test_sentences:

        for i in range(
            len(sentence)
        ):

            word = sentence[i]

            if word in [
                '<s>',
                '</s>'
            ]:

                continue

            # -----------------------------------------
            # UNIGRAM
            # -----------------------------------------

            if n == 1:

                if use_smoothing:

                    probability = (
                        smoothed_unigram_probability(
                            word
                        )
                    )

                else:

                    probability = (
                        unigram_probability(
                            word
                        )
                    )

            # -----------------------------------------
            # BIGRAM
            # -----------------------------------------

            elif n == 2:

                if i == 0:

                    if use_smoothing:

                        probability = (
                            smoothed_unigram_probability(
                                word
                            )
                        )

                    else:

                        probability = (
                            unigram_probability(
                                word
                            )
                        )

                else:

                    previous_word = sentence[i - 1]

                    if use_smoothing:

                        probability = (
                            smoothed_bigram_probability(
                                previous_word,
                                word
                            )
                        )

                    else:

                        probability = (
                            bigram_probability(
                                previous_word,
                                word
                            )
                        )

            # -----------------------------------------
            # TRIGRAM
            # -----------------------------------------

            else:

                if i < 2:

                    if i == 0:

                        if use_smoothing:

                            probability = (
                                smoothed_unigram_probability(
                                    word
                                )
                            )

                        else:

                            probability = (
                                unigram_probability(
                                    word
                                )
                            )

                    else:

                        previous_word = sentence[i - 1]

                        if use_smoothing:

                            probability = (
                                smoothed_bigram_probability(
                                    previous_word,
                                    word
                                )
                            )

                        else:

                            probability = (
                                bigram_probability(
                                    previous_word,
                                    word
                                )
                            )

                else:

                    word1 = sentence[i - 2]
                    word2 = sentence[i - 1]

                    if use_smoothing:

                        probability = (
                            smoothed_trigram_probability(
                                word1,
                                word2,
                                word
                            )
                        )

                    else:

                        probability = (
                            trigram_probability(
                                word1,
                                word2,
                                word
                            )
                        )

            # -----------------------------------------
            # ZERO PROBABILITY
            # -----------------------------------------

            if probability == 0:

                zero_probability_count += 1

                continue

            total_log_probability += (
                math.log2(probability)
            )

            word_count += 1

    if word_count == 0:

        return float('inf'), zero_probability_count

    entropy = (
        -total_log_probability
        / word_count
    )

    return entropy, zero_probability_count


# =========================================================
# PREDICT NEXT WORD
# =========================================================

def predict_next_word(
    sentence,
    n,
    smoothing=False
):

    words = re.findall(
        r'[a-z]+',
        sentence.lower()
    )

    vocabulary = [
        word
        for word in unigram_counts
        if word not in [
            '<s>',
            '</s>'
        ]
    ]

    predictions = []

    if len(words) == 0:

        return []

    for candidate in vocabulary:

        # -----------------------------------------
        # UNIGRAM
        # -----------------------------------------

        if n == 1:

            if smoothing:

                probability = (
                    smoothed_unigram_probability(
                        candidate
                    )
                )

            else:

                probability = (
                    unigram_probability(
                        candidate
                    )
                )

        # -----------------------------------------
        # BIGRAM
        # -----------------------------------------

        elif n == 2:

            previous_word = words[-1]

            if smoothing:

                probability = (
                    smoothed_bigram_probability(
                        previous_word,
                        candidate
                    )
                )

            else:

                probability = (
                    bigram_probability(
                        previous_word,
                        candidate
                    )
                )

        # -----------------------------------------
        # TRIGRAM
        # -----------------------------------------

        else:

            if len(words) < 2:

                continue

            word1 = words[-2]
            word2 = words[-1]

            if smoothing:

                probability = (
                    smoothed_trigram_probability(
                        word1,
                        word2,
                        candidate
                    )
                )

            else:

                probability = (
                    trigram_probability(
                        word1,
                        word2,
                        candidate
                    )
                )

        predictions.append(
            (
                candidate,
                probability
            )
        )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# =========================================================
# DISPLAY ENTROPY
# =========================================================

def display_entropy():

    print("\n")
    print("=" * 70)
    print("ENTROPY OF UNSMOOTHED N-GRAM MODELS")
    print("=" * 70)

    for n in [1, 2, 3]:

        entropy, zeros = (
            calculate_entropy(
                n,
                False
            )
        )

        print(
            f"\nN = {n}"
        )

        if entropy == float('inf'):

            print(
                "Entropy = Infinity"
            )

        else:

            print(
                f"Entropy = {entropy:.4f} bits/word"
            )

        print(
            "Zero probability events =",
            zeros
        )


# =========================================================
# COMPARE SMOOTHING
# =========================================================

def compare_smoothing():

    print("\n")
    print("=" * 70)
    print("EFFECT OF SMOOTHING ON ENTROPY")
    print("=" * 70)

    print(
        "\n"
        "N        Unsmoothed Entropy        "
        "Smoothed Entropy"
    )

    print("-" * 70)

    for n in [1, 2, 3]:

        unsmoothed, zero1 = (
            calculate_entropy(
                n,
                False
            )
        )

        smoothed, zero2 = (
            calculate_entropy(
                n,
                True
            )
        )

        if unsmoothed == float('inf'):

            unsmoothed_text = "Infinity"

        else:

            unsmoothed_text = (
                f"{unsmoothed:.4f}"
            )

        print(
            f"{n:<8}"
            f"{unsmoothed_text:<25}"
            f"{smoothed:.4f}"
        )


# =========================================================
# FIND HIGH AND LOW ENTROPY SENTENCES
# =========================================================

def sentence_entropy(
    sentence,
    n
):

    probabilities = []

    for i in range(
        len(sentence)
    ):

        word = sentence[i]

        if word in [
            '<s>',
            '</s>'
        ]:

            continue

        if n == 1:

            probability = (
                unigram_probability(
                    word
                )
            )

        elif n == 2:

            if i == 0:

                probability = (
                    unigram_probability(
                        word
                    )
                )

            else:

                probability = (
                    bigram_probability(
                        sentence[i - 1],
                        word
                    )
                )

        else:

            if i < 2:

                probability = (
                    unigram_probability(
                        word
                    )
                )

            else:

                probability = (
                    trigram_probability(
                        sentence[i - 2],
                        sentence[i - 1],
                        word
                    )
                )

        if probability > 0:

            probabilities.append(
                probability
            )

        else:

            return float('inf')

    if not probabilities:

        return float('inf')

    entropy = 0

    for probability in probabilities:

        entropy += (
            -math.log2(probability)
        )

    return (
        entropy / len(probabilities)
    )


def high_low_entropy():

    print("\n")
    print("=" * 70)
    print("HIGH AND LOW ENTROPY SEQUENCES")
    print("=" * 70)

    results = []

    for sentence in test_sentences:

        entropy = sentence_entropy(
            sentence,
            3
        )

        text = " ".join(
            word
            for word in sentence
            if word not in [
                '<s>',
                '</s>'
            ]
        )

        results.append(
            (
                text,
                entropy
            )
        )

    results.sort(
        key=lambda x: x[1]
    )

    print("\nLOW ENTROPY SEQUENCE")
    print("-" * 70)

    low_sentence, low_entropy = (
        results[0]
    )

    print(
        "Sentence:",
        low_sentence
    )

    print(
        "Entropy:",
        low_entropy
    )

    print(
        "\nHIGH ENTROPY SEQUENCE"
    )

    print("-" * 70)

    high_sentence, high_entropy = (
        results[-1]
    )

    print(
        "Sentence:",
        high_sentence
    )

    print(
        "Entropy:",
        high_entropy
    )


# =========================================================
# NEXT WORD PREDICTION
# =========================================================

def prediction_menu():

    print("\n")
    print("=" * 70)
    print("TEXT PREDICTION")
    print("=" * 70)

    n = int(
        input(
            "Enter N (1, 2 or 3): "
        )
    )

    if n not in [1, 2, 3]:

        print("Invalid N.")

        return

    sentence = input(
        "Enter incomplete sentence: "
    )

    print("\nUNSMOOTHED PREDICTIONS")

    predictions = predict_next_word(
        sentence,
        n,
        False
    )

    if predictions:

        for i, (
            word,
            probability
        ) in enumerate(
            predictions,
            1
        ):

            print(
                f"{i}. {word:<20}"
                f"Probability = {probability:.4f}"
            )

    else:

        print(
            "No prediction available."
        )

    print("\nSMOOTHED PREDICTIONS")

    predictions = predict_next_word(
        sentence,
        n,
        True
    )

    for i, (
        word,
        probability
    ) in enumerate(
        predictions,
        1
    ):

        print(
            f"{i}. {word:<20}"
            f"Probability = {probability:.4f}"
        )


# =========================================================
# MAIN PROGRAM
# =========================================================

print("\n")
print("=" * 70)
print("N-GRAM ENTROPY EVALUATION SYSTEM")
print("=" * 70)

print(
    "\nTraining corpus loaded."
)

print(
    "Training sentences:",
    len(training_sentences)
)

print(
    "Test sentences:",
    len(test_sentences)
)

print(
    "Vocabulary size:",
    len(unigram_counts)
)


while True:

    print("\n")
    print("-" * 70)
    print("MAIN MENU")
    print("-" * 70)

    print("1. Calculate Entropy")
    print("2. Text Prediction")
    print("3. High and Low Entropy Sequences")
    print("4. Compare Smoothing Effect")
    print("5. Exit")

    choice = input(
        "\nEnter your choice: "
    )

    if choice == '1':

        display_entropy()

    elif choice == '2':

        prediction_menu()

    elif choice == '3':

        high_low_entropy()

    elif choice == '4':

        compare_smoothing()

    elif choice == '5':

        print(
            "\nProgram terminated successfully."
        )

        break

    else:

        print(
            "\nInvalid choice."
        )
