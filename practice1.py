# import pyttsx3
# import os
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
# directory_path = "/StartingPython"

# # list all file, and directory
# contents = os.listdir(directory_path)

# for item in contents:
#     print(item)

# with input function checking number is greater

# a = int(input("Enter the number 1: "))
# b = int(input("Enter the number 2: "))
# print("a is greater that b is: ", a>b)

# average of the numbers is
# a = int(input("Enter the number 1: "))
# b = int(input("Enter the number 2: "))
# print("Average of both the number is: ", (a+b)/2)

# square of the number
# a = int(input("Enter the number: "))
# print("Square of the number is: ", a**2)

# f string

# name = input("Enter your name: ")
# print(f"Good morning {name}")

# chainig of .replace

# letter = '''
#          Dear <|Name|>
#          you are selected <|Date|>
#          '''
# print(letter.replace("<|Name|>", "Anant").replace("<|Date|>", "19 june"))

# name = "Anant is going to market"
# print(name.find(" "))
