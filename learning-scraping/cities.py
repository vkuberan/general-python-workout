from bs4 import BeautifulSoup
import requests

with open('cities.html') as html_file:
    soup = BeautifulSoup(html_file, "lxml")

# print(soup.prettify())

title = soup.title
title_text = soup.title.text
articles = soup.find_all('article')

print(title)
print(title_text)
print(articles)
