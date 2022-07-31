# Tic tac toe
# Game between human and computer

# Importing modules used for displaying instructions
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    """Displays game instructions"""
    print(colored(figlet_format("WElCOME TO TIC TAC TOE!"), color = choice(["red", "green", "yellow", "blue", "magenta", "cyan", "white"])))
    print(
        """
        To play, you will pick the number of the field according to the following scheme:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

        Are you ready? Then let's rock!
        """
    )

def main():
    display_instruct()

if __name__ == "__main__":
    main()