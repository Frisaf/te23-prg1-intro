while True:
    user_input = input("Write something tihi: ")

    if user_input.isdigit():
        answer = input(f"Which kind of datatype is {int(user_input)}? *Looks at you nervously*\n> ")
    
    else:
        answer = input(f"Which kind of datatype is '{user_input}'? *Looks at you nervously*\n> ")

    while True:
        if user_input.isdigit() and answer in ["int", "integer"]:
            print("Yippee!! You are correct UwU.")
            break
        
        elif answer in ["str", "string"]:
            print("Yay! That's the correct answer =^U^=")
            break
        
        else:
            print("*LOUD INCORRECT BUZZER* WROOOONGGG!!!! Try again nyehehehe")
    
    quit_answer = input("Wanna play again OwO? (y/n)\n> ")

    if quit_answer == "y":
        print("Yaayyy let's play again!!")
    
    elif quit_answer == "n":
        print("Ok bye player-chan")
        break