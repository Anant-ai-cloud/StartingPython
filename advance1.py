# walrus operator

# if(n:=len([1, 2, 3, 4]))>5:
#     print("List is too long")
# else:
#     print("List is okay")

# type definations

# age:int = 25

# def rahul (a:int, b:int)-> int:
#     c= a+b
#     return c

# print(rahul(2, 4))

# from typing import List, Tuple, Dict, Union

# numbers: List[int] = [1, 2, 3, 4] # list of int
# numbers: Tuple[str, int] = [1, 2, 3, 4] # tuple of string and 

# scores: Dict[str, int] = {"Anant": 20, "Vinit": 40}

# # Union are variables that can hold multiple types

# identifier: Union[str, int] = "Id2383"
# identifier = 1245

# match case similar to switch

# def status(num):
#     match num:
#         case 200:
#             return "Its 200"
#         case 300:
#             return "its 300"
#         case _:
#             return "unknown num"

# print(status(2000))

# merge dictonary

# dict1 = {"a": 1, "b": 2}
# dict2 = {"a": 4, "c": 3}
# print(dict1 | dict2)

# multiple files can be open in one go using with

# with (
#     open(first.py) as f1,
#     open(tuple.py) as f2
# ):

# exception handling

# try: 
#     a = int(input("Enter a number: "))
#     print(a)

# except ValueError as v: # exception for particular type of error
#     print("Number to sahi type karo")

# except Exception as e :
#     print(e)

# print(" Thank You! ")

# raise custom error

# a = int(input("Enter the first number: "))
# b= int(input("Enter the second number: "))
# if (b==0):
#     raise ZeroDivisionError("Hey you are not allowed to divide by zero kya kr rahe ho")
# else:
#     print(f"The result is {a/b}")

# try except and else

# try:

#     b= int(input("Enter the second number: "))

# except Exception as e :
#     print(e)

# else:
#   print("Successfull")

# from creator import func

# a= 89

# def fun():
#     global a # change the global variable
#     a= 3
#     print(a)

# fun()
# print(a)

# l = [34, 56, 104, 56]

# index = 0
# for item in l:
#     print(f"{index}: {item}")
#     index += 1

#using enumerator

# for  sitem in enumerate(l):
#     print(f"{sitem}")

# list comprehension

# l = [2, 3, 4, 5]

# squared = [i*i for i in l]
# print(squared)