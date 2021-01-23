import os
import platform
import subprocess
from bs4 import BeautifulSoup
import requests


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


def print_char_under_string(msg, char='*', newline='\n\n'):
    msg += "\n" + (char * len(msg))
    print(msg, end=newline)


project_dirs = {
    'src': 'wiki',
    'html_dir': 'wiki/html',
    'data_dir': 'wiki/data'
}

# create 2 separate directories to save html and the scraped data
for dirname, dirpath in project_dirs.items():

    # check weather the dir exists, if not create new one
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

clear_screen()
commonStr = "Extracting 'Member states of the United Nations's' general information from Wikipedia"
print_char_under_string(commonStr)

link_source = 'https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations'
html_file = '/'.join([project_dirs['html_dir'], 'all-countries.html'])
data_file = '/'.join([project_dirs['data_dir'], 'all-countries.json'])

commonStr = "Wikipedia Link: {}, Files: [HTML: {}, Data: {}]".format(
    link_source, html_file, data_file)
print_char_under_string(commonStr, '-')

try:
    with open(html_file, 'rb') as hs:
        html_source = hs.read().decode("UTF-8")
        print_char_under_string(
            "Fetching info from the crawled file.", '-', '\n')
        soup = BeautifulSoup(html_source, 'lxml')
        # print(soup.prettify())
except:
    print_char_under_string(
        "Fetching data from the server using request.", '-', '\n')
    res = requests.get(link_source)
    soup = BeautifulSoup(res.text, 'lxml')
    f = open(html_file, mode='w', encoding='UTF-8')
    f.write(res.text)
    f.close()

countries = soup.find('table', class_='wikitable').find("tbody").find_all("tr")
coutries_data = {}

for country in countries:

    if country.find("td"):
        country_info = country.find_all("td")
