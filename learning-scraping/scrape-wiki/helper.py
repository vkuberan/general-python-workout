import os
import platform
import subprocess
import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from WikiParserHelper import *

# seconds
DEFAULT_TIMEOUT = 5
retry_strategy = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],  # http://httpstat.us/
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)


# To set default timeout parameter for our scrapper
class WikiTimeOutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]

        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout

        return super().send(request, **kwargs)


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


def print_char_under_string(msg, char='*', newline='\n\n'):
    msg += "\n" + (char * len(msg))
    print(msg, end=newline)


def create_related_dirs(project_dirs):
    # create 2 separate directories to save html and the scraped data
    for dirname, dirpath in project_dirs.items():
        # check weather the dir exists, if not create new one
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)


def fetch_data(project_dirs, link_source, html_file):
    html_file = '/'.join([project_dirs['html_dir'], html_file])
    html_source = ''
    try:
        with open(html_file, 'rb') as hs:
            html_source = hs.read().decode("UTF-16")
            print_char_under_string(
                "Fetching info from the crawled file.", '-', '\n')
    except Exception as e:
        errno, errmsg = e.args
        errmsg = 'Error: ' + errmsg + \
            ". Creating new file {}.".format(html_file)
        print_char_under_string(errmsg, '*', '\n\n')
        print_char_under_string(
            "Fetching data from the server using request.", '-', '\n')

        try:
            adapter = WikiTimeOutHTTPAdapter(
                max_retries=retry_strategy, timeout=5)
            http = requests.Session()
            http.mount("https://", adapter)
            http.mount("http://", adapter)

            response = http.get(link_source)
            # print(response.headers)

            html_source = response.text
            with open(html_file, mode='w', encoding='UTF-16') as f:
                f.write(response.text)

        except Exception as e:
            print(e)

    return html_source


# parse strategy is based on the source.
def get_list_of_all_countries(project_dirs, source, data, data_file):
    data_file = '/'.join([project_dirs['data_dir'], data_file])
    soup = BeautifulSoup(data, "lxml")
    countries_data = {}

    if source == 'wiki':
        countries = soup.find('table', class_='wikitable').find(
            "tbody").find_all("tr")

        for country in countries:

            if country.find("td"):
                country_info = country.find_all("td")
                country_name = country_info[0].get_text(
                    separator=', ', strip=True)

                if (', ' in country_name):
                    # print(country_name)
                    country_name = country_name.split(",")[0]
                    # print(country_name)
                    # input("Press any key....\n\n\n")

                country_name_tag = country_name.replace(
                    "'", '-').replace(' ', '-').lower()

                country_link = country_info[0].find('a').get('href')
                date_joined = country_info[1].get_text(strip=True)
                a_html_file = country_name_tag + ".html"
                a_data_file = country_name_tag + ".json"

                countries_data[country_name] = [country_name_tag, country_link,
                                                date_joined, a_html_file,
                                                a_data_file]

        with open(data_file, 'w') as fp:
            json.dump(countries_data, fp)

    return countries_data


# get individual countries details
def get_country_details(project_dirs, source, data, data_file):
    data_file = '/'.join([project_dirs['data_dir'], data_file])
    soup = BeautifulSoup(data, "lxml")

    country_data = {}
    culprit_found = False
    if source == 'wiki':
        details = soup.find('table', class_='infobox geography vcard').find(
            "tbody").find_all("tr")
        # remove style tag inside the table contents
        # details = details.style.decompose()
        prev = ''
        msg = ''

        for detail in details:
            # we are going to get the details
            lftData = detail.find("th")
            rgtData = detail.find("td")

            if (lftData != None and rgtData != None):

                style_tag = rgtData.style
                if style_tag != None:
                    style_tag.decompose()
                # •

                lftData = detail.find("th").get_text(
                    separator=', ', strip=True)
                rgtData = detail.find("td").get_text(
                    separator=', ', strip=True)

                if detail.find("div", class_='country-name'):
                    country_data['Country Name'] = detail.find(
                        "div", class_='country-name').get_text(separator=", ", strip=True)
                    culprit_found = True

                if 'Capital' in lftData:
                    capital_city, largest_city = wiki_parse_capital_city(
                        lftData, rgtData[0:rgtData.find("/")])

                    country_data['Capital City'] = capital_city

                    if largest_city != '':
                        country_data['Largest City'] = largest_city

                msg += lftData + ': ' + rgtData + '\n'
                # print(lftData + ': ' + rgtData)

            else:
                if lftData:

                    if lftData.find("div", class_='country-name'):
                        # to get the entire text separated by commna (or any char) of an element
                        # data = lftData.get_text(
                        #     separator=", ", strip=True)
                        country_data['Country Name'] = lftData.find(
                            "div", class_='country-name').get_text(separator=", ", strip=True)
                    else:
                        data = lftData.get_text(
                            separator=", ", strip=True)
                        msg += data + '\n'
                        print(data)

        print(country_data)
        if culprit_found == True:
            input("Country name is not found. But we caught him redhanded...")
        with open('data-dump.txt', 'wb') as cd:
            cd.write(msg.encode())
