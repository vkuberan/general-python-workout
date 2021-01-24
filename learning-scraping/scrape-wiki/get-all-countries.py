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
        html_source = hs.read().decode("UTF-16")
        print_char_under_string(
            "Fetching info from the crawled file.", '-', '\n')
        soup = BeautifulSoup(html_source, 'lxml')
        # print(soup.prettify())
except:
    print_char_under_string(
        "Fetching data from the server using request.", '-', '\n')
    res = requests.get(link_source)
    soup = BeautifulSoup(res.text, 'lxml')
    f = open(html_file, mode='w', encoding='UTF-16')
    f.write(res.text)
    f.close()

countries = soup.find('table', class_='wikitable').find("tbody").find_all("tr")
coutries_data = {}

for country in countries:

    if country.find("td"):
        country_info = country.find_all("td")
        country_name = country_info[0].get_text(separator=', ', strip=True)

        if (', ' in country_name):
            print(country_name)
            country_name = country_name.split(",")[0]
            print(country_name)
            input("Press any key....\n\n\n")

        country_name_tag = country_name.replace(
            "'", '-').replace(' ', '-').lower()

        country_link = country_info[0].find('a').get('href')
        date_joined = country_info[1].get_text(strip=True)
        a_html_file = country_name_tag + ".html"
        a_data_file = country_name_tag + ".json"
        print("{}] ({}) ({}) {}".format(country_name,
                                        country_name_tag, country_link, date_joined))

        link_data[country_name] = [country_name_tag,
                                   country_link, date_joined, a_html_file, a_data_file]

with open(data_file, 'w') as fp:
    json.dump(link_data, fp)
