### Section 1: Function Definition and Welcome Message

```python
def quiz():
    print("Welcome to my computer quiz!")
```

**Explanation:**

- **function definition:** The `quiz()` function encapsulates all the quiz logic, making the code modular and easy to manage.
- **Welcome Message:** The `print()` function displays a welcome message to the user.

<br/>

### Section 2: User Input for Playing

```python
playing = input("Do you want to play? ").strip().lower()
if playing != "yes":
    print("Quitting program... see you later!")
    return
```

**Explanation:**

- **Input and Normalization**: The `input()` asks the user if they want to play. The `strip().lower()` method ensure that the input is case-insensitive and free of leading or trailing whitespace.
- **Conditional Check:** If the user does not type "yes" a message is printed, and the function returns, exiting the quiz.

<br/>

### Section 3: Starting the Quiz

```python
    print("Great! Let's start!")
```

**Explanation:**

- **Starting Message:** This line prints a message indicating that the quiz is about to start.

<br/>

### Section 4: Questions and Answers Dictionary

```python
    questions_answers = {
        "What does CPU stand for? " : "central processing unit",
        "What does GPU stand for? " : "graphics processing unit",
        "What does RAM stand for? " : "random access memory",
        "What does PSU stand for? " : "power supply unit"
    }
```

**Explanation:**

- **Dictionary setup**: A dictionary named `questions_answers` is created to store the quiz questions as keys and their correct answers as values. This structure allows for easy iteration and management.
  - **Key**: A string on the left is representing the question.
  - **Value:** A string on right representing the correct answer.

<br/>

### Section 5: Initializing Score and Looping Through Objects

```python
score = 0

for (question, correct_answer in questons_answers.items()):
    answer = input(question).strip().lower()
    if (answer == correct_answer):
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")
```

**Explanation:**

- **Score Initializaton**: The `score` variable is initialized to 0 to keep track of the user's correct answers.
- **Loop through questions**: A `for` loop itewrates through each "Question" : "answer" pair in the `questions_answers` dictionary.
  - **Input and Normalization**: The `input()` function asks the current question. The `.strip().lower()` method ensure the answer is case-insensitive and free of trailing whitespace.
  - **Answer Check:** An `if` statment compares the users answer to the correct answer. If they match, a "correct!" message is printed and the `score` is incremented. Otherwise, incorrect.. will be printed.

> More in Depth Walkthrough

```python
for question, correct_answer in questions_answers.items():
```

- `questions_answers.items()` : The `items()` method is a dictionary that returns a view object that displays a list of key-value pairs. So:
  ```python
  [
      # Key                           # Value
      ("What does CPU stand for? ", "central processing unit"),
      ("What does GPU stand for? ", "graphics processing unit"),
      ("What does RAM stand for? ", "random access memory"),
      ("What does PSU stand for? ", "power supply unit")
  ]
  ```
- `question, correct_answer in`... This syntax is a form of unpacking. Each iteration of the loop takes a tuple (a key-value pair) from the list produced by `items()`. The first element of the tuple is assigned to `question` and the second element to `correct_answer`.
  1. The `items()` method provides the tuple `("What does CPU stand for? ", "central processing unit")`
  2. `question` is assigned the value `"What does CPU stand for? "`
  3. `correct_answer` is assigned the value `"central processing unit"`.

<br/>

### Section 6: Displaying the Final Score

```python
    total_questions = len(questions_answers)
    print(f"You got {score} questions correct!")
    print(f"You got {(score / total_questions) * 100 }%")
```

**Explanation:**

- **Total Questions Calculation:** The `total_questions` variable is assigned the number of questions by using the `leng()` function on the `questions_answers` dictionary.
- **Final Score Message:** Two `print()` statements display the users total and percentage. The `f-strings` are used for easy and readable string formatting.

<br/>

### Section 7: Main Guard

```python
if (__name__ == "__main__"):
    quiz()
```

**Explanation:**

- **Main Guard:** This block ensures that the quiz() function runs only if the script is executed directly, not if it is imported as a module in another script. This is a common Python practice to control the execution flow of the code.
