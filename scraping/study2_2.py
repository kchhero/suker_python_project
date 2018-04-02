#!/usr/bin/python3
# -*- py-python-command: "/usr/bin/python3"; -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll(text="the prince")
#find  는 limit 가 1 로 고정되어있는것과 같음.
#findall recursive True 가 default 임.
allText = bsObj.findAll(id="text")

print(len(nameList))
print(allText)
#print(allText[0])
#print(allText[0].get_text()
