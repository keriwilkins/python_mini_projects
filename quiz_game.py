# Python Question Quiz 
def quiz(): 
    print("Welcome to my computer quiz!")

    playing = input("Do you want to play? ").strip().lower()

    if (playing != "yes"):
        print("Quitting program...")
        return
    print("Great! Let's play! ")

    questions_answers = {
        "What does CPU stand for? " : "central processing unit",
        "What does GPU stand for? " : "graphics processing unit",
        "What does RAM stand for? " : "random access memory",
        "What does PSU stand for? " : "power supply unit"
    }

    score = 0

    for question, correct_answer in questions_answers.items():
        answer = input(question).strip().lower()
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect...")

    total_questions = len(questions_answers)
    print(f"You got {score} questions correct!")
    print(f"You got {(score / total_questions) * 100}%")

if (__name__ == "__main__"): 
    quiz()