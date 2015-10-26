#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

# Keurig coffee machine
url = 'http://www.amazon.com/gp/product/B004978NKY/'
url = 'http://www.amazon.com/Brita-Pitcher-Advanced-Replacement-Packaging/dp/B00004SU18/ref=zg_bs_kitchen_1'
r = requests.get(url, headers = { 'User-Agent' : 'Mozilla/5.0' })

#You could now simply parse r.text with somthing like this:
#r.text.split('priceblock_ourprice')[1].split('>')[1].split('<')[0]

# but I prefer using the BeautifulSoup package

soup = BeautifulSoup(r.text)
td_list = soup.findAll('td')
flag = False
debug = True  # Print page if no price is found
for td in td_list:
    if flag:
        try:
            print td.span.text
        except AttributeError:
            print td.text
        flag = False
        debug = False
    #if 'Price:'==td.text:
    if 'List Price:'==td.text:
        flag = True # Print the contents of the next cell too
        print td.text

if debug:
    print(soup.prettify())

