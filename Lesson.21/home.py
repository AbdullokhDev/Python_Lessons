# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:02:59 2021

@author: Abdulloh
"""

# EX1
# def bigFunc(sentences):
#     for i in range(len(sentences)):
#         sentences[i] = sentences[i].title()
    
# names = ['Muhammad', 'abu bakr', 'umar', 'usmon', 'ali']
# bigFunc(names)
# print(names)

# EX2
# def bigFunc(sentences):
#     sentences = sentences[:]
#     for i in range(len(sentences)):
#         sentences[i] = sentences[i].title()
#     return sentences
    
# names = ['Muhammad', 'abu bakr', 'umar', 'usmon', 'ali']
# newNames = bigFunc(names)
# print(names)
# print(newNames)

# EX3
students = ['smith', 'john', 'chuck', 'buckley', 'jons']

def marksFunc(names):
    marks = {}
    for name in names:
        mark = input(f"Enter {name}'s mark: ")
        marks[name] = mark
    return marks
marks = marksFunc(students)
print(marks)
print(students)