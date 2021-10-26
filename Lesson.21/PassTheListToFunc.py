# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:17:18 2021

@author: Abdulloh
"""

# def marksFunc(names):
#     marks = {}
#     while names:
#         name = names.pop()
#         mark = input(f"Enter mark of {name.title()} student: ")
#         marks[name] = int(mark)
#     return marks

# students = ['Muhammad', 'Abu Bakr', 'Umar', 'Usmon', 'Ali']
# marks = marksFunc(students)
# print(marks)

def phoneFunc(models):
    priceDic = {}
    while models:
        model = models.pop()
        price = input(f"Enter {model.upper()} model price: ")
        priceDic[model] = int(price)
    return priceDic

mobilePhones = ['iphone x', 'samsung s10', 'nokia 3310', 'oneplus eight pro']
priceDic = phoneFunc(mobilePhones[:])
print(priceDic)