import random

# THIS LOGIC SUCKS ASS!!! DOESN'T EVEN WORK PROPERLY

while True:
    computer_roll = random.randint(1, 6)
    player_roll = random.randint(1, 6)
    rule = input("Choose even or odd: ")

    if rule == "even":
        valid_rolls = [2, 4, 6]

        if computer_roll not in valid_rolls and player_roll in valid_rolls:
            print(f"The computer rolled {computer_roll}, but you rolled {valid_rolls}. You won!")

        else:
            print(f"The computer rolled {computer_roll}, but you rolled {player_roll}. You lost :(\n")
    
    elif rule == "odd":
        valid_rolls = [1, 3, 5]

        if computer_roll not in valid_rolls and player_roll in valid_rolls:
            print(f"The computer rolled {computer_roll}, but you rolled {valid_rolls}. You won!")
            break
        
        else:
            print(f"The computer rolled {computer_roll}, but you rolled {player_roll}. You lost :(\n")
    
    else:
        print("Please choose even or odd.\n")