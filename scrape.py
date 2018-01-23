#!/usr/bin/env python2

import sys
import json
from urllib2 import urlopen
from urlparse import urljoin
from bs4 import BeautifulSoup
import re

email = "[^@]+@[^@]+\.[^@]+"

def GetLinks(initialState, initialUrl):
    url = initialState['urls'][-1]
    htm1= urlopen(url).read()
    soup =BeautifulSoup(htm1, "html5lib")
    json_payload = soup.find_all("script", type="text/data")
    emails = list()
    for element in json_payload:
        payload = json.loads(element.text)
        if 'emails' in payload:
            initialState['emails'].append(payload['emails'])
    a_tags = soup.find_all("a", "c-directory-list-content-item-link")
    urls=list()
    for tag in a_tags:
        x = tag.get('href')
        nextUrl = ''.join([initialUrl, "/", x])
        initialState['urls'].append(nextUrl)
        urls.append(GetLinks(initialState, initialUrl))
    return initialState

initialState = { 'urls': [sys.argv[1]], 'emails': [] }
data = GetLinks(initialState, sys.argv[1])
print data['urls']
