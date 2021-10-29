# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 08:47:07 2021

@author: Abdulloh
"""

import random as r


print('\nFinding the number game is started>>>')

number = []
getValue = r.sample(range(10), 1)
print(getValue)

print('I thinked the number')

def pcNumber(x):
    guess = input("Guess the number: ")
    while True:
        