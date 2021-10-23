# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:49:16 2021

@author: User
"""

def infoFunc(firstName, lastName, dob, email = "", mobileNumber = None):
    client ={
        "firstName": firsName,
        "lastName": lastName,
        "dob": dob,
        "age": 2021 - age,
        "email" : email,
        "mobileNumber": number,
        }
    return client
print("Enter about client info: ")
clients = []
while True:
    firstName = input("First name: ")
    lastName = input("Last name: ")
    dob = input("Date of birth: ")
    email = input("Email address: ")
    mobileNumber = input("Mobile number: ")
    clients.append(infoFunc(firstName,lastName, dob, email, mobileNumber))