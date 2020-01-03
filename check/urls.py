from constants import *
def urlList():
	number_of_urls=int(input("no of urls"))
	if (number_of_urls==0):
		return 0
	else:
		for i in range(number_of_urls):
			x = input("urls")
			urls.append(x)
	return urls
	# https://medium.com/better-humans/how-to-set-up-your-iphone-for-productivity-focus-and-your-own-longevity-bb27a68cc3d8