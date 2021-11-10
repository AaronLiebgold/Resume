#!/usr/bin/env python3 
######################
print("\n")
varString=("Here is a nice string to slice")
print (varString)
print("\n")
######################

varList=["Here","is","a","nice","list","to","slice"]
print (varList)
print("\n")

#####################
#Slicing varString

print(varString[3::])
print("\n")
print(varString[:3:])
print("\n")
print(varString[0::2])
print("\n")
print(varString[::-1])
print("\n")

########################
#Slicing varList
print(varList[::-1])
print("\n")
print(varList[2::-1])
print("\n")
print(varList[2:4:])
print("\n")
print(varList[0::3])
print("\n")
print(varList[1::])
print("\n")
##########################
# Using a for loop print out each element of  varString print out one line at a time 
#########################
for element in varString:
    print(f"{element}")
##########################
#using a for loop print out each element of varList  one line at a time
##########################
print("\n")
for element in varList:
    print(f"{element}")
