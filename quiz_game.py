print("Welcome to my computer quiz!")

# asks if the user wants to play or not
playing = input("Do you want to play? ")

score = 0
total_questions = 4

# conditional check
if (playing.lower() != "yes"): 
    print("quitting program... see you later!")
    quit()

print("Okay! Great! Let's play :) ")

# Q1 
answer = input("What does CPU stand for? ")
if (answer.lower() == "central processing unit"): 
    print("Correct!")
    score += 1

else:
    print("Incorrect... " ) 

# Q2
answer = input("What does GPU stand for? ")
if (answer.lower() == "graphics processing unit"): 
    print("Correct!")
    score += 1

else:
    print("Incorrect... " ) 

# Q3
answer = input("What does RAM stand for? ")
if (answer.lower() == "random access memory"): 
    print("Correct!")
    score += 1

else:
    print("Incorrect... " ) 

# Q4
answer = input("What does CPU stand for? ")
if (answer.lower() == "central power unit"): 
    print("Correct!")
    score += 1

else:
    print("Incorrect... " ) 

# Implement a Score 
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / total_questions) * 100) + "%")