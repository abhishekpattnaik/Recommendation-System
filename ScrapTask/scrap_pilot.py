from get_raw_data import populate_raw_data
from put_filtered_data import populate_filtered_data
from configurations import db
from constants import USER_URL, URL_COLLECTION_NAME, URL_META_COLLECTION_NAME

def count_run_check():
    '''This will be responsible for triggering all the population '''
    raw_count = db[URL_COLLECTION_NAME].estimated_document_count()
    fitlered_count = db[URL_META_COLLECTION_NAME].estimated_document_count()
    populate_raw_data()
    # populate_filtered_data(USER_URL)
    print("Total raw data updated =", db[URL_COLLECTION_NAME].estimated_document_count()-raw_count)
    # print("Total filtered data updated = ", db[URL_META_COLLECTION_NAME].estimated_document_count()-fitlered_count)
count_run_check()
# populate_filtered_data(USER_URL)
