from sys import argv
from urllib2 import Request, urlopen, URLError
import json
script, word = argv


#print argv, type(argv)


def internet_on():
	try:
		urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=9lwKWuipCeby8AfD_KnwBQ', timeout=1)
		print "Internet is ON"
		return True
	except URLError as err: 
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
			if(len(tmp['results'])==0):
				print "no such word exists"
			else:
				print tmp['results'][0]['senses'][0]['definition']
#https://www.codecademy.com/courses/python-intermediate-en-6zbLp/0/1?curriculum_id=50ecbb9b71204640240001bf
#http://developer.pearson.com/apis/dictionaries#/
	

x=internet_on()
if x==True:
	meaning=Dictionary(word)
	meaning.get_definition() 

else:
	print"please turn on your internet"