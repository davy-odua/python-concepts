#FUNCTIONS
#Defining functions and arguments
def add(a,b):
    return a + b

result = add(1,2)
print(result)

def rect_area(length, width):
    area = length * width
    return area

result = rect_area(12,12)
print(f"The area is {result}")

def allow_enter(age, hasId):
    if age >= 18 and hasId:
        print("You can enter")
    else:
        print("You cannot enter")

allow_enter(18, True)

def greater_20(*numbers):

    for number in numbers:
        if number > 20:
            print(number)

greater_20(5,10,15,20,25,30,35,40)

def separate_adults_children(*ages):
    for age in ages:
        if age >= 60:
            print(f"{age} is old")
        elif age >= 18:
            print(f"{age} Adult")
        else:
            print(f"{age} Child")



separate_adults_children(21,15,13,90,50,40)

#Keyword Arguments
def increment(number, by):
    return number + by

print(increment(12, by=2))

#Default Arguments
def increase(number, by = 2):
    return number + by

print(increase(7))

#A function that takes a variable number og arguments (xarguments)
def greater_20(*numbers):

    for number in numbers:
        if number > 20:
            print(number)

greater_20(5,10,15,20,25,30,35,40)

def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total

result = multiply(1,2,3)
print(f"The result is {result}")


#(xxarguments) = This has multiple keyword value pairs
def details(**user):
    print(f"{user["id"]} - {user["name"]}")

details(id = 1, name = "David")
details(id = 2, name = "Kevin")

#scope = The area that a variable is defined
message1 = 1 #This message variable is a global variable since it acn be accessed anywhere in the code program

def greets():
    message2 = 2 #This message variable is a local variable since it can only be accessed through the greets function above.
    return message2 #The scope of this message variable is the greets function. It only exists inside this function.

print(greets())

