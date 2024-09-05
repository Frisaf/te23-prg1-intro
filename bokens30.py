while True:
    try:
        answer = float(input("Type a number, any number :D\n> "))
        print(f"The squared number is {answer * answer:.2f} =^v^=")

        print(f"Let's say that your input was the side of a square. That would mean that the circumference of the square is {answer * 4:.2f} and the area is {answer ** 2:.2f}")

    except ValueError:
        print("That is not a number smh")