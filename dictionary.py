from sys import argv
from urllib2 import Request, urlopen
import json
# script, word =argv

class dictionary(object):
    def __init__(self, word):
        self.meaning=word

    def get_definition(self):
        request = Request('http://api.pearson.com/v2/dictionaries/entries?headword=%r'%self.meaning)
        response = urlopen(request)
        kittens = response.read()
        tmp = json.loads(kittens)
        tmp.keys()
        print tmp['results'][0]['senses'][0]['definition']
#https://www.codecademy.com/courses/python-intermediate-en-6zbLp/0/1?curriculum_id=50ecbb9b71204640240001bf
#http://developer.pearson.com/apis/dictionaries#/

meaning=dictionary("autism")
meaning.get_definition()