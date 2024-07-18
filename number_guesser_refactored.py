import random

def get_top_of_range(): 
    while True: 
        top_of_range = input("Enter the limit for the guessing range (a positive number): ")
        if top_of_range.isdigit(): 
            top_of_range = int(top_of_range)
            if top_of_range > 0: 
                return top_of_range
            else: 
                print("The number must be greater than 0. Please try again.")
        else: 
            print("Invalid input. Please enter a postive number.")


def get_user_guess(): 
    while True: 
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            return int(user_guess)
        else: 
            print("Invalid input. Please enter a number.")


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    top_of_range = get_top_of_range()
    
    random_number = random.randint(1, top_of_range)
    guesses = 0 

    while True: 
        guesses += 1
        user_guess = get_user_guess()

        if user_guess == random_number: 
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess > random_number: 
            print("Too high! Try again.")
        else: 
            print("Too low! Try again.")

    print(f"You guessed the number in {guesses} attempts.")

if __name__ == "__main__":
    number_guessing_game()