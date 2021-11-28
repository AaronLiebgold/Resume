#!/usr/bin/env python3
import requests

# using requests.get() to copy the HTLM of the response URL
response = requests.get("http://www.notpurple.com")

# saving/writing the HTLM to a new file called store page here as shown 
with open("store_page_here.htlm",'w') as hFile:
    hFile.write(response.text)

print("File saved successfully!")
