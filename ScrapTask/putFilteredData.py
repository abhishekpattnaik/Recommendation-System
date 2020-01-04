from urllib.parse import urlparse
from configurations import db
from helper import *
from tqdm import tqdm
import sys


def populateFilteredData(userInput):
	sys.stdout.write("please wait while populating the filtered data.")
	for items in db.rawCollection.find({}):
		if isScrapped(items) and check(userInput,items['urls']):
			db.filteredCollection.insert_one(article(items['urls'],items['_id']))
			db.rawCollection.update_one({"_id" : items['_id']},{'$set':{"status" : True}})
			sys.stdout.write('.')
			sys.stdout.flush()