import json

data_dir = 'wiki/data/all-countries.json'
base_wiki_url = 'https://en.wikipedia.org/'
wiki_countries_entry = None

with open(data_dir, 'r') as fp:
    wiki_countries_entry = json.load(fp)

i = 0

for entry, country_info in wiki_countries_entry.items():
    print(entry, ": ", country_info)
    if i % 25 == 0:
        input("Press any key to continue....")
    i += 1
