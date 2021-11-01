# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 08:47:07 2021

@author: Abdulloh
"""

import random

print('\nFinding the number game is started>>>')

def findingNumbFunc(x=10):
    generatedNumb = random.randint(1, x)
    print(f"I think number from 1 to {x}. Can you find it?")
    guesses = 0
    while True:
        guesses += 1
        guessedNumb = int(input('\n>>>: '))
        if guessedNumb < generatedNumb:
            print('I though bigger number then you entered! Try again!')
        elif guessedNumb > generatedNumb:
            print('I though smaller number then you entered! Try again!')
        else:
            break
    print(f"Congrats. You found it in {guesses} try!")
    return guesses

def findPC(x=10):
    input(f"Think any number from 1 to {x} and press any keyboard to continue: ")
    smallest = 1
    biggest = x
    tries = 0
    while True:
        tries += 1
        if smallest != biggest:
            guess = random.randint(smallest, biggest)
        else:
            guess = smallest
        answer = input(f"You think {guess} number if it is correct, please write (T),"
                  f" or the number is bigger than this put (+) sign or it is lower than this put (-) sign ".lower())
        if answer == "-":
            biggest = guess - 1
        elif answer == "+":
            smallest = guess + 1
        else:
            break
    print(f"I found it in {tries} try!")
    return tries


def play(x=10):
    againPlay = True
    while againPlay:
        guesses_user = findingNumbFunc(x)
        guesses_pc = findPC(x)
        
        if guesses_user > guesses_pc:
            print("I win")
        elif guesses_user < guesses_pc:
            print("You win")
        else:
            print("Equal!")
        againPlay = int(input(("Do you want to play again? if yes type (1) else type (0) ")))