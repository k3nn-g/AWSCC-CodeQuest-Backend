player1 = input("Player 1: ")
player2 = input("Player 2: ")

move = ["rock","paper","scissors"]

if player1 not in move or player2 not in move:
    print(f"Invalid Choice. Choose rock, paper, scissors.")
else:
    if (player1 == "rock" and player2 == "paper") or (player1 == "scissors" and player2 == "rock") or (player1 == "paper" and player2 == "scissors"):
        print(f"Player 2 Wins!")
    elif (player2 == "rock" and player1 == "paper") or (player2 == "scissors" and player2 == "rock") or (player2 == "paper" and player1 == "scissors"):
        print(f"Player 1 Wins!")
    else:
        print(f"Both player is a Tie!")