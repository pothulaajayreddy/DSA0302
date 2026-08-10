Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

=============== RESTART: C:/Users/ajayk/Downloads/nlp/CO3 AT1.py ===============

======================================================================
UNSMOOTHED N-GRAM LANGUAGE MODEL
======================================================================

Training corpus loaded successfully.
Number of sentences: 30
Number of unique words: 44

----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Select N and Display Counts/Probabilities
2. Predict Top-5 Next Words
3. Demonstrate Zero Probability
4. Evaluate Prediction Performance
5. Display Limitations
6. Exit

Enter your choice: 4

======================================================================
PREDICTION PERFORMANCE EVALUATION
======================================================================
Enter N (1, 2 or 3): 2

Sentence: The student is
Expected: intelligent
Predicted: learning
Result: Incorrect

Sentence: The teacher is
Expected: intelligent
Predicted: learning
Result: Incorrect

Sentence: The computer is
Expected: fast
Predicted: learning
Result: Incorrect

Sentence: The programmer is
Expected: writing
Predicted: learning
Result: Incorrect

Sentence: The class is
Expected: interesting
Predicted: learning
Result: Incorrect

----------------------------------------------------------------------
Correct Predictions: 0
Total Test Sentences: 5
Prediction Accuracy: 0.00%

----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Select N and Display Counts/Probabilities
2. Predict Top-5 Next Words
3. Demonstrate Zero Probability
4. Evaluate Prediction Performance
5. Display Limitations
6. Exit

Enter your choice: 4

======================================================================
PREDICTION PERFORMANCE EVALUATION
======================================================================
Enter N (1, 2 or 3): 3

Sentence: The student is
Expected: intelligent
Predicted: intelligent
Result: Correct

Sentence: The teacher is
Expected: intelligent
Predicted: intelligent
Result: Correct

Sentence: The computer is
Expected: fast
Predicted: fast
Result: Correct

Sentence: The programmer is
Expected: writing
Predicted: learning
Result: Incorrect

Sentence: The class is
Expected: interesting
Predicted: learning
Result: Incorrect

----------------------------------------------------------------------
Correct Predictions: 3
Total Test Sentences: 5
Prediction Accuracy: 60.00%

----------------------------------------------------------------------
MAIN MENU
----------------------------------------------------------------------
1. Select N and Display Counts/Probabilities
2. Predict Top-5 Next Words
3. Demonstrate Zero Probability
4. Evaluate Prediction Performance
5. Display Limitations
6. Exit

