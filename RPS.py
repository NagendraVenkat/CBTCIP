values = ["Rock", "Paper", "Scissors"]

Player_1 = input()

Player_2 = input()

if Player_1 == "Rock" and Player_2 == "Paper":
    print("Player_2 won the match")
elif Player_1 == "Rock" and Player_2 == "Scissors":
    print("Player_1 won the match")
elif Player_1 == "Paper" and Player_2 == "Scissors":
    print("Player_2 won the match")
elif Player_1 == "Paper" and Player_2 == "Rock":
    print("Player_1 won the match")
elif Player_1 == "Scissors" and Player_2 == "Rock":
    print("Player_2 won the match")
elif Player_1 == "Scissors" and Player_2 == "Paper":
    print("Player_1 won the match")
else:
    print("Match Drawn")