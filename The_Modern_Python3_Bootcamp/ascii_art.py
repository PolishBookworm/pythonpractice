from pyfiglet import figlet_format
from termcolor import colored
from random import choice

COLORS = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

def ascii(text, color=choice(COLORS)):
    return colored(figlet_format(text), color)


if __name__ == "__main__":
    text = input("What message would you like to print? ")
    color = input("What color? ")

    if color not in COLORS:
        color = choice(COLORS)

    print(ascii(text, color))
