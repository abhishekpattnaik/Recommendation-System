from getRawData import populateRawData
from putFilteredData import populateFilteredData
from configurations import db
from constants import userUrl
from helper import isUrlPresent


def Count_Run_Check():
	rawCount=db.rawCollection.count()
	fitleredCount=db.filteredCollection.count()
	populateRawData()
	populateFilteredData(userUrl)
	print("Total raw data updated =",db.rawCollection.count()-rawCount)
	print("Total filtered data updated = ",db.filteredCollection.count()-fitleredCount)
