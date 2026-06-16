import pyjokes
# use: pip install pyjokes
# This prints a random joke
joke = pyjokes.get_joke()
print(joke)



import pyttsx3
engine = pyttsx3.init()
engine.say("Hey I am good")
engine.runAndWait()



import os

# Select the directory whose content you want to list 
directory_path = '/'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)
