# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:32:55 2021

@author: Abdulloh
"""

# def multiplicationFunc(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
# print(multiplicationFunc(5,2,7,687,6765,987))

# EX2
def studentInfoFunc(firstName, lastName, **kwargs):
    kwargs['firstName']=firstName.title(),
    kwargs['lastName']=lastName.title()
    return kwargs
student1 = studentInfoFunc('abdullokh', 'abdumannopov', dob=1999, study='wiut')
student2 = studentInfoFunc('roy', 'jones')
students = [student1, student2]
print(students)