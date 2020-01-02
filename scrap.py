from helper import *
from urls import *
li=urlList()
# print(li)
# articleDict={'author':author(),'Headline':headline(),'Description':description(),'Type':articleType(),'Claps':claps()}
if(li!=0):
	for links in li:
		print(article(links))
# else:
# 	print('no urls inputed')