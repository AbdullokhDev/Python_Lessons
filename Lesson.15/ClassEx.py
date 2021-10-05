- # Ex1:
#dad = {'name' : 'Abdusalom', 'DoB' : 1951, 'Nationality' : 'Uzbekistan'}
#mom = {'name' : 'Shohida', 'DoB' : 1956, 'Nationality' : 'Uzbekistan'}
#print(f"My father's name is {dad['name']}. He was born in {dad['DoB']}. \n When it comes to my mother She was born in {mom['DoB']}")
# products = {
#     'apple': 10000,
#     'pomegranate': 20000,
#     'grape': 40000,
#     'apricot': 30000}

 # Ex2:
#favouriteFood = {'dad' : 'palov', 'mom' : 'samsa', 'olderBrother' : 'chuchvara', 'me' : 'pizza'}
#print(f"My favourite food is {favouriteFood['me'].title()}")
# # print(products.keys())

#  Ex3:
# pythonDictionary = {'tuple' : 'list that unchangeable', 'if' : 'used for looping', 'else' : 'to continue if statement', 'integer' : 'type of object, used for numbers', 'string' : 'type of object, used for letters'}
# #print(f"If statement is {pythonDictionary['if'].upper()}")
# print("Products that can be found in our store: ")
# for product in products.keys():
#     print(product.title())

#  Ex4:
# key = input("Enter any python's terminology: ").lower()
# print(pythonDictionary.get(key, "Sorry, we do not have such word!"))
# products = {
#     'apple': 10,
#     'pomegranate': 22,
#     'grape': 40,
#     'apricot': 31}
# listToPurchase = ['bread', 'fish', 'apricot', 'grape', 'egg']
# print("Products that can be found in our store:")
# for product in products:
#     if product in listToPurchase:
#         print(f"{product.title()} {products[product]} dollar")
# for item in listToPurchase:
#     if item not in products:
#         print(f"Please, bring {item.title()} product")

# Ex5:
pythonDictionary = {'tuple' : 'list that unchangeable', 'if' : 'used for looping', 'else' : 'to continue if statement', 'integer' : 'type of object, used for numbers', 'string' : 'type of object, used for letters'}
# products = {
#     'apple': 10,
#     'pomegranate': 22,
#     'grape': 40,
#     'apricot': 31}
# # print("Products in our store: ")
# # for product in sorted(products):
# #     print(product.title())
# print(products.values())

smartphones = {
    'abdullokh':'iphone xr',
    'amir' : 'iphone xs max',
    'shakhida' : 'mi9',
    'abror':'galaxy s10 plus',
    'said':'oneplus 8pro',
    'ali':'iphone xr',
    'hojiakbar':'mi9'}
print("Users are using these phones: ")
# for smartphone in smartphones.values():
#     print(smartphone)
for smartphone in set(smartphones.values()):
        print(smartphone)

key = input("Enter some python word: ").lower()
translate = pythonDictionary.get(key)
if translate == None:
    print("Sorry, we do not have such word!")
else:
    print(f"{key.title()} means that {translate}")