Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============ RESTART: C:/Users/ajayk/Downloads/nlp/CO3 AT1 que 2.py ============


======================================================================
SMOOTHING AND BACKOFF N-GRAM LANGUAGE MODEL
======================================================================

Training corpus loaded successfully.
Number of sentences: 30
Vocabulary size: 44


----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Unsmoothed Trigram Prediction
2. Backoff Prediction
3. Deleted Interpolation Prediction
4. Compare All Three Models
5. Demonstrate Zero Probability
6. Display Interpolation Weights
7. Exit

Enter your choice: 1

Enter an incomplete sentence: the student is


======================================================================
UNSMOOTHED TRIGRAM MODEL
======================================================================
1. intelligent       Probability = 0.1111
2. hardworking       Probability = 0.1111
3. reading           Probability = 0.1111
4. learning          Probability = 0.1111
5. studying          Probability = 0.1111


----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Unsmoothed Trigram Prediction
2. Backoff Prediction
3. Deleted Interpolation Prediction
4. Compare All Three Models
5. Demonstrate Zero Probability
6. Display Interpolation Weights
7. Exit

Enter your choice: 2

Enter an incomplete sentence: the student is


======================================================================
BACKOFF MODEL
======================================================================
1. the               Probability = 0.1613   Used = Unigram
2. is                Probability = 0.1382   Used = Unigram
3. intelligent       Probability = 0.1111   Used = Trigram
4. hardworking       Probability = 0.1111   Used = Trigram
5. reading           Probability = 0.1111   Used = Trigram


----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Unsmoothed Trigram Prediction
2. Backoff Prediction
3. Deleted Interpolation Prediction
4. Compare All Three Models
5. Demonstrate Zero Probability
6. Display Interpolation Weights
7. Exit

Enter your choice: 3

Enter an incomplete sentence: THE STUDENT IS


======================================================================
DELETED INTERPOLATION MODEL
======================================================================
1. learning          Probability = 0.0883
2. intelligent       Probability = 0.0774
3. hardworking       Probability = 0.0774
4. reading           Probability = 0.0774
5. studying          Probability = 0.0774


----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Unsmoothed Trigram Prediction
2. Backoff Prediction
3. Deleted Interpolation Prediction
4. Compare All Three Models
5. Demonstrate Zero Probability
6. Display Interpolation Weights
7. Exit

