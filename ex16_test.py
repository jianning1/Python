from sys import argv

script, filename = argv

test = open(filename)

print(f"Here is your new {filename}:")
print(test.read())
