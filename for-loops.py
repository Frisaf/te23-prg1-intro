# seat_types = [
#     "chair",
#     "stool",
#     "floor",
#     "table",
# ]

seat_type_dict = {
    "chair": "A type of seat, typically designed for one person and consisting of one or more legs, a flat or slightly angled seat and a back rest. Optionally, it may also feature arm rests.",
    "stool": "A type of seat, typically designed for one person and consisting of one or more legs, but no back rest. Modern versions of stools may however feature one.",
    "floor": "Not typically a place where you sit, but may be sat on. It is however usually used for walking on and is often described as the lower surface of the room.",
    "table": "Not typically a place where you sit, but may be sat on. It is a piece of furniture with raised legs and a flat top, and is often supported by four legs, but may have fewer or more legs. It is often used as a surface for working at, eating or place things on.",
}

run_program = True

while run_program:
    choice = int(input("\nWhat do you want to do?\n\n[1] Print seat types\n[2] Add seat type\n[3] Remove seat type\n[4] Sort list\n[5] View item info\n[6] Exit\n> "))

    try:
        if choice == 1:
            print("SEAT TYPES:")

            seat_type_list = list(seat_type_dict.keys())

            for index, seat in enumerate(seat_type_list):
                print(f"{index + 1}. {seat.title()}")
        
        elif choice == 2:
            new_seat = input("Add a seat\n> ")

            seat_type_dict[new_seat] = "Custom item that may be sat on."
        
        elif choice == 3:
            removed_seat = int(input("Which seat do you want to remove?\n> "))
            seat_type_list = list(seat_type_dict.keys())

            print(f"Removing number {removed_seat} from the list.")

            item = seat_type_list.pop(removed_seat - 1)
            seat_type_dict.pop(item)
        
        elif choice == 4:
            print("Sorting list...")

            seat_type_list = list(seat_type_dict.keys())
            seat_type_list.sort()
            
            for index, seat in enumerate(seat_type_list):
                print(f"{index + 1}. {seat.title()}")
        
        elif choice == 5:
            print("SEAT TYPES:")
            for seat, description in seat_type_dict.items():
                print(f"- {seat.upper()}: {description}\n")
        
        elif choice == 6:
            print("Okay")
            run_program = False

        else:
            print("Please provide a valid answer.")
    
    except ValueError:
        print("Please provide a valid answer")