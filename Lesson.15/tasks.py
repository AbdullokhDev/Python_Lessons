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
countries = {
    'Uzbekistan' : 'Tashkent',
    'USA' : 'washington D.C',
    'Argentina' : 'Buenos Aires',
    'Australia' : 'Canberra',
    'Colombia' : 'Bogota',
    'Japan' : 'Tokyo',
    'Germany' : 'Berlin',
    'Egypt' : 'Cairo',
    'United Kingdom	' : 'London',
    'Norway' : 'Oslo'
    }
# print('Countries of the world: ')
# for country in sorted(countries):
#     print(country.upper())
# print("The capitals of the countries: ")
# for capital in sorted(countries.values()):
#     print(capital)

#Ex3:
countryName = input("Enter any country you would like to visit: ").lower()
capital = countries.get(countryName)
if capital == None:
    print("Sorry we does not offer for this country")
else:
    print(f"Congratulations, you can go {countryName.title()} country. It's capital is {capital.title()}")