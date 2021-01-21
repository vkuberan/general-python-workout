from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

url = 'https://coreyms.com/'
file_name = 'index.html'

parse_url = urlparse(url)

try:
    with open(file_name) as html_source:
        print("Fetching info from the crawled file.")
        soup = BeautifulSoup(html_source, "lxml")
except:
    print("Fetching data from the URL using requests.")
    html_source = requests.get(url)
    f = open(file_name, "w+")
    f.write(html_source.text)
    f.close
    soup = BeautifulSoup(html_source.text, "lxml")

title = soup.title.text
print(title)
print("*" * len(title))
print("")
