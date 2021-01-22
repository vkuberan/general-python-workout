import os
import platform
import subprocess
from bs4 import BeautifulSoup
import requests


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


project_dirs = {
    'html_dir': 'html',
    'data_dir': 'data'
}

# create 2 separate directories to save html and the scraped data
for dirname, dirpath in project_dirs.items():

    # check weather the dir exists, if not create new one
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


wiki_countries_entry = {
    'India': ['https://en.wikipedia.org/wiki/India', 'india.html', 'india.json'],
    'United States': ['https://en.wikipedia.org/wiki/India', 'us.html', 'us.json'],
    'China': ['https://en.wikipedia.org/wiki/India', ' china.html', 'china.json'],
    'United Kingdom': ['https://en.wikipedia.org/wiki/India', 'uk.html', 'uk.json'],
    'France': ['https://en.wikipedia.org/wiki/India', 'france.html', 'france.json'],
    'Germany': ['https://en.wikipedia.org/wiki/India', 'germany.html', 'germany.json'],
}

for country, properties in wiki_countries_entry.items():
    commonStr = "Extracting {}'s general information from Wikipedia".format(
        country)
    print(commonStr)
    print('*' * len(commonStr))
