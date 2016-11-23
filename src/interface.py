#file  -- interface.py --
import os

def clear_window():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def printer(type, boo):
    if type is 1:
        return "boo"
    if type is 2:
        return boo

def name():
    while True:
        z = input("Wat is je naam?")
        if z == "":
            print("Je hebt geen naam opgegeven!")
            continue
        return z

def main_menu(name):
    return "Welkom %s\n\nWat wil je doen?\n1. Voeding toevoegen\n2. Tamagotchi spelen\n3. De ranking bekijken\n4. Afsluiten\n" % name

def game_menu(name):
    return "Wat wil je doen?\n1. Geef te eten\n2. Verschoon\n3. Speel een spelletje\n4. Afsluiten\n"

def pick_number(low, high):
    while True:
        try:
            n = int(input("Maak een keuze:"))
        except ValueError:
            continue
        if n >= low or n <= high:
            if n == high:
                quit()
            else:
                return n

def quit():
    raise SystemExit

def handle(menu, number):
    return "FOO"