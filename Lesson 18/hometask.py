# EX1
# print("Order application!")
# cartOne = []
# n = 1
# while True:
#     product = input(f"{n} Enter product name: ")
#     cartOne.append(product)
#     question = input("Do you want to add more product? (Y/N) ")
#     n += 1
#     if question != 'y':
#         break
# print(cartOne)
# EX2
# print("E-commerce online market application!")
# cart = {}
# flag = True
# while flag:
#     product = input("Enter product's name: ")
#     price = input(f"Enter {product.title()}'s price in dollars: ")
#     cart[product] = int(price)
    
#     question = input("Do you want to add more product? (Yes/No) ")
#     if question == 'no'.lower():
#         flag = False
        
# for product, price in cart.items():
#     print(f"Price of {product.upper()} is equal to ${price}")
# EX3
orders = ['apple', 'banana', 'apricot', 'melon']
products = {
    'apple':5,
    'banana':6,
    'watermelon':3,
    'grape':4,
    'fig':10,
    'pomegranate':4
    }
while products:
    order = orders.pop()
    if order in products.keys():
        price = products[order]
        print(f"The {order.upper()} price is ${price}")
    else:
        print(f"We do not have {order.title()}")