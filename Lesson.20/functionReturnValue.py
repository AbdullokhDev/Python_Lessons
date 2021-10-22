# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:06:16 2021

@author: User
"""

# def giveFullName(firstName, lastName):
#     """
    

#     Parameters
#     ----------
#     fistName : TYPE - string
#         DESCRIPTION.
#     lastName : TYPE - string
#         DESCRIPTION: displays full name

#     Returns name
#     -------
#     None.

#     """
#     fullName = f"{firstName} {lastName}"
#     return fullName()
# student1 = giveFullName('Abdullokh', 'Abdumannopov')
# student2 = giveFullName("John", "Smith")
# print(f"Today, {student1} and {student2} are absent")   

# def createFullName(firstName, lastName, middleName = ''):
#     if middleName:
#         fullName = f"{firstName} {middleName} {lastName}"
#     else:
#         fullName = f"{firstName} {lastName}"
#     return fullName.title()
# student1 = createFullName('Abdullokh', 'Abdumannopov')
# student2 = createFullName('John', 'smith', 'smthMiddle')
# print(f"Today, {student1} and {student2} were absent!")

def auto_info(company, model, color, transmission, year, price = None):
    auto = {
        'company':company,
        'model':model,
        'color': color,
        'transmission': transmission,
        'year': year,
        'price': price
        }
    return auto
# auto1 = auto_info("GM", "Malibu", "Black", "Automatic", 2018)
# auto2 = auto_info("GM", "Gentra", "Whilte", "Mechanical", 2020 , "%15.000")
# autos = [auto1, auto2]
# print('Cars that exist right now: ')
# for auto in autos:
#     if auto['price']:
#         price = auto['price']
#     else:
#         price = 'Sorry, unknown'
#     print(f"{auto['color']} {auto['model']}. Price is: {price}")

# def rangeTest(min, max):
#     numbers = []
#     while min < max:
#         numbers.append(min)
#         min += 1
#     return numbers
# print(rangeTest(0,10))

# list(range(0,10))
# Out[34]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Autos list in our auto salon!")
autos = []
while True:
    print("\nEnter the fields: ", end = ' ')
    company = input("Comany name: ")
    model = input("Model name: ")
    color = input("Color: ")
    transmission = input("Transimission: ")
    year = input("Enter produced year: ")
    price = input("Price of car: ")
    
    autos.append(auto_info(company, model, color, transmission, year, price))
    
    answer = input("Do you want to enter car again? (Yes/No) ")
    if answer == 'no':
        break

print("\nCars in our  auto salon: ")
for auto in autos:
    if auto['price']:
        price = auto['price']
    else:
        price = 'Sorry, unknown'
    print(f"{auto['color']} {auto['model']}. Price is: {price}")