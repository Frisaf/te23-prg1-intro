import os
import time
import sys
import winsound

def loading_bar():
    for i in range(101):
        time.sleep(0.01)
        bar = set_color("green") + "#" * (i // 2) + set_color("reset")
        sys.stdout.write(f"\rLoading... [{bar:<59}] {i}%")
        sys.stdout.flush()
    print()

def set_color(color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    return colors.get(color, colors["reset"])

def play_christmas_melody():
    # Define the notes and their durations (frequency, duration in ms)
    melody = [
        (392, 500), (392, 500), (440, 500), (392, 500), (523, 500), (494, 1000),
        (392, 500), (392, 500), (440, 500), (392, 500), (587, 500), (523, 1000),
        (392, 500), (392, 500), (784, 500), (659, 500), (523, 500), (494, 500), (440, 1000),
        (698, 500), (698, 500), (659, 500), (523, 500), (587, 500), (523, 1000)
    ]
    for freq, duration in melody:
        winsound.Beep(freq, duration)

def main():
    name = input("Hej, vad heter du? ")
    os.system("cls" if os.name == "nt" else "clear")
    loading_bar()

    snowflake = set_color("cyan") + "* * *" + set_color("reset")
    santa = set_color("red") + "🎅" + set_color("reset")
    tree = set_color("green") + "🎄" + set_color("reset")
    greeting = set_color("red") + "God Jul och Gott Nytt År!" + set_color("reset")
    user_name = set_color("cyan") + name + set_color("reset")
    message = f"""
        {snowflake} {santa} {tree}
        {greeting} {user_name}!
        {tree} {santa} {snowflake}
    """

    print(set_color("red") + message + set_color("reset"))
    play_christmas_melody()

if __name__ == "__main__":
    main()