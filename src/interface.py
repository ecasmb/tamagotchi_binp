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
    return str("Welkom", name, "\nWat wil je doen?\n1. Voeding toevoegen\n2. Tamagotchi spelen\n3. De ranking bekijken\n 4. Afsluiten\n\n")

def pick_number(low, high):
    while True:
        n = input("Maak een keuze:")
        if n >= low or n <= high:
            return n

def handle(menu, number):
    return "FOO"