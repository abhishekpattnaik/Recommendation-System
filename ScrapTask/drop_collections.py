'''This drop url and urls_meta databases '''
from configurations import db,URL_COLLECTION_NAME,URL_META_COLLECTION_NAME
db[URL_COLLECTION_NAME].drop()
db[URL_META_COLLECTION_NAME].drop()
print("Both Collections dropped")
