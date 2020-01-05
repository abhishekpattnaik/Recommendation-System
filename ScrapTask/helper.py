import json
from bs4 import BeautifulSoup
from constants import *
import requests
from urllib.parse import urlparse

def isNotPresent(url,dbCollection):	#to check whether the url present in the corresponding database
	for items in db[dbCollection].find({"urls":url}):
		return False
	return True

def isUrlPresent(url,dbCollection):
	for colObj in db[dbCollection].find({}):
		if url in str(colObj["urls"]):
			return True
	return False

def article(url,url_id):
	# url = 'https://medium.com/better-humans/how-to-set-up-your-iphone-for-productivity-focus-and-your-own-longevity-bb27a68cc3d8'
	res = requests.get(url)
	mainSoup = BeautifulSoup(res.text,'html.parser')
	jsonSoup=BeautifulSoup(res.text,'html.parser').find(type="application/ld+json")
	for element in jsonSoup:
		jsonstring=str(element)
	data = json.loads(jsonstring)
	def fullArticle():
		artilceString=''
		for elem in mainSoup.find_all('p'):
			artilceString=artilceString+elem.get_text()
		return artilceString
	def author():
		return data['author']['name']
	def description():
		return data['description']
	def headline():
		return data['headline']
	def articleType():
		return data['@type']
	def claps():
		claps=str(0)
		
		for elem in mainSoup.find_all('button'):
			if 'claps' in elem.get_text():
				claps = elem.string
				break;
		return str(claps)
	return {'author':author(),'Headline':headline(),'Description':description(),'Type':articleType(),'Claps':claps(),'Full Article':fullArticle(),'url':url,'url_id':url_id}

def isScrapped(monDict): #To check whether the dictionay is scrapped or not
	if(monDict['status']==False):
		return True
	else:
		return False


def check(userInput,url): #To check whether the domain is present in the url or not
	if userInput in url:
		return True
	else:
		return False


def getDomain(ur):
	parsed_uri = urlparse(ur)
	result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	return result