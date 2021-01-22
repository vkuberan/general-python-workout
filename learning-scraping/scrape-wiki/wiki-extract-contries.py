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
    'United States': ['https://en.wikipedia.org/wiki/United_States', 'us.html', 'us.json'],
    'China': ['https://en.wikipedia.org/wiki/China', ' china.html', 'china.json'],
    'United Kingdom': ['https://en.wikipedia.org/wiki/United_Kingdom', 'uk.html', 'uk.json'],
    'France': ['https://en.wikipedia.org/wiki/France', 'france.html', 'france.json'],
    'Germany': ['https://en.wikipedia.org/wiki/Germany', 'germany.html', 'germany.json'],
}

for country, properties in wiki_countries_entry.items():
    clear_screen()
    commonStr = "Extracting {}'s general information from Wikipedia".format(
        country)
    print(commonStr)
    print('*' * len(commonStr))

    link_source = properties[0]
    html_file = '/'.join([project_dirs['html_dir'], properties[1]])
    data_file = '/'.join([project_dirs['data_dir'], properties[2]])

    print("Wikipedia Link: {}, Files: [HTML: {}, Data: {}]".format(
        link_source, html_file, data_file))

    try:
        with open(html_file, 'rb') as html_source:
            print("Fetching info from the crawled file.")
            soup = BeautifulSoup(html_source, 'lxml')
    except:
        print("Fetching data from the server using request.")
        res = requests.get(link_source)
        soup = BeautifulSoup(res.text, 'lxml')
        f = open(html_file, "wb+")
        f.write(res.text.encode('utf8'))
        f.close()

    details = soup.find('table', class_='infobox geography vcard').find(
        "tbody").find_all("tr")

    print(details[0])
    details = []

    i = 0
    data = {}
    for detail in details:
        # we are going to get the details
        lftData = detail.find("th")

        if lftData:
            if i == 0:
                print(lftData.find('div'))
            # else:
            #     print(lftData.get_text())

        i += 1

    input("\nPress any key to continue...")
    clear_screen()
