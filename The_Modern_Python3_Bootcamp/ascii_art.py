from pyfiglet import figlet_format
from termcolor import colored
from random import choice

colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

def ascii(text, color=choice(colors)):
    return colored(figlet_format(text), color)


if __name__ == "__main__":
    text = input("What message would you like to print? ")
    color = input("What color? ")

    if color not in colors:
        color = choice(colors)

    print(ascii(text, color))


# try:
#     result = colored(figlet_format(text), color)
# except KeyError:
#     result = colored(figlet_format(text), color = choice(["red", "green", "yellow", "blue", "magenta", "cyan", "white"]))
# print(result)