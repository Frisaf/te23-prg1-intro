seat_types = [
    "chair",
    "stool",
    "floor",
    "table",
]

run_program = True

while run_program:
    choice = int(input("\nWhat do you want to do?\n\n[1] Print seat types\n[2] Add seat type\n[3] Remove seat type\n[4] Exit\n> "))

    try:
        if choice == 1:
            print("SEAT TYPES:")

            for seat in seat_types:
                print(seat.title())
        
        elif choice == 2:
            new_seat = input("Add a seat\n> ")

            seat_types.append(new_seat)
        
        elif choice == 3:
            removed_seat = input("Which seat do you want to remove?\n> ").lower()

            if removed_seat not in seat_types:
                print("Please provide a valid answer")
            
            else:
                print(f"Removing {removed_seat} from the list.")

                seat_types.remove(removed_seat)
        
        elif choice == 4:
            print("Okay")
            run_program = False

        else:
            print("Please provide a valid answer.")
    
    except ValueError:
        print("Please provide a valid answer")