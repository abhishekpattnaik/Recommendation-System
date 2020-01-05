#------------------------>warning<-----------------------------
#this program is used to clean all the collections form the database of mongo

from configurations import db
db.rawCollection.drop()
db.filteredCollection.drop()
print("Both Collections dropped")