import random, time
from time import sleep

map = [
    [0, 0, 0, "W"],
    ["~", "~", "~", "~"],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
]

for column in map:
    for item in column:
        if item == 1:
            player_pos_x = column.index(1)
            player_pos_y = map.index(column)

def word_type():
    words = ["stab", "wind", "promise", "deer", "debt", "legislation", "offend", "directory", "arrogant", "lock", "hang", "god", "lend", "prediction", "crevice", "responsibility", "original", "snow", "wheel", "provide", "ear", "tribute", "decrease", "transfer", "nomination", "donor", "liberal", "orientation", "mist", "training", "depend", "possible", "provincial", "bread", "list", "assertive", "production", "distinct", "orthodox", "assume", "camera", "railroad", "morning", "night", "button", "intention", "late", "early", "sentence", "cage", "pupil", "protection", "depression", "computer", "goalkeeper", "couple", "format", "agent", "brick", "common", "evolution", "deputy", "relieve", "vegetable", "reader", "aluminum", "feat", "evening", "memory", "desk", "or", "sleeve", "relax", "mouth", "reserve", "forecast", "vacuum", "nature", "pin", "regret", "prevalence", "bomber", "comfort", "democratic", "penny", "outer"]
    count = 0
    correct_count = 0
    
    while count < 3:
        word = random.choice(words)
        print(word)
        start_time = time.time()
        inp = input("> ")

        if inp == word:
            print("Correct!")
            correct_count += 1
        
        else:
            print("Wrong!")

        count += 1

        end_time = time.time()
        result_time = end_time - start_time

        if result_time > 5 and inp == word:
            print("But you were too slow!")
            
            correct_count -= 1
        
        elif result_time > 5 and inp != word:
            print("And you were too slow!")
    
    if correct_count >= 2:
        print("You successfully swam over!")
    
    else:
        print("You unfortunately did not make it. You died.")
        sleep(3)
        quit()

while True:
    for row in map:
        print(row)

    print("\nWhere do you want to go?")

    move = input("> ")
    error_msg = "You cannot go that way."

    if move == "w":
        if player_pos_y == 0:
            print(error_msg)
        
        else:
            map[player_pos_y][player_pos_x] = 0
            player_pos_y -= 1

    elif move == "a":
        if player_pos_x == 0:
            print(error_msg)
        
        else:
            map[player_pos_y][player_pos_x] = 0
            player_pos_x -= 1

    elif move == "s":
        if player_pos_y == 3:
            print(error_msg)
        
        else:
            map[player_pos_y][player_pos_x] = 0
            player_pos_y += 1

    elif move == "d":
        if player_pos_x == 3:
            print(error_msg)
        
        else:
            map[player_pos_y][player_pos_x] = 0
            player_pos_x += 1
    
    else:
        print("Please provide a position: w, a, s, d")

    if map[player_pos_y][player_pos_x] == "W":
        print("You won!")
        map[player_pos_y][player_pos_x] = 1

        for row in map:
            print(row)

        break

    elif map[player_pos_y][player_pos_x] == "~":
        print("Oh no! You've encountered a stream. You need to swim across it.")
        print("Type the words that appear in your terminal to succeed!")
        word_type()
        
        player_pos_y -= 1
        map[player_pos_y + 1][player_pos_x] = "~"
        map[player_pos_y][player_pos_x] = 1
    
    else:
        map[player_pos_y][player_pos_x] = 1