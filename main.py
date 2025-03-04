from getpass import getpass as input
player_1_score = 0
player_2_score = 0
while True:
  player_1 = input("Enter R for Rock, P for Paper or S for Scissors (Your input will be hidden upon being typed so type and then press space to continue): ")
  player_2 = input("Enter R for Rock, P for Paper or S for Scissors (Your input will be hidden   upon being typed so type and then press space to continue): ")
  if player_1 == "R" or player_1 == "r":
    if player_2 == "R" or player_2 == "r":
      print("Draw")
    elif player_2 == "P" or player_2 == "p":
      print("Player 2 wins!")
      player_2_score += 1
    elif player_2 == "S" or player_2 == "s":
      print("Player 1 wins!")
      player_1_score += 1
    else:
      print("Invalid input from Player 2")
  elif player_1 == "P" or player_1 == "p":
    if player_2 == "R" or player_2 == "r":
      print("Player 1 wins!")
      player_1_score += 1
    elif player_2 == "P" or player_2 == "p":
      print("Draw")
    elif player_2 == "S" or player_2 == "s":
      print("Player 2 wins!")
      player_2_score += 1
    else:
      print("Invalid input from Player 2")
  elif player_1 == "S" or player_1 == "s":
    if player_2 == "R" or player_2 == "r":
      print("Player 2 wins!")
      player_2_score += 1
    elif player_2 == "P" or player_2 == "p":
      print("Player 1 wins!")
      player_1_score += 1
    elif player_2 == "S" or player_2 == "s":
      print("Draw")
    else:
      print("Invalid input from Player 2")
  else:
    print("Invalid input from Player 2")
  if player_1_score == 3:
    print("Player 1 wins the whole game")
    exit()
  elif player_2_score == 3:
    print("Player 2 wins the whole game")
    exit()
  else:
    continue
