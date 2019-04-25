#!/home/suker/.pyenv/versions/2.7.15/bin/python
from urllib.request import urlopen
from bs4 import BeautifulSoup

myURL = "http://dart.fss.or.kr/dsac001/mainY.do"
# textpage = urlopen(myURL)
# print(textpage.read(), 'utf-8')

html = urlopen(myURL)
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id" : "mw-content-text"}).get_text()
content = bytes(content, 'UTF-8')
content = content.decode('UTR-8')
