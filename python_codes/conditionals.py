a = int(input("Enter your age: "))
# If else statement
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")
else:
    print("You are below the age of consent")
print("End of Program")

----

a = int(input("Enter your age: "))
# If elif else ladder
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0):
    print("You are entering an invalid negative age")
elif(a==0):
    print("You are entering 0 which is not a valid age")    
else:
    print("You are below the age of consent")
print("End of Program")

----

# Multiple if Statements
a = int(input("Enter your age: "))
if(a%2 == 0):
    print("a is even")
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0):
    print("You are entering an invalid negative age")  
else:
    print("You are below the age of consent")
print("End of Program")

----

# in keyword
p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"
message = input("Enter your comment: ")
if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")

----

# Problems
marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))
total_percentage = (100*(marks1 + marks2 + marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", total_percentage)
else:
    print("You failed, try again next year:", total_percentage)


post = input("Enter the post: ")
if("harry" in post.lower()):
    print("This post is talking about harry")
else:
    print("This post is not talking about harry")


marks = int(input("Enter your marks: "))
if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"
print("Your grade is:", grade)
