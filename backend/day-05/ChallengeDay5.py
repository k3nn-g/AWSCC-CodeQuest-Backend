import random

name = input("Enter your name: ").capitalize()
print(f"Hi, {name}!")

player = input("Enter a move (rock, paper, scissors): ").lower()

choice = ["rock", "paper", "scissors"]

computer = random.choice(choice)
print(f"Computer: {computer}")

if player == computer:
    print(f"It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print(f"The computer chose Scissors. Rock beats Scissors. You WIN!")
    else:
        print(f"The computer chose Paper. Paper beats Rock. You LOSE!")
elif player == "paper":
    if computer == "rock":
        print(f"The computer chose Rock. Paper beats Rock. You WIN!")
    else:
        print(f"The computer chose Scissors. Scissors beats Paper. You LOSE!")
elif player == "scissors":
    if computer == "paper":
        print(f"The computer chose Paper. Scissors beats Paper. You WIN!")
    else:
        print(f"The computer chose Rock. Rock beats Scissors. You LOSE!")