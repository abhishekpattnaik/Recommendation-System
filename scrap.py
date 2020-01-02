from helper import *
from urls import *
li=urlList()
if(li!=0):
	for links in li:
		print(article(links))
else:
	print('no urls inputed')