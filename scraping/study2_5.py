#!/usr/bin/python3
# -*- py-python-command: "/usr/bin/python3"; -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")
#for link in bsObj.findAll("a")
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])


