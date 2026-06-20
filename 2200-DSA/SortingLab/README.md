In labs for this unit, we aim for you to get practice with the process of analysing, solving, and explaining a computer science problem. Eventually, we expect you to be able to solve these problems unaided, but in these labs we provide guidance and milestones, with the intention being that you fill the specified gaps.

You are encouraged to discuss these problems with your classmates. You are also encouraged to use generative AI tools such as ChatGPT as a learning aid. However, anything you submit for assessment must remain your own original work, and you must understand the reasoning behind all answers and code you submit.

**Required Answer Structure**

Write your own answer in your own words. Justify your position using your understanding from lectures, labs, or your implemented code. 

# CITS2200 Lab 1: Speedrunning Leaderboard

To help you through the problem solving process we have broken it down into the following stages:
- Description
- Abstraction
- Investigation
- Design
- Implementation
- Analysis

You will only be assessed on some of these stages, but you are strongly encouraged to make sure you understand the whole process.
Having said this, problem solving is a highly flexible exercise with no universally perfect process, and this is meant only as a teaching aid, not as a strict framework.
So long as you are comfortable tackling all the aspects of the problem solving process, you are not expected to follow any particular framework.


## Description

You are tasked to design a class for keeping track of a speedrunning leaderboard, ranked by fastest run using [standard competition ranking](https://en.wikipedia.org/wiki/Ranking#Standard_competition_ranking_(%221224%22_ranking)).
Your class must implement certain functionalities.
Specifically we wish to be able to:
1. Get the current leaderboard (in rank order) at any time
2. Submit a new run with a given time and runner name to the leaderboard
3. Construct a new instance of the class given an initial list of runs
4. Find the run time required to achieve a given rank
5. Find what rank a particular time would achieve if submitted
6. Find how many runs are tied for a given time

You will be asked to implement this as the `Leaderboard` class found in `speedrunning.py`.
You are **not** allowed to use Python's built-in sorting functions or import any modules.



In competition ranking, items that compare equal receive the same ranking number, and then a gap is left in the ranking numbers. The number of ranking numbers that are left out in this gap is one less than the number of items that compared equal. Equivalently, each item's ranking number is 1 plus the number of items ranked above it. This ranking strategy is frequently adopted for competitions, as it means that if two (or more) competitors tie for a position in the ranking, the position of all those ranked below them is unaffected (i.e., a competitor only comes second if exactly one person scores better than them, third if exactly two people score better than them, fourth if exactly three people score better than them, etc.).

Thus if A ranks ahead of B and C (which compare equal) which are both ranked ahead of D, then A gets ranking number 1 ("first"), B gets ranking number 2 ("joint second"), C also gets ranking number 2 ("joint second") and D gets ranking number 4 ("fourth").

This method is called "Low" by IBM SPSS[4] and "min" by the R programming language[5] in their methods to handle ties.

## Abstraction

**Question 1 (1 mark):**
Write a short paragraph explaining the relationship between this problem and more abstract computer science topics we have covered in class.

Write your answer in the space provided in `answers.md`.


## Investigation

Hint: Above you should have been able to argue that this problem can be abstracted to sorting, updating, and searching ordered lists.

Now we can investigate the properties of this more abstract concept and algorithms and data structures for working with ordered lists.
Specifically, you should investigate and understand the logic behind insertion sort, merge sort, and binary search.
These have already been covered in Exercise 1, and if you have not yet completed this exercise, you are encouraged to do so now.


## Design

Armed with the understanding you developed in your investigation, you should now be able to come up with a design for how to solve this problem.

Reminder: You are **not** allowed to use Python's built-in sorting functions or import any modules.

**Question 2 (1 mark):**
What data do you need to store in the `Leaderboard` class?
What algorithm do you intend to use for each method?

Write your answer in the space provided in `answers.md`.


## Implementation

**Question 3 (5 marks):**
Implement your design by filling out the method stubs in `speedrunning.py`.
Your implementation must pass the tests given in `test_speedrunning.py`, which can be invoked by running `python -m unittest`.

Reminder: You are **not** allowed to use Python's built-in sorting functions or import any modules.

You are welcome to add methods to the class, so long as they do not compromise the provided tests.

For the implementation task (Question 3), you are permitted to use ChatGPT to generate a reference implementation for learning purposes.

You may:

- Generate code using ChatGPT

- Use ChatGPT to debug or explain your program

However, your submitted code must demonstrate your own understanding. Your implementation in speedrunning.py must include your own explanatory comments. 

You must understand the purpose and logic of:

- Each method

- Each loop and conditional

- Any non-trivial line of code

Comments must be written in your own words and should explain why the code works, not just what it does.



## Analysis

You should at this point be confident in your implementation, and should be able to explain the logic behind how it works to others.

The following questions ask you to provide arguments explaining your design.
Only brief, informal arguments are required of about a paragraph each.
You should not simply cite the known complexity for the algorithm you have chosen, nor should you simply narrate the code step by step, as this only explains *what* the algorithm does, not *why* it is correct.
Your arguments should be sufficient to convince a fellow student who has not seen this algorithm before that your design is correct and has the complexity you claim.

As a very simple example, here is an acceptable argument for the correctness and complexity of using binary search to find the largest natural number `x` such that `x^2 < y` for some given natural number `y`:
> Since the square of any natural number cannot be smaller than that number, we know that `y` can not be smaller than `x`.
> Therefore any answer must exist in the range between `0` and `y`.
> Using binary search, we can refine this range by taking the midpoint `m` of the range, comparing `m^2` to `y`.
> If `m^2 < y`, then we know that `m` satisfies `x^2 < y`, and so `x` must be at least `m`.
> Otherwise `m` must not satisfy the constraint, and so `x` must be less than `m`.
> Either way, this allows us to halve the search range.
> Repeating this process will eventually leave us with a range containing a single integer, which must therefore be the answer.
> Each step halves the size of the range, which started at `y`, meaning that it will take at most `log2(y)` steps to cut the range down to a single integer.
> Since each step can be done in constant time, this gives a time complexity of `O(lg y)`.

**Question 4 (1 mark):**
Give an argument for the correctness and complexity of your `__init__()` function.

**Question 5 (1 mark):**
Give an argument for the correctness and complexity of your `submit_run()` function.

**Question 6 (1 mark):**
Give an argument for the correctness and complexity of your `count_time()` function.

Write your answers in the spaces provided in `answers.md`.


## Extension (Not marking)

Consider the following questions:
1. Give arguments for the correctness and complexity of every method.
2. Is there a tradeoff between the complexities of different methods? That is, does making one method faster necessitate making another slower?
3. How could you make `get_runs()` tie-break by submission order instead of by name?



# Assessment

This lab is marked out of 10 marks and is worth 10% of your unit mark.

## Submitting

Submit only `speedrunning.py` and `answers.md` to cssubmit.
Ensure your name and student number are in the spaces provided at the top of both files.

## Marking Rubric

Each assessable component of this lab relates to some of the learning outcomes for this unit.
For reference, the learning outcomes for this unit are that students should be able to:
1. Undertake problem identification via abstraction
2. Describe common and important data structures and algorithms in the computing discipline
3. Implement a range of data structures and information literacy algorithms in a high-level programming language
4. Apply existing data structures and algorithms from pre-built software libraries
5. Design data structures and algorithms
6. Critically assess the performance of different data structures and algorithms

| Question | Basic                                              | Proficient                 | Total | Outcomes |
| -------- | -------------------------------------------------- | -------------------------- | ----- | -------- |
| 1        | (+1) Relates problem description to abstract topic |                            | /1    | 1        |
| 2        | (+1) Proposes a valid design                       |                            | /1    | 2, 5, 6  |
| 3        | (+1) Passes at least 50% of provided unit tests    | (+4) Passes all unit tests | /5    | 2, 3     |
| 4        | (+1) Provides convincing argument                  |                            | /1    | 2, 6     |
| 5        | (+1) Provides convincing argument                  |                            | /1    | 2, 6     |
| 6        | (+1) Provides convincing argument                  |                            | /1    | 2, 6     |
