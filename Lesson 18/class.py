# print("List of close friends!")
# names = []
# n = 1
# while True:
#     question = f"Enter your {n} friend: "
#     name = input(question)
#     names.append(name)
#     repeat = input("Do you want add a name again? (YES/NO)")
#     n+=1
#     if repeat != 'yes':
#         break
# print("Your friends list: ")
# for name in names:
#     print(name.title())

# print("Age of your friends!")
# friends = {}
# sign = True
# while sign:
#     name = input("Enter friend's name: ")
#     age = input(f"Enter {name.title()}'s age: ")
#     friends[name] = int(age)
    
#     answer = input("Do you want to enter again? (YES/NO)")
#     if answer == "no":
#         sign = False
# for name, age in friends.items():
#     print(f"{name.title()} is {age} years old")

# cars = ['bmw', 'audi', 'chevrolet', 'ford', 'chevrolet', 'tesla','rolce royce']
# while 'chevrolet' in cars:
#     cars.remove('chevrolet')
# print(cars)

# cars = ['bmw', 'audi', 'chevrolet', 'ford', 'chevrolet', 'tesla','rolce royce']
# car = 'chevrolet'
# while car in cars:
#     cars.remove(car)
# print(cars)

students = ['Abdullokh', 'ALi', 'Vali', 'Hasan', 'Husan']
marks = {}
while students:
    student = students.pop()
    mark = input(f"Enter {student.title()}'s mark: ")
    print(f"{student} is marked with {mark}")
    marks[student] = int(mark)
print(marks)