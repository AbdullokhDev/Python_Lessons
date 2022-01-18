# Ex1

# def calc_year(name, age):
#     print(f"Name is: {name.upper()}\n"
#           f"He was born in {2022-age}")

# calc_year(age=23, name="abdullokh")

# Ex2

# def calc_square_cube(numb):
#     print(f"{numb} x {numb} = {numb**2}\n"
#           f"cube of {numb} is equal to {numb**3}")

# calc_square_cube(2)

# Ex3

# def odd_or_even(number):
#     if number % 2 == 0:
#         print(f"Entered number({number}) is even")
#     else:
#         print(f"Entered number({number}) is odd")

# odd_or_even(456760)

# Ex4

# def display_bigger_number(numb1, numb2):
#     if numb1 == numb2:
#         print("They are equal!")
#     elif numb1 > numb2:
#         print(f"First number is bigger {numb1}")
#     else:
#         print("Error! Try again")


# display_bigger_number(55, 34)

# Ex5

# def power_of_smth(x, y):
#     print(f"x = {x} and y = {y}\n"
#           f"{x ** y}")

# power_of_smth(2, 4)

# Ex6
def division(number):
    for n in range(2, 11):
        if not number % n:
            print(f"{number} divisible by {n}")

division(7)