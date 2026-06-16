# Functions
def avg(): # you can keep any name of function
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    
    average = (a + b + c)/3
    print(average) # till this, whole is iside avg(), known as function definition

avg() # Function Call
print("Thank you!")
avg()

----

# Functins with arguments
def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
goodDay("Aditya, Thanks")

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"
a = goodDay("Harry", "Thank you") 
print(a)

## Default Argument
def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Harry", "Thanks")
goodDay("Rohan")

----

# Recursion
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

----

# Problems
##1
def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C") # round off number to 2 decimal places
##2
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4)) # Recursive Relation
##3
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
pattern(3) # Recursive Relation
##4
def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))
