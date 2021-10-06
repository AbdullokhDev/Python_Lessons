# #Ex1:
# pythonDictionary = {
#     'if' : 'statement returns true or false',
#     'tuple' : 'used to store multiple items in a single variable',
#     'list' : 'used for changable list',
#     'for' : 'used for looping the function',
#     '%' : 'modular division is used to find remainder',
#     'array' : 'used to save many values of the the same data',
#     'dictionary' : 'used for store the data',
#     }
# print("List: ")
# for a, b in sorted(pythonDictionary.items()):
#     print(f"{a.title()} means that {b.upper()}")

# #Ex2:
# countries = {
#     'Uzbekistan' : 'Tashkent',
#     'USA' : 'washington D.C',
#     'Argentina' : 'Buenos Aires',
#     'Australia' : 'Canberra',
#     'Colombia' : 'Bogota',
#     'Japan' : 'Tokyo',
#     'Germany' : 'Berlin',
#     'Egypt' : 'Cairo',
#     'United Kingdom	' : 'London',
#     'Norway' : 'Oslo'
#     }
# print('Countries of the world: ')
# for country in sorted(countries):
#     print(country.upper())
# print("The capitals of the countries: ")
# for capital in sorted(countries.values()):
#     print(capital)

# #Ex3:
# countryName = input("Enter any country you would like to visit: ").lower()
# capital = countries.get(countryName)
# if capital == None:
#     print("Sorry we does not offer for this country")
# else:
#     print(f"Congratulations, you can go {countryName.title()} country. It's capital is {capital.title()}")

#Ex4:
menu = {
        'fish tacos' : '$15',
        'mixed green salads' : '$7.99',
        'shrimp' : '$20',
        'raw oysters' : '$27',
        'sweet potato fries' : '$9.49',
        'cheese fries' : '$10.49',
        'chicken tenders' : '$14.99',
        'vanilla ice cream' : '$10',
        'tuna' : '$5',
        'whipped potato' : '$10'
        }
# for f in range(3):
#     print(input(f"Enter {f+1} meal: "))
# for f, p in menu:
#     if f in menu.items():
#         print(f"{f} is can be find in our restaurant. Price is {p}")
#     else:
#             print("Sorry")

print('Enter three meals from menu: ')
orders = []
for n in range(3):
    orders.append(input(f"{n+1} meals is: ").lower())
    
for order in orders:
    if order in menu:
        print(f"Entered meal {order.upper()} is available. Price is {menu[order]}")
    else:
            print(f"Sorry, we do not have {order.upper()}")