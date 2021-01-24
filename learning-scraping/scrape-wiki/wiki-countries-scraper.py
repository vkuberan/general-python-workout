# A small scraper used to scrape 'member countries of united nations'
# from wikipedia and saves important informations like president,
# population, gdp, etc., in a json file.
# Wiki: 'https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations'

from common import *
import json
from bs4 import BeautifulSoup
import requests

project_dirs = {
    'src': 'wiki',
    'html_dir': 'wiki/html',
    'data_dir': 'wiki/data'
}

link_data = {}

create_related_dirs(project_dirs)

clear_screen()

link_source = 'https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations'
countries_html = '/'.join([project_dirs['html_dir'], 'all-countries.html'])
countries_data = '/'.join([project_dirs['data_dir'], 'all-countries.json'])

commonStr = "Extracting countries list from Wikipedia Link: {}".format(
    link_source)
print_char_under_string(commonStr, '-')
data = fetch_data(project_dirs, link_source, countries_html)
countries_soup = BeautifulSoup(data)
print(countries_soup.prettify())
