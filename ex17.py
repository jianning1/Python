# Exercise 17 More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#out_file = open(to_file, 'w')
#out_file.write(indata)
open(to_file, 'w').write(indata)

print("Alright, all done.")

#out_file.close()
#in_file.close()
# Why you had to write out_file.clsoe() in the code? To end writing.
# Below is from https://www.tutorialspoint.com/python3/python_files_io.htm
# The close() method of a file object flushes any unwritten information and closes the file object, after which no more writing can be done.
# Python automatically closes a file when the reference object of a file is reassigned to another file. It is a good practice to use the close() method to close a file.
