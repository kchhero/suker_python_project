#!/usr/bin/python3
# -*- py-python-command: "/usr/bin/python3"; -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl) :
    internallinks = []
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")) :
        if link.attrs['href'] is not None :
            if link.attrs['href'] not in internallinks :
                internallinks.append(link.attrs['href'])

    return internallinks

def getExternalLinks(bsObj, excludeUrl):
    externallinks = []
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None :
            if link.attrs['href'] not in externallinks :
                externallinks.append(link.attrs['href'])
    return externallinks

def splitAddress(address) :
    addressParts = address.replace("http://", "").split("/")
    return addressParts
                                                   
def getRandomExternalLink(startingPage) :
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externallinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externallinks) == 0:
        internallinks = getInternalLinks(startingPage)
        ### book --> getNextExternalLink
        return getExternalLinks(internallinks[random.randint(0,
                                                len(internallinks)-1)])
    else :
        return externallinks[random.randint(0, len(externallinks)-1)]

def followExternalOnly(startingSite) :
    externallink = getRandomExternalLink("http://oreilly.com")
    print("Random external link is : "+externallink)
    followExternalOnly(externallink)

followExternalOnly("http://oreilly.com")
