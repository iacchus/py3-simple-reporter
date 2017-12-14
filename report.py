#!/usr/bin/env python3

# https://stackoverflow.com/questions/8692/how-to-use-xpath-in-python

import requests
from lxml.html import fromstring

TITLE_XPATH = "//title"

targets = []

with open('targets.txt', 'r') as targets_file:
    targets = targets_file.readlines()

for target in targets:
    current = target.strip().split(' ')
    
    if len(current) == 2:
        url, xpath = current

        query = requests.get(url)
        root = fromstring(query.content)
        content = root.xpath(xpath)
        
        title = root.xpath(TITLE_XPATH)[0].text
        number_of_elements = len(content)
        
        print("{} ({})".format(title, number_of_elements))
        for element in content:
            print(element.text)
