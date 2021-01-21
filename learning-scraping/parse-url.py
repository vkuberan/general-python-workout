from urllib.parse import urlparse

url = 'http://stackoverflow.com/questions/1234567/blah-blah-blah-blah'

o = urlparse(url)

print(o)
