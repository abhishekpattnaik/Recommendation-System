from recommend_app.scripts.get_raw_data import populate_raw_data
from recommend_app.scripts.configurations import db
from recommend_app.scripts.constants import USER_URL, URL_COLLECTION_NAME, URL_META_COLLECTION_NAME

def count_run_check():
    '''
    This will be responsible for triggering all the population 
    '''
    raw_count = db[URL_COLLECTION_NAME].estimated_document_count()
    fitlered_count = db[URL_META_COLLECTION_NAME].estimated_document_count()
    populate_raw_data()
    print("Total raw data updated =", db[URL_COLLECTION_NAME].estimated_document_count()-raw_count)
