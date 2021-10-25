# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:49:16 2021

@author: User
"""

# EX1
# def infoFunc(x, y, DoB, PoB, email, address, number = None):
#     client = {
#         'firstName': abdullokh,
#         'lastName': abdumannopov,
#         'DoB': DoB,
#         'PoB': PoB,
#         'email': email,
#         'address': address,
#         'a': number
#         }
#     return client

# print("\nInfo about client: ")
# # EX2
# clients = []
# while True:
#     abdullokh = input("First name: ")
#     abdumannopov = input("Last name: ")
#     DoB = input("Date of birth: ")
#     PoB = input("Date of place: ")
#     email = input("Email address: ")
#     address = input("Address: ")
#     number = input("Mobile number: ")
#     clients.append(infoFunc(abdullokh, abdumannopov, DoB, PoB, email, address, number))
    
#     answer = input("Do you want to add more client (Yes/No) ")
#     if answer == 'no':
#         break
    
# print("Clients: ")
# for client in clients:
#     print(
#         f"{client['firstName'].title()} {client['lastName'].title()},"
#         f"{client['a']}, {client['email']}"
#         )

# EX3
# def numbFunc(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max
# print(numbFunc(22, 10, 2))

# def maximum(a, b, c):
  
#     if (a >= b) and (a >= c):
#         largest = a
  
#     elif (b >= a) and (b >= c):
#         largest = b
#     else:
#         largest = c
          
#     return largest
# print(maximum(22, 55, 1))

# EX4
# def circleFunc(radius, pi = 3.14159):
#     infoAboutCircle ={
#         'radius': radius,
#         'diameter': radius * 2,
#         'perimeter': radius * 2 * pi,
#         "circle's face": pi * (radius **2) 
#         }
#     return infoAboutCircle
# print(circleFunc(3))
 
# EX5 does not done by me!
# def primeNumberFunc(min, max):
#     numbers = []
#     for n in range(min, max + 1):
#         prime = True
#         if n == 1:
#             prime = False
#         elif n == 2:
#             prime = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     prime = False
#         if prime:
#             numbers.append(n)
#     return numbers
# print(primeNumberFunc(41, 500))

# EX6
def Fibonacci(n):
    numbers = []
    for x in range(n):
        if x == 0 or x == 1:
            numbers.append(1)
        else:
            numbers.append(numbers[x - 1] + numbers[x - 2])
    return numbers
print(Fibonacci(10))