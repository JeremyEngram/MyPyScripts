#!/usr/bin/env python3
from signal import pause

#PYTHON DINNER ROULETTE

import random
import pyfiglet


# This is my first python script

print("""DINNER ROULETTE IS A BASIC PYTHON SCRIPT THAT GATHERS A LIST OF WHAT I LIKE TO EAT IN AN ARRAY.
THE END GOAL IS TO DESIGN A DYNAMIC PYTHON PROGRAM THAT WILL TAKE USER INPUT AS CONTENTS FROM FRIDGE
AND MAKE RECOMMENDATIONS ON WHAT TO HAVE FOR DINNER BASED ON THE PRIMARY RECOMMENDATION AND CONTENTS OF FRIDGEjER.""")

ascii_banner = pyfiglet.figlet_format("DINNER ROULETTE")
print(ascii_banner)

user_name = input("Enter your name: ")
print("Hello", user_name + " Here is an idea for dinner tonight!\n")

#Random Dinner Suggestion Generator with Python random module
myfoods = ["Pizza", "Grilled-Cheese Provolone" "French-Bread Pizza", "White Pizza", "Meatball Sub", "Home-Made Italian Sub", "Spaghetti", "Steak", "Eggs & Bacon For Dinner", "Whaffles For Dinner", "Frechtoast For Dinner", "Hamburgers", "BBQ Ribbs", "BBQ Chicken", "Lemon Chicken", "Fried Chicken", "Orange Chicken", "Chavettas Chicken", "Breaded Chicken" ]

print( "Dinner Roulette Says: " + random.choice(myfoods))

quit()