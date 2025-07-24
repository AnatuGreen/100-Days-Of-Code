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

game_ascii = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice <= 2 and player_choice >= 0:
    print(f"You chose:\n{game_ascii[player_choice]}\n")

computer_choice = random.randint(0, 2)

if player_choice < 0 or player_choice > 2:
    print("Invalid submission. You lose!")
elif player_choice == 0 and computer_choice == 2:
    print(f"Computer chose {computer_choice}:\n{game_ascii[computer_choice]}\nYou win!")
elif player_choice == 2 and computer_choice == 0:
    print(f"Computer chose {computer_choice}:\n{game_ascii[computer_choice]}\nYou lose!")
elif player_choice > computer_choice:
    print(f"Computer chose {computer_choice}:\n{game_ascii[computer_choice]}\nYou win!")
elif player_choice < computer_choice:
    print(f"Computer chose {computer_choice}:\n{game_ascii[computer_choice]}\nYou lose!")
elif player_choice == computer_choice:
    print(f"Computer chose {computer_choice}:\n{game_ascii[computer_choice]}\nIts a draw")

else:
    print("Invalid submission. You lose!")