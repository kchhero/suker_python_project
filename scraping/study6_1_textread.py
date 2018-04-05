from urllib.request import urlopen
textpage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(textpage.read(), 'utf-8')

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# bsObj = BeautifulSoup(html, "html.parser")
# content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
# content = bytes(content, 'UTF-8')
# content = content.decode('UTR-8')
