import re
from collections import Counter


# =========================================================
# TRAINING CORPUS
# =========================================================

corpus = """
The student is intelligent.
The student is hardworking.
The student is reading a book.
The student is learning programming.
The student is studying computer science.
The student is writing a program.
The student is solving problems.
The student is attending the class.
The student is using a computer.

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
The class is starting today.
The class is learning programming.
The class is studying computer science.
"""


# =========================================================
# PREPROCESSING AND TOKENIZATION
# =========================================================

def preprocess(text):

    text = text.lower()

    raw_sentences = re.split(r'[.!?]+', text)

    sentences = []

    for sentence in raw_sentences:

        words = re.findall(r'[a-z]+', sentence)

        if words:

            words = ['<s>'] + words + ['</s>']

            sentences.append(words)

    return sentences


sentences = preprocess(corpus)


# =========================================================
# CREATE N-GRAM COUNTS
# =========================================================

unigram_counts = Counter()
bigram_counts = Counter()
trigram_counts = Counter()


for sentence in sentences:

    # Unigrams
    for word in sentence:

        unigram_counts[word] += 1

    # Bigrams
    for i in range(len(sentence) - 1):

        bigram = (
            sentence[i],
            sentence[i + 1]
        )

        bigram_counts[bigram] += 1

    # Trigrams
    for i in range(len(sentence) - 2):

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

    total = sum(unigram_counts.values())

    if total == 0:

        return 0

    return unigram_counts[word] / total


def bigram_probability(word1, word2):

    count_bigram = bigram_counts[
        (word1, word2)
    ]

    count_word1 = unigram_counts[word1]

    if count_word1 == 0:

        return 0

    return count_bigram / count_word1


def trigram_probability(word1, word2, word3):

    count_trigram = trigram_counts[
        (word1, word2, word3)
    ]

    count_bigram = bigram_counts[
        (word1, word2)
    ]

    if count_bigram == 0:

        return 0

    return count_trigram / count_bigram


# =========================================================
# UNSMOOTHED TRIGRAM PREDICTION
# =========================================================

def unsmoothed_prediction(sentence):

    words = re.findall(
        r'[a-z]+',
        sentence.lower()
    )

    if len(words) < 2:

        return []

    word1 = words[-2]
    word2 = words[-1]

    predictions = []

    vocabulary = [
        word
        for word in unigram_counts
        if word not in ['<s>', '</s>']
    ]

    for word in vocabulary:

        probability = trigram_probability(
            word1,
            word2,
            word
        )

        if probability > 0:

            predictions.append(
                (word, probability)
            )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# =========================================================
# BACKOFF MODEL
# =========================================================

def backoff_probability(
    word1,
    word2,
    word3
):

    # First try trigram
    trigram_prob = trigram_probability(
        word1,
        word2,
        word3
    )

    if trigram_prob > 0:

        return trigram_prob, "Trigram"

    # If trigram is unavailable,
    # use bigram
    bigram_prob = bigram_probability(
        word2,
        word3
    )

    if bigram_prob > 0:

        return bigram_prob, "Bigram"

    # If bigram is unavailable,
    # use unigram
    unigram_prob = unigram_probability(
        word3
    )

    return unigram_prob, "Unigram"


def backoff_prediction(sentence):

    words = re.findall(
        r'[a-z]+',
        sentence.lower()
    )

    if len(words) < 2:

        return []

    word1 = words[-2]
    word2 = words[-1]

    predictions = []

    vocabulary = [
        word
        for word in unigram_counts
        if word not in ['<s>', '</s>']
    ]

    for word in vocabulary:

        probability, level = backoff_probability(
            word1,
            word2,
            word
        )

        predictions.append(
            (word, probability, level)
        )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# =========================================================
# DELETED INTERPOLATION
# =========================================================

# Interpolation weights
LAMBDA_UNIGRAM = 0.2
LAMBDA_BIGRAM = 0.3
LAMBDA_TRIGRAM = 0.5


def interpolation_probability(
    word1,
    word2,
    word3
):

    p1 = unigram_probability(word3)

    p2 = bigram_probability(
        word2,
        word3
    )

    p3 = trigram_probability(
        word1,
        word2,
        word3
    )

    probability = (
        LAMBDA_UNIGRAM * p1
        +
        LAMBDA_BIGRAM * p2
        +
        LAMBDA_TRIGRAM * p3
    )

    return probability


def interpolation_prediction(sentence):

    words = re.findall(
        r'[a-z]+',
        sentence.lower()
    )

    if len(words) < 2:

        return []

    word1 = words[-2]
    word2 = words[-1]

    predictions = []

    vocabulary = [
        word
        for word in unigram_counts
        if word not in ['<s>', '</s>']
    ]

    for word in vocabulary:

        probability = interpolation_probability(
            word1,
            word2,
            word
        )

        predictions.append(
            (word, probability)
        )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# =========================================================
# DISPLAY PREDICTIONS
# =========================================================

def display_predictions(
    title,
    predictions,
    model
):

    print("\n")
    print("=" * 70)
    print(title)
    print("=" * 70)

    if not predictions:

        print(
            "No prediction available."
        )

        return

    for i, item in enumerate(
        predictions,
        1
    ):

        if model == "backoff":

            word, probability, level = item

            print(
                f"{i}. {word:<18}"
                f"Probability = {probability:.4f}"
                f"   Used = {level}"
            )

        else:

            word, probability = item

            print(
                f"{i}. {word:<18}"
                f"Probability = {probability:.4f}"
            )


