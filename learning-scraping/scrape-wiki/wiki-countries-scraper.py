# A small scraper used to scrape 'member countries of united nations'
# from wikipedia and saves important informations like president,
# population, gdp, etc., in a json file.
# Wiki: 'https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations'

from common import *

import json


project_dirs = {
    'src': 'wiki',
    'html_dir': 'wiki/html',
    'data_dir': 'wiki/data'
}

link_data = {}

create_related_dirs(project_dirs)

clear_screen()

wiki_countries_source = 'https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations'

commonStr = "Extracting countries list from Wikipedia Source: {}".format(
    wiki_countries_source)

print_char_under_string(commonStr, '-')

# fetch data from wiki source
data = fetch_data(project_dirs, wiki_countries_source, 'all-countries.html')

# parse the data to get list of all countries
list_of_all_countries = get_list_of_all_countries(
    project_dirs, 'wiki', data, 'all-countries.json')

for country, values in list_of_all_countries.items():
    print("'{}' Joined on {}, Wiki Source: {}, saved as {}".format(country,
                                                                   values[2],
                                                                   values[1],
                                                                   values[3]))
