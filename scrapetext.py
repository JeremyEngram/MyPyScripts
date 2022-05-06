#!/usr/bin/env python3

from bs4 import BeautifulSoup

        # url = input("Enter url:")
#val = input("Enter your value: ")

import requests
page = requests.get("https://stackoverflow.com/questions/16206380/python-beautifulsoup-how-to-remove-all-tags-from-an-element")
page

page.status_code

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


#soup = BeautifulSoup(html)
text = soup.get_text()
print(text)

#print(soup)
