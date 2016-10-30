# -*- coding: utf-8 -*-
'__author__:TomatoSoupM8'

import random

# możliwość wyboru języka
def chooseLanguage():
    print("_____Choose your language of the game_____")
    print("___1. English___")
    print("___2. Polski____")
    choose = input("Type the number: ")
    if choose == "1":
        gameEN()
    elif choose == "2":
        gamePL()

def gameEN():
    print ("___Goal of the Game: Guess a number between 1 and 100___")
    found = False
    # losowanie liczby z przedziału 1-100
    randomNumber = random.randint(1, 100)
    while not found:
        # odpowiedź gracza
        userGuess = int(input("Your Guess: "))
        # jeśli zgadnie
        if userGuess == randomNumber:
            print ("You got it!")
            found = True
        # jeśli jego liczba jest większa od wylosowanej
        elif userGuess > randomNumber:
            print ("Guess lower!")
        # jeśli jego liczba jest mniejsza od wylosowanej
        else:
            print ("Guess higher!")
            
def gamePL():
    print("___Cel gry: Zgadnij liczbe pomiędzy 1 a 100___")
    found = False
    # losowanie liczby z przedziału 1-100
    randomNumber = random.randint(1, 100)
    while not found:
        # odpowiedź gracza
        userGuess = int(input("Twoja odpowiedź: "))
        # jeśli zgadnie
        if userGuess == randomNumber:
            print("Zgadłeś!")
            found = True
        # jeśli jego liczba jest większa od wylosowanej
        elif userGuess > randomNumber:
            print("Zgaduj niżej")
        # jeśli jego liczba jest mniejsza od wylosowanej
        else:
            print("Zgaduj wyżej")

if __name__ == '__main__':
    chooseLanguage()
