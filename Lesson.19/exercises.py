# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 06:16:11 2021

@author: User
"""

# EX 1
# def calcOfAge(name, age):
#     """
    

#     Enter your name: Abdullokh
#     Enter your age: 22
#     -------
#     User's name should be indicated with his/her age!

#     """
#     # name = input("Enter your name: ")
#     # age = int(input("Enter your age: "))
#     print(f"Hey {name.title()}, your dob is {2021 - age}")
# calcOfAge("Smith", 42)

# EX 2
# def calcOfNumbs(x):
#     square = x ** 2
#     cube = x ** 3
#     print(f"Square of {x} is {square}\n"
#           f"Cube of {x} is {cube}")
# calcOfNumbs(6543)

# EX 3
# def oddOrEven(y):
#     even = y % 2
#     if even == 0:
#         print(f"{y} number is even number")
#     else:
#         print(f"{y} number is odd number")
# oddOrEven(57)

# EX 4
# def biggerOneDisplays(x, y):
#     if x > y:
#         print(f"{x} is bigger than {y}")
#     elif x < y:
#         print(f"{y} is bigger than {x}")
#     else:
#         print("Numbers are equal")
# biggerOneDisplays(21, 21)

# EX 5
# def calc(x, y):
#     """
    

#     Returns square, cube and fourth power
#     -------
#     x is the number you want to enter while y is the power of x.
#     -------
#     2 = 2 * 2, 5 = 5 * 5 * 5, 3 = 3 * 3 * 3 * 3

#     """
#     if y == 2:
#         print(f"{x}'s square is {x ** 2}")
#     elif y == 3:
#         print(f"{x}'s cube is {x ** 3}")
#     else:
#             print(f"{x}'s foruth power is {y ** 4}")
# calc(5, 4)

# EX 6
# def findingPower(x, y = 2):
#     print(f"The power of {x} is equal to {x ** y}")
# findingPower(5, 2)

# EX 7
def division(number):
    for n in range(2, 11):
        if not number % n:
            print(f"{number} divided to {n} without remainder")
division(11)