# Exercise 13 Parameters, Unpacking, Variables

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
# unpacks argv to hold all the arguments
# when running this script
# python3.6 ex13.py x y z
# take x as first, y as second, z as third

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

favoriate =input("Your favoriate variable is: ")
print(f"So, among {first}, {second}, and {third}, your favoriate is {favoriate}")

# Difference between argv and input()
# When to give inputs
# input() returns string, to convert to int, use int(input())
