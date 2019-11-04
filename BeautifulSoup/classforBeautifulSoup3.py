import requests

from bs4 import BeautifulSoup

webpage = requests.get('https://www.webscraper.io/test-sites/e-commerce/static')

content = webpage.content
result = BeautifulSoup(content,'html.parser')

head = result.head
print(head)
h2 = result.h2
print(h2)
title = result.title
print(title)
title.name = 'mytitle'
print(title)

header = result.header
print(header.prettify())

print(header.attrs)
print(header['role'])
print(header['class'])
print(header.get('role'))
print(header.get('class'))

header['role'] = 'something'
print(header.attrs)

header['new'] = 'python'
print(header.attrs)

del header['new']
print(header.attrs)

print(h2)
print(h2.string)

print(result.header.div.div.a.button)
print(result.header.button)
print(result.header.span)

print(result.find('div'))
print(result.find('div').prettify())

print(result.find_all('h1'))
print(len(result.find_all('h1')))

products = result.find_all("div",{"class":"col-sm-4 col-lg-4 col-md-4"})
print(len(products))