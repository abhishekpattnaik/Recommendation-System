from bs4 import BeautifulSoup
import requests
from Program4 import urlList
# url = input("url")
# url = 'https://medium.com/better-humans/how-to-set-up-your-iphone-for-productivity-focus-and-your-own-longevity-bb27a68cc3d8'
# url ='https://elemental.medium.com/science-confirms-that-the-vagus-nerve-is-key-to-well-being-c23fab90e211' 
def scrapped(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text,'html.parser')
	for elem in soup.find_all('button'):
		if elem.string.endswith('claps'):
			claps = elem.string
			break;
	heading = soup.find('h1').string
	count =0
	# print(soup.find('article.h2'))
	val = {"claps":claps,"heading":heading}
	return val
def urlList():
	urls = []
	for i in range(int(input("no of urls"))):
		x = input("urls")
		urls.append(x)
	return urls
for i in urlList():
	print(scrapped(i))
# print(urlList())
# print(val)