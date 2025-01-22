map = [
    [0, 0, 0, "W"],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
]

for column in map:
    for item in column:
        if item == 1:
            player_pos_x = column.index(1)
            player_pos_y = map.index(column)

player_position = {
    "X": player_pos_x,
    "Y": player_pos_y,
}

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
    
    else:
        map[player_pos_y][player_pos_x] = 1