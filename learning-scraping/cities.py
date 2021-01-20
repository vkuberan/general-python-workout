from bs4 import BeautifulSoup
import requests

with open('cities.html') as html_file:
    soup = BeautifulSoup(html_file, "lxml")

title = soup.title
title_text = soup.title.text


print(title_text)
print("*" * len(title_text))
print()

for article in soup.find_all('article'):
    headline = article.h1.text
    summary = article.find("div", class_="summary").text
    print(headline)
    print(summary)
    print("\n")
