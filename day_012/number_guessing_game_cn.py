from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, and returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    # Generate a random number between 1 & 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. Game over.")
            return
        elif guess != answer:
            print("Guess again")

# Track the number of turns and reduce by 1 if they get it wrong
game()

# Repeat the guessing functionality if they get wrong.




















# def compare():
#     number_to_guess = random.randint(1, 100)
#     print(number_to_guess)
#     guess = int(input("Make a guess: "))
#     game_over = True
#
#     while not game_over:
#         if guess == number_to_guess:
#             print(art.right_answer)
#         elif guess > number_to_guess:
#             print("Too high. Guess again")
#         else:
#             print("Too low. Guess again")
#
# compare()
