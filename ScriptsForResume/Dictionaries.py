#!/usr/bin/env python3

#################################
# Using FDQN' and IP Addresses
# to practice with Dictionaries
#
###############################
#
#Example= myDictionay = {'Key1':'Value`} 
#
##############################
# Creating A Dictionary With FQDN's and their IP Addresses 
#############################


FDQN = {
    'server1.testlab.com':'192.168.1.10',
    'server2.testlab.com':'192.168.1.11',
    'server3.testlab.com':'192.168.1.12',
    'server4.testlab.com':'192.168.1.13',
    'server5.testlab.com':'192.168.1.14',
    'server6.testlab.com':'192.168.1.15',
    'server7.testlab.com':'192.168.1.16',
    'server8.testlab.com':'192.168.1.17',
}
##############################
# Listing all of the FQDN 's (keys)
#############################

print("\n")
print(FDQN.keys())


#############################
#
# Listing all of the IP Addresses (values)
#
#############################

print("\n")
print(FDQN.values())

##############################
#
# Listing all of the items in  Dictionary (key/value)
#
##############################

print("\n")
print(FDQN.items())

############################
#
# checkng to see if a specific key pair is in the dictionary
#
###########################

print("\n")
print(f"The IP Address accociated with server2.testlab.com is :",FDQN["server2.testlab.com"])


################################
#
# Checking to see if server 10 (non-existant) is in the dictionary
#
####################################

print("\n")
print('server10.testlab.com' in FDQN)

####################################

print(f"\n",'This is the end of the Script')
