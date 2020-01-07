'''This file is to populate the filtered data'''
from configurations import db
from helper import article, check
from constants import URL_META_COLLECTION_NAME, URL_COLLECTION_NAME


def populate_filtered_data(user_input):
    '''it will populate all the new data into the url_meta collection'''
    print("please wait while populating the filtered data.")
    for items in db[URL_COLLECTION_NAME].find({'status':False}):
        if check(user_input, items['urls']):                 
            url_data = article(items['urls'], items['_id'])
            db[URL_META_COLLECTION_NAME].insert_one(url_data)
            db[URL_COLLECTION_NAME].update_one({"_id" : items['_id']}, {'$set':{"status" : True}})
            print('Filtered->', items['urls'])
