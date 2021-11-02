# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:13:50 2021

@author: Abdulloh
"""

import random
from uzwords import words

def getWordF():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def displayF(user_letters,word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter -= "-"
    return display_letter

def playF():
    word = getWordF()
    wordLetters = set(word)
    user_letters = ''
    print(f"I think {len(word)} character of word. Can you find it?")