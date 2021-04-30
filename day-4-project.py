# Rock Paper Scessors

import random

print("Lets play a game! \n Rock Paper Scissors")
user = input("What is you choice?\n")
choices = ["rock", "paper", "scissors"]
choices_len = len(choices) - 1
computer = choices[random.randint(0, choices_len)]
print(computer)
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

if user == "rock":
    if computer == "rock":
        print(
            f"\nYour {rock} \n Computer {rock}\n\nNo one win.\n »» Play again! ««")
    elif computer == "scissors":
        print(
            f"\nYour {rock} \n Computer {scissors}\n\nYou Win!\n »» Play again! ««")
    else:
        print(
            f"\nYour {rock} \n Computer {paper}\n\nComputer Wins!\n »» Play again! ««")
elif user == "paper":
    if computer == "paper":
        print(
            f"\nYour {paper} \n Computer {paper}\n\nNo one win.\n »» Play again! ««")
    elif computer == "rock":
        print(
            f"\nYour {paper} \n Computer {rock}\n\nYou Win!\n »» Play again! ««")
    else:
        print(
            f"\nYour {paper} \n Computer {scissors}\n\nComputer Wins!\n »» Play again! ««")
else:
    if computer == "scissors":
        print(
            f"\nYour {scissors} \n Computer {scissors}\n\nNo one win.\n »» Play again! ««")
    elif computer == "scissors":
        print(
            f"\nYour {scissors} \n Computer {paper}\n\nYou Win!\n »» Play again! ««")
    else:
        print(
            f"\nYour {scissors} \n Computer {rock}\n\nComputer Wins!\n »» Play again! ««")
