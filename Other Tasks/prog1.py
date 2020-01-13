'''In process '''

import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from configurations import db
from constants import URL_DATA_COLLECTION



def compute_tf(input_str, user_str):
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

def compute_idf(collection, user_str):
    ''' this will return the idf value of the word from the dictionary '''
    present_count = 0
    collection_count = db[collection].count()

    idf = log(collection_count/present_count)
    return idf