import time
from bs4 import BeautifulSoup
import requests

time_taken = {}

with open('cities.html') as html_file:

    # html.parser
    start_time = time.time()
    soup = BeautifulSoup(html_file, "html.parser")
    end_time = time.time()
    time_diff = end_time - start_time
    time_taken["html.parser"] = time_diff

with open('cities.html') as html_file:
    # lxml
    start_time = time.time()
    soup = BeautifulSoup(html_file, "lxml")
    end_time = time.time()
    time_diff = end_time - start_time
    time_taken["lxml"] = time_diff

with open('cities.html') as html_file:
    # html5lib
    start_time = time.time()
    soup = BeautifulSoup(html_file, "html5lib")
    end_time = time.time()
    time_diff = end_time - start_time
    time_taken["html5lib"] = time_diff


for key, val in time_taken.items():
    print("{} {}".format(key, val))


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
