import random
import time

points = 0

while True:
    datatypes = ["Pelle Svanslös", "korv", 64387484837483, 2323.232, "potatismos", True, True, True, True, "grrrr", "meow", "uwu", False, False, False, False, 567, 5511, {"this": "that", "hey": "goodbye"}, ["yes", True, "OwO", 123], 3.1415926535, 2.65, ["a", "b", "c"], {"some": "thing", "five": 5}, 10.44, "6th March 2026", 45678, 44.44, "55", "123", "56789", "3.14", None, None, None, None]
    item = random.choice(datatypes)
    start_time = time.time()

    if type(item).__name__ == "str":
        guess = input(f"What kind of datatype is '{item}'?\n> ")

    else:
        guess = input(f"What kind of datatype is {item}?\n> ")

    if guess == type(item).__name__:
        end_time = time.time()
        points += int(10 - (end_time - start_time) * 0.5)

        print("Yay that's the correct answer :D")
        print(f"You got more points! You currently have {points} points!\n ")
        # print("Wanna play again (pls say yes UwU)?")

        # quit_ans = input("(y/n)\n> ")

        # if quit_ans == "y":
        #     print("YAAYAYAYAYA")
        
        # elif quit_ans == "n":
        #     print("grrrrr")
        #     break
    
    else:
        end_time = time.time()
        points -= int(0.5 * (end_time - start_time))

        print(f"Nu uh. The correct datatype is {type(item).__name__}")
        print(f"You lost points. You currently have {points} points :(\n ")