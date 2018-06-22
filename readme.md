# Data Science Research & Development Assessment

Thank you for your interest in working at xxx! This assessment will help us understand aspects of your skills as a data scientist which are more difficult to understand in a standard in-person interview. We expect that you should be able to complete the assessment in around 4 hours.

## Instructions

* Use Python for all coding problems.
* Written answers should be provided in a new text document; code should be in files named <yourfirstname><yourlastname>_question<question number>.<py/ipynb>. Example: "janesmith_qustion2.py".
* Please work independently. Web searches are fine, but don’t share work with other people.

## Question 1: Modeling

Recommended time: 3 hours

The xxx Data Science team spends some time working on client engagements, and we also spend time with data after the engagements to develop modeling algorithms and automated workflows for future engagements. In this question, you will test different data processing and modeling techniques to see what approaches are the most effective in making predictions.

In the past, xxx has worked with educational groups and schools to help them leverage their data for decisions in policies and new programs. One example of this is student retention. Universities will often want to help keep students in school and make sure that they can graduate. Universities have limited resources to devote to retention, so they need to make sure that those resources are directed at the students who can benefit the most. Data on student demographics, performance, and history can be used to predict which students are in danger of dropping out so that the university can intervene in problem situations.

In the _data_ folder, find a CSV, `graduates.csv`, of [synthetic] data on students and graduation status. Each row represents one student, and each column is a piece of information about that student. One column, "graduated", represents whether or not this student successfully completed their degree program. Consider how to predict this column for future students who have recorded values for all (or most) of the other columns. Try at least two different modeling approaches and compare them to each other. This may be as simple as different hyperparameters, or as involved as completely different modeling algorithms and preprocessing steps. Which is the best, and why?

Your response should be a combination of code and a written document -- treat this as a quick exploration of different modeling approaches which you'll then share with your colleagues. If you work in a notebook-style environment such as Jupyter, include the explanatory text in the notebook. Otherwise, write explanatory text in the document, and code in a separate .py file. You may use any available open-source software package(s) you find helpful.

Structure your document in three sections:
A. Pre-Processing: What (if anything) have you done to prepare or clean the data before using it to train your model?
B. Model Building: Use the data to predict the probability that a student will successfully graduate. Also please elaborate why you choose a certain model and what are the pros and cons of the chosen model. 
C. Validation: How well is each model performing? Which is better?

Don't worry about micro-optimizations of your model at this point. We're interested in large-scale differences (if any) produced by different modeling choices.

## Question 2: Coding

Recommended time: 1 hour

Nothing works right the first time. At xxx, software writing and model building is a collaborative effort. Before anything goes into production, it will be reviewed by at least one other team member. In this problem, we've provided a piece of code which almost, but not quite, works. Read through the provided code and figure out what it's supposed to do. Fix or rewrite it so that the tests pass. Your fixed version of the broken function should be something that you'd be willing to put into the company code base for long-term use.

The failing code is in a file `failing_code.py` in the folder _code_ . Modify the code so that it works (feel free to completely rewrite the function if you like) and add documentation so that future data scientists can use and maintain it. Save your new function (with the original tests) as <yourfirstname><yourlastname>_question2.<py/ipynb> and return it with your other materials.

Make sure that your documentation explains the purpose of the function.
* Your modified function should take the same inputs as the original function: a 2D array and a list of integers.
* The modified function should output a 2D array.
* You may use any standard library modules, but no external packages which are not already imported / loaded.
* There are no bugs in the test functions; do not modify the tests.
