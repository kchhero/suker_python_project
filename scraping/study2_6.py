#!/usr/bin/python3
# -*- py-python-command: "/usr/bin/python3"; -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getlink(pageUrl) :
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")) :
        if 'href' in link.attrs :
            if link.attrs['href'] not in pages :
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getlink(newPage)

getlink("")

