from bs4 import BeautifulSoup
import requests

url_name = 'https://coreyms.com/'
file_name = 'coreyms.html'

try:
    with open(file_name) as html_source:
        print("Fetching info from the crawled file.")
        soup = BeautifulSoup(html_source, "lxml")
except:
    print("Fetching data from the URL using requests.")
    html_source = requests.get(url_name)
    f = open(file_name, 'w')
    f.write(html_source.text)
    f.close
    soup = BeautifulSoup(html_source.text, "lxml")

title = soup.title.text
print(title)
print("*" * len(title))
print("")
