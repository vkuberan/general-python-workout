from common import *
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
base_wiki_url = 'https://en.wikipedia.org/'
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

    link_source = properties[0]
    html_file = '/'.join([project_dirs['html_dir'], properties[1]])
    data_file = '/'.join([project_dirs['data_dir'], properties[2]])

    commonStr = "Wikipedia Link: {}, Files: [HTML: {}, Data: {}]".format(
        link_source, html_file, data_file)
    print_char_under_string(commonStr, '-')

    input("\nPress any key to continue...")
    clear_screen()
