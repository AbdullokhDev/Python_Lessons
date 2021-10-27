# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:43:19 2021

@author: Abdulloh
"""

# import auto_module as a_m

# auto1 = auto_module.avto_info('gm', 'malibu', 'black', 'automatic', 2020, 30000)
# auto_module.info_print(auto1)

# auto2 = a_m.avto_info('gm', 'malibu', 'black', 'automatic', 2020, 30000)
# a_m.info_print(auto2)


#from auto_module import avto_info as a_i, info_print as i_p

# auto3 = a_i('gm', 'malibu', 'black', 'automatic', 2020, 30000)
# i_p(auto3)


# from auto_module import *


# import math

# x = 400
# print(math.sqrt(x))

# print(pow(2,5))


# from math import pi

#print(pi)



# import math

# print(math.log2(8))
# print(math.log10(100))


import random as r

#RANDINT(A,B)
# number = r.randint(0,100)
# print(number)

#CHOICE(X)
# names = ['Muhammad', 'Abu Bakr', 'Umar', 'Usmon', 'Ali']
# name = r.choice(names)
# print(name)
# print(r.choice(name))

x = list(range(0,100,5))
print(x)
print(r.choice(x))

#SHUFFLE(X)
x = list(range(11))
print(x)
r.shuffle(x)
print(x)