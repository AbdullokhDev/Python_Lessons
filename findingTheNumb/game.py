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

def findMyNumbFunc(y=10):
    generatedNumb = random.randint(1,y)
    
    while True:
        sign = input("")
        