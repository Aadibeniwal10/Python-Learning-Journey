# Make a File
f = open("file.txt", "r") # You can skip "r"
data = f.read()
print(data)
f.close() # Do it everytime

# How to write in a File?
st = "Hey Harry you are amazing"
f = open("myfile.txt", "w") # This made a file named myfile.txt
f.write(st)
f.close()

# Files Functions
f = open("file.txt")
## lines = f.readlines() ## Reads all lines
## print(lines, type(lines)) ## Lines are of lists types 

## line1 = f.readline() ## Reads only one line 
## print(line1, type(line1))

## line2 = f.readline()
## print(line2, type(line2))

## line3 = f.readline()
## print(line3, type(line3))

## line4 = f.readline()
## print(line4, type(line4))

## line5 = f.readline()
## print(line5 =="")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()
## Append
st = "Hey Harry you are amazing"
f = open("myfile.txt", "a")
f.write(st) ## This writes strings in main Files not in output
f.close()

# With Statement
f = open("file.txt")
print(f.read())
f.close()
## The same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())
## You dont have to explicitly close the file

----

# Problems
## 1
import random
def game(): 
    print("You are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score
game()
## 2
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"    
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)
for i in range(2, 21):
    generateTable(i)
## 3
words = ["Donkey", "bad", "ganda"]
with open("file.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))
with open("file.txt", "w") as f:
    f.write(content)
## 4
with open("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No Python is not present")
## 5
with open("this_copy.txt", "w") as f:
    f.write("") ## To clear all content of a file
## 6
with open("old.txt") as f:
    content = f.read()
with open("renamed_by_python.txt", "w") as f:
    f.write(content)
