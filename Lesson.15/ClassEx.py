# products = {
#     'apple': 10000,
#     'pomegranate': 20000,
#     'grape': 40000,
#     'apricot': 30000}

# # print(products.keys())

# print("Products that can be found in our store: ")
# for product in products.keys():
#     print(product.title())

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

