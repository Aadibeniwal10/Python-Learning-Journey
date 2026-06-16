import pyjokes
# use: pip install pyjokes
# This prints a random joke
joke = pyjokes.get_joke()
print(joke)




import pyttsx3
engine = pyttsx3.init()
engine.say("Hey I am good")
engine.runAndWait()
