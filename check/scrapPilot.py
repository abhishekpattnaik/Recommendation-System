from getRawData import populateRawData
from putFilteredData import populateFilteredData
from configurations import db
from helper import isUrlPresent

userUrl='medium.com/'								#method of article in helper.py is based on medium.com
rawCount=db.rawCollection.count()
fitleredCount=db.filteredCollection.count()
populateRawData()									#populates the raw data into the rawCollection of database
if isUrlPresent(userUrl,'rawCollection'):			#Checks whether the desired link is present or not
	populateFilteredData(userUrl)					#if present then populates the filtered data into the filteredCollection of database
else:
	print("No such matching url found")				#else doesn't populate the data
print()
print("Total raw data updated =",db.rawCollection.count()-rawCount)
print("Total filtered data updated = ",db.filteredCollection.count()-fitleredCount)

print("Done")