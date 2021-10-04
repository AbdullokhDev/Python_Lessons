 # Ex1:
#dad = {'name' : 'Abdusalom', 'DoB' : 1951, 'Nationality' : 'Uzbekistan'}
#mom = {'name' : 'Shohida', 'DoB' : 1956, 'Nationality' : 'Uzbekistan'}
#print(f"My father's name is {dad['name']}. He was born in {dad['DoB']}. \n When it comes to my mother She was born in {mom['DoB']}")

 # Ex2:
#favouriteFood = {'dad' : 'palov', 'mom' : 'samsa', 'olderBrother' : 'chuchvara', 'me' : 'pizza'}
#print(f"My favourite food is {favouriteFood['me'].title()}")

#  Ex3:
# pythonDictionary = {'tuple' : 'list that unchangeable', 'if' : 'used for looping', 'else' : 'to continue if statement', 'integer' : 'type of object, used for numbers', 'string' : 'type of object, used for letters'}
# #print(f"If statement is {pythonDictionary['if'].upper()}")

#  Ex4:
# key = input("Enter any python's terminology: ").lower()
# print(pythonDictionary.get(key, "Sorry, we do not have such word!"))

# Ex5:
pythonDictionary = {'tuple' : 'list that unchangeable', 'if' : 'used for looping', 'else' : 'to continue if statement', 'integer' : 'type of object, used for numbers', 'string' : 'type of object, used for letters'}

key = input("Enter some python word: ").lower()
translate = pythonDictionary.get(key)
if translate == None:
    print("Sorry, we do not have such word!")
else:
    print(f"{key.title()} means that {translate}")