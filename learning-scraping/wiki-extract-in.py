from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

# Important Url
# https://www.thinkingondata.com/web-scraping-wikipedia-using-beautiful-soup/
# https://www.geeksforgeeks.org/web-scraping-using-lxml-and-xpath-in-python/?ref=rp
# https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722
# https://www.oreilly.com/library/view/web-scraping-with/9781491910283/ch01.html
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree

# Iterate over the table: https://stackoverflow.com/questions/10309550/python-beautifulsoup-iterate-over-table
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

details = soup.find('table', class_='infobox geography vcard').find(
    "tbody").find_all("tr")

for detail in details:
    # we are going to get the details
    lftData = detail.find("th")

    if lftData:
        print(lftData.get_text())

# find the capital
# capital = soup.find_all("th", string="Capital")

# print(capital)
