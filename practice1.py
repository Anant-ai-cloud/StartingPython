import pyttsx3
import os
# 1 print a poem,multiline print
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
#  ''')

# install random module

# engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("durgesh nai, 20 rs dadi khakhori free")
# engine.runAndWait()

# voices = engine.getProperty("voices")
# for index, voice in enumerate(voices):
#   print(f"Index: {index}")
#   print(f" - ID: {voice.id}")
#   print(f" - Name: {voice.name}")
#   print(f" - Language: {voice.languages}")
#   print(f" - Gender: {voice.gender}\n")

# engine.setProperty("voice", voices[0].id)
# engine.say("Durgesh nai 20rs dadhi, khakhori free")
# engine.runAndWait()

# using os module read directory

# specific directory to list
directory_path = "/StartingPython"

# list all file, and directory
contents = os.listdir(directory_path)

for item in contents:
    print(item)
