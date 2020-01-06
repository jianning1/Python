# Exercise 5: More Variables and Printing

name = 'Zed A. Shaw'
age = 35
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Embed variables in string using {variables}
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually taht's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#convert inch to cm, lb to kg
height_cm = height * 2.54
weight_kg = weight / 2.2
print(f"He's {height_cm} cm tall.")
print(f"He's {weight_kg} kg heavy.")

#round to 2 decimals
height_cm = round(height * 2.54, 2)
weight_kg = round(weight / 2.2, 2)
print(f"He's {height_cm} cm tall.")
print(f"He's {weight_kg} kg heavy.")
