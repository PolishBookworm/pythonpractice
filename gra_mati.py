# -*- coding: utf-8 -*-

# WWII simulation w/ password & Python info

# imports
from random import choice
from time import sleep
from datetime import date
from pwinput import pwinput

# global constants
PASSWORD = "HASŁO_MASŁO"
PYTHON_RELEASE_DATE = 1990

def menu():
    print("\n\n"
            "Pomoc........0\n"
            "O Pythonie...1 \n"
            "GRA..........2")

    x = input()
    if x == "0":
        prog_help()
    elif x == "1":
        py_info()
    elif x == "2":
        game()

def prog_help():
    """help function, currently does absolutely nothing"""
    menu()

def py_info():
    """gives you info about python"""
    python_age = date.today().year - PYTHON_RELEASE_DATE
    print(f"""Cześć, nazywam się Python.
            Jestem językiem programowania stworzonym przez Guida van Rossum. Mam {python_age} lat.""")
    menu()
    

def game():
    """WWII simulation"""
    print("Witamy w grze!")

    user = 0
    comp = 0

    while True:
        print("""
        Symulacja bitwy:
        alianci
        vs III Rzesza
        vs Armia Czerwona.
        """)
        print(("Obsługa gry:\n"
                "Głosujesz na...\n"
                "a - alianci\n"
                "n - niemcy\n"
                "c - armia czerwona\n"
                "__________________\n"
                "0 - zakończenie gry\n\n"

                "Wpisz 0, n, c lub a."
        ))
        x = input()
        if x == '0':
            break
        elif x == 'a':
            x = "alianci"
        elif x == 'n':
            x = "niemcy"
        elif x == 'c':
            x = "armia czerwona"
        else:
            continue

        y = choice(["alianci", "niemcy", "armia czerwona"])

        for i in range(0, 3):
            print(3 - i)
            sleep(1)

        print("Wynik rzutu: ", y)

        if x == y:
            user += 1
        else:
            comp += 1

        print("Twoje wyniki:")
        print(f"Liczba odgadniętych wyników: {user}")
        print(f"Liczba nieodgadniętych wyników: {comp}")


# welcome screen & password input

print("Witaj w systemie")

user_input = pwinput("Wprowadź hasło: ")

if user_input != PASSWORD:
    print("Brak dostępu!!!\n"
          "Aby spróbować jeszcze raz, ponownie uruchom program.")

else:
    print("Dostęp został udzielony!\n")

    menu()
 



input("\n\nAby zakończyć, wciśnij klawisz Enter.")