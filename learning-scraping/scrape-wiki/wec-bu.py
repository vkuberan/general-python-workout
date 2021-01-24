from common import *
import time
import json
from bs4 import BeautifulSoup
import requests


project_dirs = {
    'src': 'wiki',
    'html_dir': 'wiki/html',
    'data_dir': 'wiki/data'
}

create_related_dirs(project_dirs)

data_dir = 'wiki/data/all-countries.json'
base_wiki_url = 'https://en.wikipedia.org'
wiki_countries_entry = {}

with open(data_dir, 'r') as fp:
    wiki_countries_entry = json.load(fp)

i = 0

for entry, country_info in wiki_countries_entry.items():

    country_data = {}

    clear_screen()
    commonStr = "Extracting {}'s general information from Wikipedia".format(
        entry)
    print_char_under_string(commonStr)

    link_source = ''.join([base_wiki_url, country_info[1]])
    html_file = '/'.join([project_dirs['html_dir'], country_info[3]])
    data_file = '/'.join([project_dirs['data_dir'], country_info[4]])

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
        time.sleep(3)

    print(soup.title.text)

    # input("\nPress any key to continue...")
    clear_screen()
