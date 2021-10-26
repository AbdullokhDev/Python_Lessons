# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:58:45 2021

@author: Abdulloh
"""

# here five mandatory argument and only one optional argument which is price
# def autoInfoFunc(company, model, color, transmission, year, price = None):
#     auto = {
#         'company': company,
#         'model': model,
#         'color': color,
#         'transmission': transmission,
#         'year': year,
#         'price': price
#         }
#     return auto
# auto1 = autoInfoFunc('Gm', "Malibu", "black", "auto", 2021)
# auto2 = autoInfoFunc('Gm', "spark", "white", "manual", 2019, 7500)
# autos = [auto1, auto2]
# print(autos)

# def sumFunc(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#         # total += 1
#     return total
# print(sumFunc(1,2))
# print(sumFunc(1,2,3,4,5))
# print(sumFunc(4,5,6,7,8,9))

# def sumFunc(*numbers):
#     return sum(numbers)
# print(sumFunc(55,44,9,3543,354357,36))

# def sumFunc(x,y,*numbers):
#     return x+y+sum(numbers)
# print(sumFunc(55,44))
# print(sumFunc(55,44,45,45,78))
# print(sumFunc(55)) # shows: TypeError: sumFunc() missing 1 required positional argument: 'y'

def autoInfoFunc(company, model, **info):
    info['company']=company,
    info['model']=model
    return info
auto1 = autoInfoFunc("Gm", "Malibu", color="black", transmision="auto", year=2021)
auto2 = autoInfoFunc("Gm", "spark", color="white", transmission="manual", year=2019, price=7500)
autos = [auto1, auto2]
print(autos)