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

# doc1 = 'When I published the article “Understanding Blockchain” many of you wrote me to ask me if I could make one dedicated to Artificial Intelligence. The truth is that I hadn’t had time to get on with it and before sharing anything, I wanted to finish some courses in order to add value to the recommendations.The problem with Artificial Intelligence is that it’s much more fragmented, both technologically and in use cases, than Blockchain, making it a real challenge to condense all the information and share it meaningfully. Likewise, I have tried to make an effort in the summary of key concepts and in the compilation of interesting sources and resources, I hope it helps you as well as it did to me!'
# doc2 = 'The way Stefan got an idea to write an article about natural language processing is simple — every once in a while he would stumble across a good article and save bits and pieces here and there.Once he decided to accumulate these thoughts and put them in o ne place — that worked out as an ultimated NLP guide. In this 23-minute read, the author managed to put enough insights and wisdom, that someone could write a book based on this post.The article describes the possible applications, challenges, and work mechanisms of natural language processing. It might not be an “easy” read — your head feels “stuffed” after you are done, but it’s definitely t he one you’ll always come back to.' 
# doc3 = 'Goroutines are otherwise normal functions that Go executes concurrently. We could write an entire article digging into how Goroutines work under the hood, but at a high level, Goroutines are lightweight threads managed automatically by the Go runtime. Many Goroutines can fit on a single OS thread, and if a Goroutine blocks an OS thread, the Go runtime automatically moves the rest of the Goroutines over to a new OS thread.Goroutines also offer a feature called “channels,” which allow Goroutines to pass messages between themselves, allowing us to schedule requests and prevent race conditions.Implementing all of this functionality in Python may be doable with recent tools like asyncio, but the fact that Go is designed with this use case in mind makes our lives much easier.'
# doc4 = 'The final note I’ll make on why we ultimately built Cortex in Go is that Go is just nice.Relative to Python, Go is a bit more painful to get started with. Go’s unforgiving nature, however, is what makes it such a joy for large projects. We still heavily test our software, but static typing and compilation — two things that make Go a bit less comfortable for beginners — act as sort of guard rails for us, helping us to write (relatively) bug-free code.There may be other languages you could argue offer a particular advantage, but on balance, Go best satisfies our technical and aesthetic needs.'
# doc5 = 'We still love Python, and it has its place within Cortex, specifically around inference processing.Cortex serves TensorFlow, PyTorch, scikit-learn, and other Python models, which means that interfacing with the models—as well as pre and post inference processing—are done in Python. However, even that Python code is packaged up into Docker containers, which are orchestrated by code that is written in Go.If you’re interested in becoming a machine learning engineer, knowing Python is more or less non-negotiable. If you’re interested in working on machine learning infrastructure, however, you should seriously consider using Go.'
# doc6 = 'In today’s scenario, one way of people’s success identified by how they are communicating and sharing information to others. That’s where the concepts of language come into picture. However, there are many languages in the world. Each has many standards and alphabets, and the combination of these words arranged meaningfull'
# doc_list = [doc1,doc2,doc3,doc4,doc5,doc6]


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


def get_tf_list():
    ''' This will return the list of tf_dict '''
    tf_list = []
    def get_tf(word_count, doc_length):
        tf_wc = {}
        for key,value in word_count.items():
            tf_wc[key] = float(value)/float(doc_length)
        return tf_wc
    for doc_id in DIL:
        word_count = WCL[doc_id]['word_list']
        doc_length = WCL[doc_id]['size']
        tf_list.append(get_tf(word_count, doc_length))
    return tf_list


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
    tf_idf_list = []
    tf_list = get_tf_list()
    df_dict = get_df_dict()
    count = get_words_count()
    for doc in tf_list:
        doc_dict = {}
        for key,value in doc.items():
            doc_dict[key]=value*math.log(len(tf_list)/df_dict[key])
        tf_idf_list.append(doc_dict)

    return tf_idf_list


def search_word(input_str):
    '''This will return the list of most recommended doc in descending order '''
    p_stemmer = SnowballStemmer("english")
    # PorterStemmer()
    input_str = p_stemmer.stem(input_str)
    TI_list = get_tf_idf()
    score_rank = {}
    doc_id = 0
    for doc in TI_list:
        if input_str in doc:
            score_rank[doc_id]=doc[input_str]
        doc_id += 1
    # print('check') 
    return {key: value for key, value in sorted(score_rank.items(), key=lambda item: item[1], reverse=True)}


# print(search_word(input('input string')))
'''--------------------------------------------------------------------------------------------------------'''

def update(source_collection):    
    # doc_count_list=[]
    count = 0
    doc_count = db[source_collection].estimated_document_count()
    for elem in db[source_collection].find():
        word_list,size = most_count_list(elem['page artilce'])
        # WCL.append({str(elem['_id']):{'word_list':word_list,'size':size,'url':elem['urls']}}) 
        # DIL.append(str(elem['_id']))
        WCL[elem['_id']]={'word_list':word_list,'size':size,'url':elem['urls']} 
        DIL.append(elem['_id'])
        count += 1
        print('processed',count,'/',doc_count)
        if count == 10:
            break
    # for doc_id in DIL:
    #     print(WCL[doc_id]['size'])
    # print(WCL)


def search_website(input_str='test', source_collection='url_data'):
    '''from the given imput this will search the top recommended websites '''
    update(source_collection) 
    print(search_word(input('input the str')))
search_website()


