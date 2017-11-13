from sys import argv
import urllib2 
import json
#script, word = argv


#print argv, type(argv), 


def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        print "Internet is ON"
        return True
    except urllib2.URLError as err: 
    	print "Internet is not working"
        return False



class Dictionary(object):
	def __init__(self, word):
		self.meaning=word

	def get_definition(self):
		
			request = Request('http://api.pearson.com/v2/dictionaries/entries?headword=%r'%self.meaning)
			response = urlopen(request)
			read_response = response.read()
			tmp = json.loads(read_response)
			tmp.keys()
			print tmp['results'][0]['senses'][0]['definition']
#https://www.codecademy.com/courses/python-intermediate-en-6zbLp/0/1?curriculum_id=50ecbb9b71204640240001bf
#http://developer.pearson.com/apis/dictionaries#/
	

x=internet_on()
if x==True:
	meaning=Dictionary("autism")
	meaning.get_definition() 

else:
	print"please turn on your internet"