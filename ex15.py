# Exercise 15 Reading Files

from sys import argv

script, filename = argv

txt = open(filename) # open the file and put the file object to txt

print(f"Here's your file {filename}:")
print(txt.read())  # read function on txt

txt.close()

print("Type the filename again:")
file_again = input("> ") # type in the file name again

txt_again = open(file_again) # open the file again and put it to txt_again
# A file can be opened more than once in Python

print(txt_again.read()) # read function on txt_again

txt_again.close()

# To open and print txt files in python3.6 shell
# python3.6
# filename = "ex15_sample.txt"
# txt = open(filename)
# print(txt.read())
