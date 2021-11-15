#!/usr/bin/env python3

print("\n")
print("Name:Aaron Liebgold")
print("\n")

hFile=open("Midterm-if.txt","r")
strFiletxt=hFile.read()
print(strFiletxt)

print("\n")
print(f"The length of the file is {len(strFiletxt)} bytes long")
print("\n")

magicWords=("parnall")

if magicWords == strFiletxt :
	print(line)
#print("wasnt successfull with this part of the midterm at all ")
