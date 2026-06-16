# Positive Slicing
name = "Harry"
nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)

----

# Negative Slicing
name = "Harry"
print(name[0:3])
print(name[-4: -1])
print(name[1:4])
print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

----

# Functions
name = "harry"
print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))
print(name.capitalize())

a = 'Harry is a good boy\nbut not a bad \'boy\''
print(a)

name = input("Enter your name: ")
print(f"good afternoon, {name}")

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
print(letter.replace("<|Name|>", "Harry").replace("<|Date|", "24 September 2050"))

name = "Harry is a good  boy and  "
print(name.find("  "))

name = "Harry is a good  boy and  "
print(name.replace("  ", " "))
print(name) # Strings are immutable which means that you cannot change them by running functions on them

letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(letter)
