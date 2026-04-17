#Comparison operators, logical operators, Conditional statements: if, elif, else, Loops: for, for..else, iterables, while

#Comparison Operators = These compare two values then return true or false

print(5 != 6)
print(5 >= 5)
print(5 == 4)
print(5 <= 3)

#Logical operators = They include and , or , not

age = 20
has_licence = True

if age >=21 and has_licence:
    print("Eligible to drive")
if age < 21 or not has_licence:
    print("Not eligible to drive")


years = 18
has_id = False

if years >= 18 and has_id == True:
    print("Allowed to vote.")
else:
    print("Not allowed to vote")


#Conitional Statements (if, elif, else)

grade = 40

if grade >= 70:
    print("GRADE: A")
elif grade >= 60:
    print("GRADE: B")
elif grade >= 50:
    print("GRADE: C")
elif grade >= 40:
    print("GRADE: D")
else:
    print("FAIL")

print("LOOPS")

#Loops = They include for, for..else, iterables, while
#For loop

vegetables = ["Kale", "Spinach", "Mrenda", "Kunde", "Skumawiki", "Cabbage"]

for vegetable in vegetables:
    print(vegetable)

for i in range(1, 15, 3):
    print(i)

print("")
print("FOR ELSE")
#For else
num = [1, 2, 3, 4,5 ]

for n in num:
    if n == 5:
        print("5 was found")
        break
else:
    print("5 was not found")

for i in num:
    if i % i == 0 and i % 1 == 0:
        print(f"{i} is a prime number")
        
else:
    print(f"{i} is not a prime number")




