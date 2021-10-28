# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:02:40 2021

@author: Abdulloh
"""

# LAMBDA

# import math

# length is identification not variable name
# length = lambda pi, r : 2*pi*r
# print(length(math.pi,10))

# product = lambda x, y : x ** y
# print(product(5,2))

# def degreeFunc(n):
#     return lambda x : x**n

# square = degreeFunc(2)
# cube = degreeFunc(3)
# print(f"Square of 5 is equal to {square(5)} while cube of 5 is equal to {cube(5)}")


# from math import sqrt

# numbers = list(range(11))
# root = list(map(sqrt, numbers))

# numbers = list(range(11))
# def square(x):
#     return x*x
# print(list(map(square, numbers)))

# numbers = list(range(11))
# square = lambda x : x*x
# print(list(map(square, numbers)))

# numbers = list(range(11))
# square = []
# for number in numbers:
#     square.append(number*number)
# print(square)

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x, y : x+y, a, b))
# print(a_plus_b)

# names = ['Muhammad', 'Abu Bakr', 'Umar', 'Usmon', 'Ali']
# print(list(map(lambda name : name.upper(), names)))

# import random as r

# numbers = r.sample(range(100), 10)
# def isItEvenFunc(x):
#     """
    

#     Parameters takes ten numbers from zero to one hundred
#     ----------
#     x : if x is EVEN number it

#     Returns
#     -------
#     TRUE

#     """
#     return x%2==0
# evenNumbs = list(filter(isItEvenFunc, numbers))
# print(numbers)
# print(evenNumbs)

# numbers = r.sample(range(100), 10)
# evenNumbs = list(filter(lambda x : x%2==0, numbers))
# print(numbers)
# print(evenNumbs)

# fruits = ['banana', 'melon', 'watermelon', 'apricot', 'grape', 'pomegranate', 'pear']
# fruit_b = list(filter(lambda fruit : fruit.startswith('b'), fruits ))
# print(fruit_b)

# fruits = ['banana', 'melon', 'watermelon', 'apricot', 'grape', 'pomegranate', 'pear']
# fruit_p = list(filter(lambda fruit : fruit.startswith('p'), fruits ))
# print(fruit_p)

# fruits = ['banana', 'melon', 'watermelon', 'apricot', 'grape', 'pomegranate', 'pear']
# fruit = list(filter(lambda fruit : len(fruit) <= 5, fruits))
# print(fruit)

fruits = ['banana', 'melon', 'watermelon', 'apricot', 'grape', 'pomegranate', 'pear']
start_end = list(filter(lambda fruit : (fruit.startswith('g') and fruit.endswith('e')), fruits))
print(start_end)




















