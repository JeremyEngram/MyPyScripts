#!/bin/env python3

print("""Welcome to Jeremy's Coffee Shop""")

name = input("What is your name? ") 

if name == "Ben":
    print("You are not welcome here, please leave")
else: 
    print("Hello " + name + ", Thank you for coming in today.")

coffee = input("What kind of coffee would you like? ")

print("Here is your " + coffee)