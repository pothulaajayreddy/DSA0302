Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============= RESTART: C:/Users/ajayk/Downloads/nlp/co5 at1 que1.py ============
INPUT:
John and Mary went to the park. He brought a ball. She wanted to play with it. The dog chased him excitedly. Finally, they all went home.

COREFERENCE RESOLUTION:
He -> John
She -> Mary
it -> ball
him -> John
they -> John, Mary and dog

CONSTRAINTS USED:
1. Gender and number agreement
2. Recency
3. Semantic compatibility
4. Discourse coherence

FINAL COREFERENCE CHAINS:
John -> He -> him
Mary -> She
Ball -> it
John + Mary + Dog -> they

REWRITTEN PARAGRAPH:
John and Mary went to the park. John brought a ball.
Mary wanted to play with the ball.
The dog chased John excitedly.
Finally, John, Mary and the dog all went home.

========== RESTART: C:/Users/ajayk/OneDrive/Documents/co5 at1 que2.py ==========
USER INPUT:
I have an important exam tomorrow but I’m not able to concentrate.

DIALOG ACT:
Advise + Encourage

CONSTRAINTS:
1. Maintain exam and concentrate
2. Use Cause-Effect or Elaboration
3. Include focus, break or confident
4. Response length: 2 sentences
5. Positive and logical response

GENERATED RESPONSES:

Response 1 :
Since your exam is tomorrow, take a short break and then focus on one topic at a time. Stay confident because steady effort can help you prepare well.

Response 2 :
Your exam is important, so take a short break and remove distractions before studying. This can improve your focus and help you feel confident.

Response 3 :
If you cannot concentrate for your exam, take a short break and return with a clear focus. You can prepare well and feel confident with regular study.

EVALUATION:
Response 1 : Satisfies constraints
Response 2 : Satisfies constraints
Response 3 : Satisfies constraints

BEST RESPONSE:
Since your exam is tomorrow, take a short break and then focus on one topic at a time. Stay confident because steady effort can help you prepare well.

============= RESTART: C:/Users/ajayk/Downloads/nlp/co5 at1 que3.py ============
INPUT SENTENCE:
The bank by the river flooded after the storm, but it was saved by quick action.

AMBIGUOUS WORD:
bank

WORD SENSE SCORES:
Financial Bank = 0
Riverbank = 3

RESOLVED SENSE:
Riverbank

CONSTRAINTS USED:
1. Contextual constraint
2. Semantic compatibility
3. Discourse coherence

PREDICATE LOGIC:
riverbank(x) AND near(x, river)
flood(x) AND after(flood, storm)
saved(x, quick_action)

PARAPHRASE:
The riverbank near the river flooded after the storm, but quick action saved it.

DISCOURSE RELATION:
CONTRAST

============= RESTART: C:/Users/ajayk/Downloads/nlp/co5 at1 que4.py ============
INPUT SENTENCE:
The student saw the professor with the telescope.

POSSIBLE INTERPRETATIONS:

Interpretation 1:
The student used the telescope to see the professor.

Interpretation 2:
The professor had the telescope.

CONSTRAINT ANALYSIS:

Interpretation 1:
syntax : with the telescope modifies the action saw
semantic : student uses telescope
role : Instrument

Interpretation 2:
syntax : with the telescope modifies professor
semantic : professor possesses telescope
role : Possession

CONSTRAINTS USED:
1. Syntactic attachment
2. Semantic compatibility
3. Contextual interpretation
4. Semantic role labeling

SELECTED INTERPRETATION:
The student used the telescope to see the professor.

SEMANTIC ROLES:
Agent     : Student
Action    : Saw
Patient   : Professor
Instrument: Telescope

============= RESTART: C:/Users/ajayk/Downloads/nlp/co5 at1 que5.py ============
INPUT:
The student missed the assignment deadline because the submission portal was unavailable.

ENTITIES:
1. Student
2. Assignment
3. Deadline
4. Submission Portal

SEMANTIC RELATION:
Submission portal unavailable
        ↓
Student unable to submit assignment
        ↓
Assignment deadline missed

DISCOURSE RELATION:
CAUSE -> EFFECT

GENERATED RESPONSES:

Response 1 :
The student missed the assignment deadline because the submission portal was unavailable. The student should contact the instructor and explain the issue politely.

Response 2 :
Since the submission portal was unavailable, the student could not submit the assignment before the deadline. The student should inform the instructor about the problem.

Response 3 :
The submission portal was unavailable, so the student missed the assignment deadline. The student can explain the technical problem and request further assistance.

CONSTRAINT EVALUATION:
Response 1 : All entity constraints satisfied
Response 2 : All entity constraints satisfied
Response 3 : All entity constraints satisfied

BEST RESPONSE:
Since the submission portal was unavailable, the student could not submit the assignment before the deadline. The student should inform the instructor about the problem.
