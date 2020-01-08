import re
import math
from collections import Counter
import nltk
from nltk.corpus import stopwords
from configurations import db
from constants import URL_DATA_COLLECTION, URL_TF_IDF_COLLECTION

def get_tf_val(input_str, user_str):
    '''This will return the calculated term frequency in the given dict '''
    input_str = input_str.lower()
    input_str = re.sub('\W+', ' ', input_str)
    tokens = nltk.word_tokenize(input_str)
    filtered = [w for w in tokens if not w in stopwords.words('english')] 
    count = dict(Counter(filtered)) 
    length = len(count)
    for key,value in count.items(): 
        if user_str == key: 
            return value/length 
    return 0


def is_present(url_dict,user_str):
    for key in url_dict['word_count'].keys():
        if user_str == key:
            return True
    return False


def compute_tf(collection,user_str):
    coll_obj = db[collection].find()
    for url_dict in coll_obj:
        if is_present(url_dict,user_str):
            print(url_dict['urls'],get_tf_val(url_dict['page artilce'],user_str))
# compute_tf(URL_DATA_COLLECTION,'technology')


def compute_idf(collection, user_str):
    ''' this will return the idf value of the word from the dictionary '''
    present_count = 0
    collection_count = db[collection].count()
    coll_obj = db[collection].find()
    for url_dict in coll_obj:
        if is_present(url_dict,user_str):
            present_count += 1
    idf = math.log(collection_count/present_count)
    return idf

