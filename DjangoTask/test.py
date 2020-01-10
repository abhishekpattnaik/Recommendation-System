'''This file is for all the required dependencies '''
from collections import Counter
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
# from configurations import db
import pandas as pd

doc1 = 'When I published the article “Understanding Blockchain” many of you wrote me to ask me if I could make one dedicated to Artificial Intelligence. The truth is that I hadn’t had time to get on with it and before sharing anything, I wanted to finish some courses in order to add value to the recommendations.The problem with Artificial Intelligence is that it’s much more fragmented, both technologically and in use cases, than Blockchain, making it a real challenge to condense all the information and share it meaningfully. Likewise, I have tried to make an effort in the summary of key concepts and in the compilation of interesting sources and resources, I hope it helps you as well as it did to me!'
doc2 = 'The way Stefan got an idea to write an article about natural language processing is simple — every once in a while he would stumble across a good article and save bits and pieces here and there.Once he decided to accumulate these thoughts and put them in o ne place — that worked out as an ultimated NLP guide. In this 23-minute read, the author managed to put enough insights and wisdom, that someone could write a book based on this post.The article describes the possible applications, challenges, and work mechanisms of natural language processing. It might not be an “easy” read — your head feels “stuffed” after you are done, but it’s definitely t he one you’ll always come back to.' 
doc3 = 'Goroutines are otherwise normal functions that Go executes concurrently. We could write an entire article digging into how Goroutines work under the hood, but at a high level, Goroutines are lightweight threads managed automatically by the Go runtime. Many Goroutines can fit on a single OS thread, and if a Goroutine blocks an OS thread, the Go runtime automatically moves the rest of the Goroutines over to a new OS thread.Goroutines also offer a feature called “channels,” which allow Goroutines to pass messages between themselves, allowing us to schedule requests and prevent race conditions.Implementing all of this functionality in Python may be doable with recent tools like asyncio, but the fact that Go is designed with this use case in mind makes our lives much easier.'
doc4 = 'The final note I’ll make on why we ultimately built Cortex in Go is that Go is just nice.Relative to Python, Go is a bit more painful to get started with. Go’s unforgiving nature, however, is what makes it such a joy for large projects. We still heavily test our software, but static typing and compilation — two things that make Go a bit less comfortable for beginners — act as sort of guard rails for us, helping us to write (relatively) bug-free code.There may be other languages you could argue offer a particular advantage, but on balance, Go best satisfies our technical and aesthetic needs.'
doc5 = 'We still love Python, and it has its place within Cortex, specifically around inference processing.Cortex serves TensorFlow, PyTorch, scikit-learn, and other Python models, which means that interfacing with the models—as well as pre and post inference processing—are done in Python. However, even that Python code is packaged up into Docker containers, which are orchestrated by code that is written in Go.If you’re interested in becoming a machine learning engineer, knowing Python is more or less non-negotiable. If you’re interested in working on machine learning infrastructure, however, you should seriously consider using Go.'
doc6 = 'In today’s scenario, one way of people’s success identified by how they are communicating and sharing information to others. That’s where the concepts of language come into picture. However, there are many languages in the world. Each has many standards and alphabets, and the combination of these words arranged meaningfull'
doc_list = [doc1,doc2,doc3,doc4,doc5,doc6]
IDF = []


def remove_spec_char(input_str):
    '''This will remove all the special characters from the given string '''
    input_str=input_str.lower()
    return re.sub('\W+', ' ', input_str)


def most_count_list(input_str):
    '''Returns the list of top ten repeated keywords '''
    input_str = remove_spec_char(input_str)
    tokens = nltk.word_tokenize(input_str)
    filtered = [w for w in tokens if not w in stopwords.words('english')]   
    p_stemmer = PorterStemmer()
    for i in range(len(filtered)):
        filtered[i] = p_stemmer.stem(filtered[i]) 
    count = Counter(filtered)
    return dict(count),len(tokens)


def get_tf_list(doc_list):
    ''' This will return the list of tf_dict '''
    tf_list = []
    def get_tf(word_count, doc_length):
        tf_wc = {}
        for key,value in word_count.items():
            tf_wc[key]=float(value)/float(doc_length)
        return tf_wc
    for doc in doc_list:
        word_count,doc_length = most_count_list(doc)
        tf_list.append(get_tf(word_count, doc_length))
    return tf_list

def get_df(doc_list):
    df_dict = {}
    for doc in doc_list:
        word_count,doc_length = most_count_list(doc)
    pass
# def get_df(word_list):
#     DF = []
#     for elem in word_list:
#         for sub in elem:
#             for subs in sub.keys():
#                 if subs not in DF:
#                     DF.append(subs)
#     return DF


print(pd.DataFrame(get_tf_list(doc_list)))  
