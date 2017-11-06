from sys import argv
from urllib2 import Request, urlopen, URLError
import json

script, word =argv
print "the word is",word
request = Request('http://api.pearson.com/v2/dictionaries/entries?headword=%r'%word)


response = urlopen(request)
kittens = response.read()
tmp = json.loads(kittens)
tmp.keys()
print tmp['results'][0]['senses'][0]['definition']


