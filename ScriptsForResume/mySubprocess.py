#!/usr/bin/env python3

import subprocess


#part 1

myproc = subprocess.run(["ps", "-axco", "command"],stdout=subprocess.PIPE)
print(myproc)

#part 2

myprocstring = myproc.stdout.decode().split("\n")
print(myprocstring)

#step 3

print(myprocstring [8::])

print("\n")

for line in myprocstring:
    print(line)

print(f"There are {len(myprocstring[2::])} Processes in the file")
