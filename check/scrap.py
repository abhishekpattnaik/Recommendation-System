from helper import *
from urls import *
ulist=urlList()
if(ulist!=0):
	for links in ulist:
		print(article(links))
else:
	print('no urls inputed')