#!/usr/bin/env python3

# importing the neccessary Modules

import requests
import argparse
import json


# parser object to define command line 

parser = argparse.ArgumentParser(description='This script collects information based on the specified IP Address')
parser.add_argument('-ip','--ipAddress', type=str, metavar='[IP address]', default='none', required=True, help='The IP Address you want to learn more about :')

# object that includes data
args=parser.parse_args()

# argument data to identify the IP Address
ipinfoTarget = args.ipAddress

def runQuery(ipinfoTarget):
    ipinfoRequest = f'http://ipinfo.io/{ipinfoTarget}/json'
    jsonResponse = requests.get(ipinfoRequest)
    myDict = json.loads(jsonResponse.text)
    return myDict

# funtion to print and parse  dictionary objects recieved
def printFindings(myDict):
    for key,value in myDict.items():
        print(f'{key}:{value}')

def main():
    myDict = runQuery(ipinfoTarget)
    printFindings(myDict)

if __name__ == '__main__':
    main()
