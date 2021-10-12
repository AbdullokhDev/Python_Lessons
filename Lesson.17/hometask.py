# EX1
# print('Favorite books app!')
# question = "What kind of book is your favourite one?"
# question += " (If you want to stop the app, please write 'stop' keyword)"
# value = " "
# while value != 'stop':
#     value = input(question)
#     if value != 'stop':
#         print(value)
# print("Thank you. App is finished!")

# print('Favorite books app!')
# question = "What kind of book is your favourite one?"
# question += " (If you want to stop the app, please write 'stop' keyword)"
# flag = True
# while flag:
#     value = input(question)
#     if value == 'stop':
#         flag = False
#     else:
#          print(value)
# print("Thank you. App is finished!")

# print('Favorite books app!')
# question = "What kind of book is your favourite one?"
# question += " (If you want to stop the app, please write 'stop' keyword)"
# while True:
#     value = input(question)
#     if value == 'stop':
#         break
#     else:
#           print(value)
# print("Thank you. App is finished!")

# EX2
# print("The price of wallet for theater app!")
# question = "Please, enter your age"
# question += " (If you want to stop the app, please write 'exit' or 'quit' keywords.)"
# while True:
#     value = input(question)
#     if value == 'quit' or value == 'exit':
#         break
#     age = int(value)
    
#     if age < 7:
#         price = '$20'
#     elif 7 <= age <= 18:
#         price = '$30'
#     elif 18 <= age <= 65:
#         price = '$50'
#     else:
#         price = 0
        
#     if price == 0:
#         print("It is free for you")
#     else:
#         print(f"Wallat's price is {price}")
# print("Thank you. App is finished!")

# EX3
print("Finding root of the number app!")
data = "Please enter posite number: "
data += "(In order to stop the app, please write 'stop' keyword)"
while True:
    number = input(data)
    if number == 'stop':
        break
    elif float(number) < 0:
        continue
    else:
        root = float(number)**(0.5)
        print(f"Entered number is {number} and its root is equal to {root}")
print("Thank you. App is finished!")
        
    