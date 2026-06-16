a = 1
b = 2
print(a + b)

----

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))

----

a = "31.2"
b = float(a) # a but the type should be float
t = type(b) 
print(t)

----

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)

----

a = 37
b = 5
print("Remainder when a is divided by b is", a % b)

----

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("The average of these two number is", (a+b)/2)

----

a = int(input("Enter your number: ")) 
print("The square of the number is", a**2)
print("The square of the number is", a*a)
# print("The square of the number is", a^2) # Incorrect for finding square of a number in Python
