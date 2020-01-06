from urllib.parse import urlparse
from configurations import db
from helper import *

def populateFilteredData(userInput):
	print("please wait while populating the filtered data.")
	try:
		if isUrlPresent(userInput,'rawCollection'):
			for items in db.rawCollection.find({}):
				if isScrapped(items) and check(userInput,items['urls']):
					db.filteredCollection.insert_one(article(items['urls'],items['_id']))
					db.rawCollection.update_one({"_id" : items['_id']},{'$set':{"status" : True}})
					print('Filtered->',items['urls'])
				# print('Check')
		else:
			print('No Such Matching String found')
	except:
		print('Error occured while filtering the Raw Collectionn ')