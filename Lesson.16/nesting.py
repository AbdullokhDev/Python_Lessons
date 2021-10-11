# car0 = {
#         'model':'lacetti',
#         'color':'black',
#         'year':2019,
#         'price':'$13000',
#         'transmission':'automatic'
#         }
# car1 = {
#         'model':'Nexia3',
#         'color':'white',
#         'year':2020,
#         'price':'$11000',
#         'transmission':'manual'
#         }
# car2 = {
#         'model':'Equinox',
#         'color':'black',
#         'year':2021,
#         'price':'$37000',
#         'transmission':'automatic'
#         }

# car = car1
# print(f"Car model is {car['model'].title()}.",
#       f"Price is {car['price']}.",
#       f"Color is {car['color'].upper()}")

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"Car model is {car['model'].title()}.",
#           f"Price is {car['price']}.",
#           f"Color is {car['color'].upper()}")
# type(cars)
## IN brackers you should indicate index number:
# print(f"{cars[2]['color'].title()}",
#       f"{cars[2]['model']}")

# audis= []
# for n in range(10):
#     new_car = {
#         'model':'rs7 sportback c8',
#         'color':None, #'black'
#         'year':2021,
#         'price':None, #223.877
#         'mileage':0,
#         'transmission':'eight speed automatic transmission'
#         }
#     audis.append(new_car)
# # giving color from index zero to three (check color is black only 3 cars)    
# for audi in audis[:3]:
#     audi['color']='black'
    
# for audi in audis[3:6]:
#     audi['color']='silver'
    
# for audi in audis[6:]:
#     audi['color']='red'
#     audi['transmission']='6 speed automatic transmission'

# for audi in audis:
#     if audi['transmission']=='eight speed automatic transmission':
#         audi['price']='$223.877'
#     else:
#         audi['price']='$200.00'
# for audi in audis:
#     print(audi)

coders = {
    'abdullokh':['python','js'],
    'vali':['html','css','c++'],
    'ali':['php','sql'],
    'maryam':['c++','c#']
    }
for name,programmingLanaguages in coders.items():
  print(f"\n{name.title()} knows: ")
  for programmingLanaguage in programmingLanaguages:
      print(f"{programmingLanaguage.upper()}", end=' ')
