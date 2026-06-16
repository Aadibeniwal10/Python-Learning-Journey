# Loops
for i in range(1, 6):
    print(i)

----

# While Loops
i = 1
while(i<51):
    print(i)
    i += 1 # or i = i + 1
  
l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]
i = 0
while(i<len(l)):
    print(l[i])
    i += 1

----

# For Loops
for i in range(4): # same as (0,4)
    print(i)

for i in range(0,100,4): # (start,stop,step_size)
  print(i)

## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Harry"
for i in s:
    print(i)

## For loop with else
l= [1,7,8] 
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exhausts!

## For loop break and continue 
for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)  

## For loop with pass
for i in range(645):
    pass # skips this loop

i = 0
while(i<45):
    print(i)
    i += 1

----

# Problems
##!
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}") # multiplication table
##2
n = int(input("Enter a number: "))
for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
##3
n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1
print(sum) # sum of first n natural numbers
##4
n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i
print(f"The factorial of {n} is {product}")
##5
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")
##6
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")
