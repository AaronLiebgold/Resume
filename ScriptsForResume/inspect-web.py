#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = "https://www.notpurple.com"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll('a')

for link in links:
    print(link.get("href"))
print(soup.title)
