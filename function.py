# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:41:15 2021

@author: Abdullokh
"""

# def sayHello():
#     """ Comments for coders """
#     print("Hello, World!")
    
# sayHello()


# def sayHello(name): # Inside brackets after function name you should write PARAMETER for coders
#     """
#     # Called DOCSTRING gives  info abt function

#     Returns the name of user
#     -------
#     None.

#     """
#     print(f"Hello, dear {name.title()}")

# sayHello('Abdullokh') # after function name is called ARGUMENT for users
# sayHello('Smith')


# def fullName(name, surname):
#     """
    

#     User's first name and last name function
#     -------
#     None.

#     """
#     print(f"User's name is: {name.title()}\n"
#           f"User's surname is: {surname.title()}")
# fullName('abdullokh', 'abdumannopov')


def calculateAge(dob = 1999, currentYear = 2021):
    """
    Calculates age of users!
    """
    print(f"Born year is {dob}. Your age is {currentYear - dob}")
calculateAge(2000)
calculateAge(currentYear = 2019, dob = 1997)