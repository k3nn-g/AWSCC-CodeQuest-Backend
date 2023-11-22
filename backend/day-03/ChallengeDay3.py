import random

#PLAYER INPUT (INTRODUCTION)
name = input("Enter your name: ")
print(f"Welcome to rock, paper, scissors, {name}!")

#GAME PROPER
action = input("Enter a choice (Rock, Paper, Scissors): ")

possible_actions = ["Rock", "Paper", "Scissors"]
computer = random.choice(possible_actions)

print(f"\nYou chose {action} while the computer chose {computer}.\n")

#DETERMINE THE WINNER
if action == computer:
    print(f"It's a tie!")
elif action == "Rock":
    if computer == "Scissors":
        print(f"The computer chose Scissors. Rock beats Scissors. You WIN!")
    else:
        print(f"The coputer chose Paper. Paper beats Rock. You LOSE!")
elif action == "Paper":
    if computer == "Rock":
        print(f"The computer chose Rock. Paper beats Rock. You WIN!")
    else:
        print(f"The computer chose Scissors. Scissors beats Paper. You LOSE!")
elif action == "Scissors":
    if computer == "Paper":
        print(f"The computer chose Paper. Scissors beats Paper. You WIN!")
    else:
        print(f"The computer chose Rock. Rock beats Scissors. You LOSE!")
