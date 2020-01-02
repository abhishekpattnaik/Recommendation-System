from bs4 import BeautifulSoup
import requests
def urlList():
	urls = []
	for i in range(int(input("no of urls"))):
		x = input("urls")
		urls.append(x)
	return urls
	
# print(urls)