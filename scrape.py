#!/usr/bin/env python3


from bs4 import BeautifulSoup

        # url = input("Enter url:")

import requests
page = requests.get("https://www.cnn.com/")
page

page.status_code

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#soup = BeautifulSoup(html)
#text = soup.get_text()
#print(text)

#print(soup)
print(soup.prettify())