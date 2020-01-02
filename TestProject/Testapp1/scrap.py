from helper import *
# from urls import *

def urlList():
	urls = []
	number_of_urls=int(input("no of urls"))
	if (number_of_urls==0):
		return 0
	else:
		for i in range(number_of_urls):
			x = input("urls")
			urls.append(x)
	return urls

li=urlList()
if(li!=0):
	for links in li:
		print(article(links))
else:
	print('no urls inputed')