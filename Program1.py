from bs4 import BeautifulSoup
import requests

res = requests.get('https://elemental.medium.com/science-confirms-that-the-vagus-nerve-is-key-to-well-being-c23fab90e211')
soup = BeautifulSoup(res.text,'html.parser')
for elem in soup.find_all('button'):
	if elem.string.endswith('claps'):
		claps = elem.string
		break;
heading = soup.find('h1').string
val = {"claps":claps,"heading":heading}
# print(val)

from pymongo import MongoClient
client = MongoClient()
db = client.testdatabase
collection = db.collection
# x = int(input("please enter the no of times"))
collection.insert(val)  
print('done')