from bs4 import BeautifulSoup
from constants import *
import requests
from configurations import db
from helper import getDomain,isNotPresent
from functools import lru_cache


def populateRawData():
	print('populating in rawCollection...')
	for pageNo in tqdm(range(1,21)):
		res = requests.get('https://news.ycombinator.com/news?p='+str(pageNo))
		Soup=BeautifulSoup(res.text,'html.parser')
		for tagObj in Soup.find_all('a',class_='storylink'):
			if isNotPresent(tagObj.attrs['href'],'rawCollection'):	
				db.rawCollection.insert_one({'urls':tagObj.attrs['href'],'domain':getDomain(tagObj.attrs['href']),'status':False}) 
