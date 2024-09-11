import random

# Två spelare
# Spelare 1 rullar tärning, spelare 2 rullar en tärning. Se vem som rullade högst och se vem som rullade högst. Högst vinner. Upprepa tills någon har vunnit allt (bäst av 3)

player1_points = 0
player2_points = 0
rounds = 0
play_game = "y"

while play_game == "y":
    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)

    print(f"This is round {rounds + 1}")
    print(f"Player 1 rolled: {player1_roll}")
    print(f"Player 2 rolled: {player2_roll}")

    if player1_roll > player2_roll:
        print("Player 1 won.")

        player1_points = player1_points + 1
        rounds = rounds + 1

        print(f"The standing is:\n1: {player1_points} | 2: {player2_points}")
        input("Press enter to continue")
    
    elif player1_roll < player2_roll:
        print("Player 2 won.")

        player2_points  = player2_points + 1
        rounds = rounds + 1

        print(f"The standing is:\n1: {player1_points} | 2: {player2_points}")
        input("Press enter to continue")
    
    elif player1_roll == player2_roll:
        print("Your roles were equal.")
    
    if rounds == 3:
        if player1_points > player2_points:
            print("PLAYER 1 WON IT ALL!")
            play_game = input("Do you want to play again? y/n\n> ").lower()
        
        elif player1_points < player2_points:
            print("PLAYER 2 WON IT ALL!")
            play_game = input("Do you want to play again? y/n\n> ").lower()
    
    else:
        continue