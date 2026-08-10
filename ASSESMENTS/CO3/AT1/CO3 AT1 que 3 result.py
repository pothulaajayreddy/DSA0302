Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============ RESTART: C:/Users/ajayk/Downloads/nlp/CO3 AT1 que 3.py ============


======================================================================
N-GRAM ENTROPY EVALUATION SYSTEM
======================================================================

Training corpus loaded.
Training sentences: 27
Test sentences: 5
Vocabulary size: 40


----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Calculate Entropy
2. Text Prediction
3. High and Low Entropy Sequences
4. Compare Smoothing Effect
5. Exit

Enter your choice: 1


======================================================================
ENTROPY OF UNSMOOTHED N-GRAM MODELS
======================================================================

N = 1
Entropy = 4.6891 bits/word
Zero probability events = 0

N = 2
Entropy = 1.3246 bits/word
Zero probability events = 0

N = 3
Entropy = 0.9517 bits/word
Zero probability events = 0


----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Calculate Entropy
2. Text Prediction
3. High and Low Entropy Sequences
4. Compare Smoothing Effect
5. Exit

Enter your choice: 2


======================================================================
TEXT PREDICTION
======================================================================
Enter N (1, 2 or 3): 2
Enter incomplete sentence: the student is

UNSMOOTHED PREDICTIONS
1. learning            Probability = 0.1111
2. intelligent         Probability = 0.0741
3. hardworking         Probability = 0.0741
4. reading             Probability = 0.0741
5. studying            Probability = 0.0741

SMOOTHED PREDICTIONS
1. learning            Probability = 0.0597
2. intelligent         Probability = 0.0448
3. hardworking         Probability = 0.0448
4. reading             Probability = 0.0448
5. studying            Probability = 0.0448


----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Calculate Entropy
2. Text Prediction
3. High and Low Entropy Sequences
4. Compare Smoothing Effect
5. Exit

Enter your choice: 3


======================================================================
HIGH AND LOW ENTROPY SEQUENCES
======================================================================

LOW ENTROPY SEQUENCE
----------------------------------------------------------------------
Sentence: the teacher is reading a book
Entropy: 1.2334340056606201

HIGH ENTROPY SEQUENCE
----------------------------------------------------------------------
Sentence: the student is intelligent
Entropy: 1.8983122779765291


----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Calculate Entropy
2. Text Prediction
3. High and Low Entropy Sequences
4. Compare Smoothing Effect
5. Exit

Enter your choice: 4


======================================================================
EFFECT OF SMOOTHING ON ENTROPY
======================================================================

N        Unsmoothed Entropy        Smoothed Entropy
----------------------------------------------------------------------
1       4.6891                   4.6644
2       1.3246                   3.1656
3       0.9517                   3.1689


----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Calculate Entropy
2. Text Prediction
3. High and Low Entropy Sequences
4. Compare Smoothing Effect
5. Exit

