from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}\nThe input file is {len(indata)} bytes long\nReady, hit RETURN to continue, CTRL-C to abort.")
input()

open(to_file, 'w').write(open(from_file.read()))

print("Alright, all done.")
