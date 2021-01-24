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
countries_data = '/'.join([project_dirs['data_dir'], 'all-countries.json'])

commonStr = "Extracting countries list from Wikipedia Source: {}".format(
    wiki_countries_source)
print_char_under_string(commonStr, '-')

# fetch data from wiki source
data = fetch_data(project_dirs, wiki_countries_source, 'all-countries.html')

# parse the data to get list of all countries
list_of_all_countries = get_list_of_all_countries(
    project_dirs, 'wiki', data, 'all-countries.json')

countries_soup = BeautifulSoup(data, "lxml")
print(countries_soup.title.text)
