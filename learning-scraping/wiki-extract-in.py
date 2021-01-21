from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

# administrative states:
# url = 'https://en.wikipedia.org/wiki/Administrative_divisions_of_India'

url = 'https://en.wikipedia.org/wiki/India'
html_file = 'india.html'
data_file = 'india.json'

try:
    with open(html_file, 'rb') as html_source:
        print("Fetching info from the crawled file.")
        soup = BeautifulSoup(html_source, 'lxml')
except:
    print("Fetching data from the server using request.")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    f = open(html_file, "wb+")
    f.write(res.text.encode('utf8'))
    f.close()

print(soup.title.text)

# find the capital
capital = soup.find_all("th", string="Capital")
print(capital)
