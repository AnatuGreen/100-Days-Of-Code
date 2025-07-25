import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#My solution before watching Angela

all_signs = [rock, paper, scissors]
user_sign = int(input("Enter 0 for Rock 1 for Paper, 2 for Scissors "))
computer_sign = random.randint(0,2)

#Ties
if user_sign == computer_sign:
    print(f"You played\n:"
          f"{all_signs[user_sign]}")
    print(f"Computer played\n:"
          f"{all_signs[computer_sign]}")
    print("That is a tie! Play again!")
#User winnings
elif user_sign == 0 and computer_sign == 2:
    print(f"You played\n:"
          f"{all_signs[user_sign]}")
    print(f"Computer played\n:"
          f"{all_signs[computer_sign]}")
    print("You Won!!!")
elif user_sign == 2 and computer_sign == 1:
    print(f"You played\n:"
          f"{all_signs[user_sign]}")
    print(f"Computer played\n:"
          f"{all_signs[computer_sign]}")
    print("You Won!!!")
elif user_sign == 1 and computer_sign == 0:
    print(f"You played\n:"
          f"{all_signs[user_sign]}")
    print(f"Computer played\n:"
          f"{all_signs[computer_sign]}")
    print("You Won!!!")
#Comp winnings
elif user_sign == 0 and computer_sign ==1:
    print(f"You played\n:"
          f"{all_signs[user_sign]}")
    print(f"Computer played\n:"
          f"{all_signs[computer_sign]}")
    print("Computer Won!!!")
elif user_sign == 1 and computer_sign == 2:
    print(f"You played\n:"
          f"{all_signs[user_sign]}")
    print(f"Computer played\n:"
          f"{all_signs[computer_sign]}")
    print("Computer Won!!!")
elif user_sign == 2 and computer_sign == 0:
    print(f"You played\n:"
          f"{all_signs[user_sign]}")
    print(f"Computer played\n:"
          f"{all_signs[computer_sign]}")
    print("Computer Won!!!")
else:
    print("Check that you entered accepted value and play again")