# =========================================================
# ZERO PROBABILITY DEMONSTRATION
# =========================================================

def demonstrate_zero_probability():

    print("\n")
    print("=" * 70)
    print("ZERO PROBABILITY DEMONSTRATION")
    print("=" * 70)

    word1 = input(
        "Enter first context word: "
    ).lower()

    word2 = input(
        "Enter second context word: "
    ).lower()

    word3 = input(
        "Enter candidate next word: "
    ).lower()

    probability = trigram_probability(
        word1,
        word2,
        word3
    )

    print("\nTrigram:")
    print(
        word1,
        word2,
        word3
    )

    print(
        "Trigram Count =",
        trigram_counts[
            (word1, word2, word3)
        ]
    )

    print(
        "Unsmoothed Trigram Probability =",
        probability
    )

    if probability == 0:

        print(
            "\nThe trigram is unseen."
        )

        print(
            "Therefore, the unsmoothed probability is 0."
        )

        backoff_prob, level = backoff_probability(
            word1,
            word2,
            word3
        )

        print(
            "\nBackoff Probability =",
            round(backoff_prob, 4)
        )

        print(
            "Backoff used:",
            level
        )


# =========================================================
# COMPARE ALL THREE MODELS
# =========================================================

def compare_models():

    print("\n")
    print("=" * 70)
    print("MODEL COMPARISON")
    print("=" * 70)

    sentence = input(
        "Enter an incomplete sentence: "
    )

    print("\nInput:", sentence)

    # Unsmoothed
    unsmoothed = unsmoothed_prediction(
        sentence
    )

    display_predictions(
        "UNSMOOTHED TRIGRAM MODEL",
        unsmoothed,
        "normal"
    )

    # Backoff
    backoff = backoff_prediction(
        sentence
    )

    display_predictions(
        "BACKOFF MODEL",
        backoff,
        "backoff"
    )

    # Deleted interpolation
    interpolation = interpolation_prediction(
        sentence
    )

    display_predictions(
        "DELETED INTERPOLATION MODEL",
        interpolation,
        "normal"
    )


# =========================================================
# DISPLAY FORMULA AND WEIGHTS
# =========================================================

def display_interpolation():

    print("\n")
    print("=" * 70)
    print("DELETED INTERPOLATION")
    print("=" * 70)

    print(
        "\nInterpolation formula:"
    )

    print(
        "P = λ1 * P(unigram)"
        " + λ2 * P(bigram)"
        " + λ3 * P(trigram)"
    )

    print("\nWeights:")

    print(
        "λ1 (Unigram) =",
        LAMBDA_UNIGRAM
    )

    print(
        "λ2 (Bigram)  =",
        LAMBDA_BIGRAM
    )

    print(
        "λ3 (Trigram) =",
        LAMBDA_TRIGRAM
    )

    print(
        "\nSum of weights =",
        LAMBDA_UNIGRAM
        + LAMBDA_BIGRAM
        + LAMBDA_TRIGRAM
    )


# =========================================================
# MAIN PROGRAM
# =========================================================

print("\n")
print("=" * 70)
print("SMOOTHING AND BACKOFF N-GRAM LANGUAGE MODEL")
print("=" * 70)

print(
    "\nTraining corpus loaded successfully."
)

print(
    "Number of sentences:",
    len(sentences)
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

    print("1. Unsmoothed Trigram Prediction")
    print("2. Backoff Prediction")
    print("3. Deleted Interpolation Prediction")
    print("4. Compare All Three Models")
    print("5. Demonstrate Zero Probability")
    print("6. Display Interpolation Weights")
    print("7. Exit")

    choice = input(
        "\nEnter your choice: "
    )

    # -----------------------------------------------------
    # UNSMOOTHED
    # -----------------------------------------------------

    if choice == '1':

        sentence = input(
            "\nEnter an incomplete sentence: "
        )

        predictions = unsmoothed_prediction(
            sentence
        )

        display_predictions(
            "UNSMOOTHED TRIGRAM MODEL",
            predictions,
            "normal"
        )

    # -----------------------------------------------------
    # BACKOFF
    # -----------------------------------------------------

    elif choice == '2':

        sentence = input(
            "\nEnter an incomplete sentence: "
        )

        predictions = backoff_prediction(
            sentence
        )

        display_predictions(
            "BACKOFF MODEL",
            predictions,
            "backoff"
        )

    # -----------------------------------------------------
    # DELETED INTERPOLATION
    # -----------------------------------------------------

    elif choice == '3':

        sentence = input(
            "\nEnter an incomplete sentence: "
        )

        predictions = interpolation_prediction(
            sentence
        )

        display_predictions(
            "DELETED INTERPOLATION MODEL",
            predictions,
            "normal"
        )

    # -----------------------------------------------------
    # COMPARE
    # -----------------------------------------------------

    elif choice == '4':

        compare_models()

    # -----------------------------------------------------
    # ZERO PROBABILITY
    # -----------------------------------------------------

    elif choice == '5':

        demonstrate_zero_probability()

    # -----------------------------------------------------
    # WEIGHTS
    # -----------------------------------------------------

    elif choice == '6':

        display_interpolation()

    # -----------------------------------------------------
    # EXIT
    # -----------------------------------------------------

    elif choice == '7':

        print(
            "\nProgram terminated successfully."
        )

        break

    else:

        print(
            "\nInvalid choice. Please enter 1 to 7."
        )
