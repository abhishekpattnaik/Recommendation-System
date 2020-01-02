import json
from bs4 import BeautifulSoup
import requests
url = 'https://medium.com/better-humans/how-to-set-up-your-iphone-for-productivity-focus-and-your-own-longevity-bb27a68cc3d8'
res = requests.get(url)
Soup=BeautifulSoup(res.text,'html.parser').find(type="application/ld+json")
jsonstring=''
for element in Soup:
	jsonstring=str(element)
data = json.loads(jsonstring)
def author():
	return data['author']['name']
def description():
	return data['description']
def headline():
	return data['headline']
def articleType():
	return data['@type']
def claps():
	clapSoup = BeautifulSoup(res.text,'html.parser')
	for elem in clapSoup.find_all('button'):
		if elem.string.endswith('claps'):
			claps = elem.string
			break;
	return str(claps)
def urlinput():
	return url
# print(author())
# print(description())
# print(headline())
# print(articleType())
# print(claps())
def article():
	return {'author':author(),'Headline':headline(),'Description':description(),'Type':articleType(),'Claps':claps(),'url':urlinput()}
# print(articleDict)