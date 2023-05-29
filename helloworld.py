print("Hi Everyone")

username = "Shivam"
#print(username, "is Awesome")  
def somefunc():
        global username
        print(username,"is Awesome")
        username = "Tithi"

somefunc()
print(username, "is Awesome")  

             

[print(x) for x in range(5)]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

myNewList = list()

#populate new list with all the elements in 'fruits' list having character 'a'

for fruit  in fruits:
        if 'a' in fruit:
                myNewList.append(fruit)

print("New fruit list:",myNewList)



"""
creating same list with list comprehension
"""

myNewList.clear()

print("mynewList cleared",myNewList)

myNewList = [x for x in fruits if 'a' in x]
print(myNewList)
[print(x.upper()) for x in myNewList]


#tuple
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))
print(thistuple)

car = {
        "brand" : "maruti suzuki",
        "makeYear" : "2020",
        "model": "swift",
        "variant": "zxi"
}

print(car.keys())
print(car.values())
print(car.items())
car["model"] = "G wagon"
print(car.items())