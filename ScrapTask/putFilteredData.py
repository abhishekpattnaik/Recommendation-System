from urllib.parse import urlparse
from configurations import db
from helper import *

def populateFilteredData(userInput):
	print("please wait while populating the filtered data.")
	for items in db.rawCollection.find({}):
		if isScrapped(items) and check(userInput,items['urls']):
			db.filteredCollection.insert_one(article(items['urls'],items['_id']))
			db.rawCollection.update_one({"_id" : items['_id']},{'$set':{"status" : True}})
			print('Filtered->',items['urls'])