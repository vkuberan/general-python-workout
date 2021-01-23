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


wiki_countries_entry = {
    'India': ['https://en.wikipedia.org/wiki/India', 'india.html', 'india.json'],
    'United States': ['https://en.wikipedia.org/wiki/United_States', 'us.html', 'us.json'],
    'China': ['https://en.wikipedia.org/wiki/China', ' china.html', 'china.json'],
    'United Kingdom': ['https://en.wikipedia.org/wiki/United_Kingdom', 'uk.html', 'uk.json'],
    'France': ['https://en.wikipedia.org/wiki/France', 'france.html', 'france.json'],
    'Germany': ['https://en.wikipedia.org/wiki/Germany', 'germany.html', 'germany.json'],
}

for country, properties in wiki_countries_entry.items():

    data = {}

    clear_screen()
    commonStr = "Extracting {}'s general information from Wikipedia".format(
        country)
    print_char_under_string(commonStr)

    link_source = properties[0]
    html_file = '/'.join([project_dirs['html_dir'], properties[1]])
    data_file = '/'.join([project_dirs['data_dir'], properties[2]])

    commonStr = "Wikipedia Link: {}, Files: [HTML: {}, Data: {}]".format(
        link_source, html_file, data_file)
    print_char_under_string(commonStr, '-')

    try:
        with open(html_file, 'rb') as html_source:
            print_char_under_string(
                "Fetching info from the crawled file.", '-', '\n')
            soup = BeautifulSoup(html_source, 'lxml')
    except:
        print_char_under_string(
            "Fetching data from the server using request.", '-', '\n')
        res = requests.get(link_source)
        soup = BeautifulSoup(res.text, 'lxml')
        f = open(html_file, "wb+")
        f.write(res.text.encode('utf16'))
        f.close()

    details = soup.find('table', class_='infobox geography vcard').find(
        "tbody").find_all("tr")

    for detail in details:
        # we are going to get the details
        lftData = detail.find("th")
        rgtData = detail.find("td")

        if (lftData != None and rgtData != None):
            print("Both Contains data on both side")
        else:
            if lftData:
                print(lftData)

    input("\nPress any key to continue...")
    clear_screen()
