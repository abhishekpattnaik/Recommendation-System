'''This file is for all the required dependencies '''
from collections import Counter
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from configurations import db
from constants import WORD_COUNT_LIST as WCL
from constants import DOCUMENT_ID_LIST as DIL
import pandas as pd
import math
from nltk.stem.snowball import SnowballStemmer

def remove_spec_char(input_str):
    '''This will remove all the special characters from the given string '''
    input_str=input_str.lower()
    return re.sub('\W+', ' ', input_str)


def most_count_list(input_str):
    '''Returns the list of top ten repeated keywords '''
    input_str = remove_spec_char(input_str)
    tokens = nltk.word_tokenize(input_str)
    filtered = [w for w in tokens if not w in stopwords.words('english')]   
    p_stemmer = SnowballStemmer("english")
    # PorterStemmer()
    for i in range(len(filtered)):
        filtered[i] = p_stemmer.stem(filtered[i]) 
    count = Counter(filtered)
    return dict(count),len(tokens)


def get_words_count():
    ''' This method will return number of words present in that doc '''
    count = 0
    for doc_id in DIL:
        doc_length = WCL[doc_id]['size']
        count = count+doc_length
    return count


def get_tf_dict():
    ''' This will return the list of tf_dict '''
    tf_dict = {}
    def get_tf(word_count, doc_length):
        tf_wc = {}
        for key,value in word_count.items():
            tf_wc[key] = float(value)/float(doc_length)
        return tf_wc
    for doc_id in DIL:
        word_count = WCL[doc_id]['word_list']
        doc_length = WCL[doc_id]['size']
        tf_dict[doc_id]=get_tf(word_count, doc_length)
    return tf_dict


def get_df_dict():
    '''This will return the df dict '''
    df_dict = {}
    for doc_id in DIL:
        word_count = WCL[doc_id]['word_list']
        doc_length = WCL[doc_id]['size']
        for word in word_count:
            if word not in df_dict:
                df_dict[word] = 1
            else:
                df_dict[word] = df_dict[word]+1
    return df_dict


def get_tf_idf():
    ''' This will return the list of dictionaries according to the doc list implying the tf idf core of each word'''
    tf_idf_dict = {}
    tf_dict = get_tf_dict()
    df_dict = get_df_dict()
    count = get_words_count()
    for doc in DIL:
        doc_dict = {}
        for key,value in tf_dict[doc].items():
            doc_dict[key]=value*math.log(len(tf_dict)/df_dict[key])
        tf_idf_dict[doc]=doc_dict

    return tf_idf_dict


def search_word(input_str):
    '''This will return the list of most recommended doc in descending order '''
    p_stemmer = SnowballStemmer("english")
    # PorterStemmer()
    input_str = p_stemmer.stem(input_str)
    TI_dict = get_tf_idf()
    score_rank = {}
    for doc in DIL:
        if input_str in TI_dict[doc]:
            score_rank[doc]=TI_dict[doc][input_str]
    return {key: value for key, value in sorted(score_rank.items(), key=lambda item: item[1], reverse=True)}


def update(source_collection):    
    ''' updates the local variable value as it populates the word count list corresponding to its url's object id '''
    # doc_count_list=[]
    count = 0
    doc_count = db[source_collection].estimated_document_count()
    for elem in db[source_collection].find():
        word_list,size = most_count_list(elem['page artilce'])
        WCL[elem['_id']]={'word_list':word_list,'size':size,'url':elem['urls']} 
        DIL.append(elem['_id'])
        count += 1
        print('processed',count,'/',doc_count)

def search_website(input_str='test', source_collection='url_data'):
    '''from the given imput this will search the top recommended websites '''
    update(source_collection)
    sw = search_word(input('input the str'))
    for ob_id in sw.keys():
        print(WCL[ob_id]['url'])f()
# search_website()
