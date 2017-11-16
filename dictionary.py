from sys import argv
from urllib2 import Request, urlopen, URLError
import json
import pickle
import os
script, word = argv 											   #to take input from user


def internet_on():                                                 #to check if the internet is turned on or not.  
	
	try:
		urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=9lwKWuipCeby8AfD_KnwBQ', timeout=1)
		print "Internet is ON"
		return True
	except URLError as err: 
		print "Internet is not working"
		return False


class Dictionary(object):                                               #class defining the word and to function to get the definition of the word
	def __init__(self, word):                                           #either by offline dictionary or using the internet if the word does not exists in offline dict
		self.meaning=word
		self.dictionary=self.load_dictionary()

	def get_definition(self):
		
		x=self.check()
		if x==True:
			pass
		else:
			try:
				request = Request('http://api.pearson.com/v2/dictionaries/laad3/entries?headword=%r'%self.meaning)
				response = urlopen(request)
				read_response = response.read()
				tmp = json.loads(read_response)
				tmp.keys()
				if(len(tmp['results'])==0):
					print "no such word exists"
				else:
					word_meaning=tmp['results'][0]['senses'][0]['definition']
					print word_meaning
					d={self.meaning:word_meaning}
					self.store_words(d)
				raise
			except e:
				print "got an error code", e
	
	def check(self):                                                          #function to check if the word exists in the offline dictionarys
		if self.dictionary.get(self.meaning):
			print "meaning from offline dictionary"
  			print self.dictionary[self.meaning] 
  			return True
		else:
 			print "searching from the internet"
  			return False


	def load_dictionary(self):
		if os.path.exists('offline_dictionary'):
			return pickle.load(open('offline_dictionary','rb'))
		else:
			return {}
	

	def store_words(self,m):                                                  #to create a offline dictionary if it does not exists  
			pickle.dump(self.dictionary, open(r'offline_dictionary', 'wb'))
			words=pickle.load(open('offline_dictionary','rb'))                #if it exists add the word and its meaning. (used pickle for this)
			words.update(m)
			pickle.dump(words, open(r'offline_dictionary', 'wb'))
	

x=internet_on()                                            #call to check internet connection
if x==True:                                                #The rest of the code runs only if internet is on
	meaning=Dictionary(word)
	meaning.get_definition() 

else:
	print"please turn on your internet"

#important websites
#https://www.codecademy.com/courses/python-intermediate-en-6zbLp/0/1?curriculum_id=50ecbb9b71204640240001bf
#http://developer.pearson.com/apis/dictionaries#/