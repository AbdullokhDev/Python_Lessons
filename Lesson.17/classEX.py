# name = input("Enter your name: ").lower()
# question = f"Hello, {name.title()}. How old are you? Plase enter your age: "
# age = input(question)
# age = int(age)
# height = input("How tall are you? Please enter: ")
# height = float(height)

# number = 1
# while number <= 5:
#     print(number, end = ' ')
#     number += 1
# print("Programm is finished")

# print('Squaring app!')
# question = "Enter any number to square: "
# question += "(To stop the app please write 'exit' keyword. ) "
# value = " "
# while value != 'exit':
#     value = input(question)
#     if value != 'exit':
#         print(float(value)**2)
# print("Thank you. App is finished")

# # FLAG
# print('Squaring app!')
# question = "Enter any number to square: "
# question += "(To stop the app please write 'exit' keyword. ) "
# flag = True
# while flag:
#     value = input(question)
#     if value == 'exit':
#         flag = False
#     else:
#         print(float(value)**2)
# print("Thank you. App is finished")

# # BREAK WHILE
# print('Squaring app!')
# question = "Enter any number to square: "
# question += "(To stop the app please write 'exit' keyword. ) "
# while True:  # forever loop
#     value = input(question)
#     if value == 'exit':
#         break # stop looping
#     else:
#         print(float(value)**2)
# print("Thank you. App is finished")

# # BREAK FOR
# numbers = list(range(1,11))
# for number in numbers:
#     if number == 7:
#         break
#     print(f"Square of {number} is {number**2}")

# # CONTINUE
# numbers = list(range(1,11))
# for number in numbers:
#     if number == 5:
#         continue
#     print(f"Square of {number} is {number**2}")

# # CONTINUE WHILE
# number = 0
# while number < 10:
#     number += 1
#     if number%2 != 0:
#         continue
#     else:
#         print(number)

# INFINITE LOOP
# number = 0
# while number < 10:
#     if number%2 != 0:
#         continue
#     else:
#         print(number)

number = 1
while number > 0:
    number += 1
    if number%2 != 0:
        continue
    else:
        print(number)