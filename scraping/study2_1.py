#!/usr/bin/python3
# -*- py-python-command: "/usr/bin/python3"; -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())


