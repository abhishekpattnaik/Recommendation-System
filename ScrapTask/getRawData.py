from bs4 import BeautifulSoup
from constants import *
import requests
from configurations import db
from helper import getDomain,isNotPresent
def populateRawData():
	print('populating in rawCollection...')
	try:
		for pageNo in tqdm(range(1,21)):
			res = requests.get('https://news.ycombinator.com/news?p='+str(pageNo))
			Soup=BeautifulSoup(res.text,'html.parser')
			for tagObj in Soup.find_all('a',class_='storylink'):
				if isNotPresent(tagObj.attrs['href'],'rawCollection') and 'http' in str(tagObj.attrs['href']):	
					db.rawCollection.insert_one({'urls':tagObj.attrs['href'],'domain':getDomain(tagObj.attrs['href']),'status':False}) 
	except:
		print('Error occured while scrapping raw data')