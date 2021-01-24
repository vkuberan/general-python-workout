import os
import platform
import subprocess
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup

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
    except:
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
    print(data_file)
