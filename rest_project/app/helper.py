from math import log
from re import sub
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from collections import Counter
from app.constants import WORD_COUNT_DICT as WCD
from app.constants import INVERSE_DOCUMENT_FREQUENCY as IDF 
from app.constants import TF_IDF
from app.configurations import db
from pandas import DataFrame 

p_stemmer = SnowballStemmer("english")


def populate_WCD(db_collection='url_data'):
	'''initializes the  WORD_COUNT_DICT by filtering and tokenizing'''
	for doc_obj in db['url_data'].find():
		doc_dict = {}
		doc_id = str(doc_obj['_id'])
		doc_str = str(doc_obj['page artilce']).lower()
		doc_str = sub('\W+', ' ', doc_str)
		doc_dict[doc_id] = doc_str
		token = word_tokenize(doc_dict[doc_id])
		token = [p_stemmer.stem(w) for w in token if not w in stopwords.words('english')]
		count = dict(Counter(token))
		WCD[str(doc_obj['_id'])] = {'count':count, 'url':doc_obj['urls'], 'title':doc_obj['title']}


def populate_IDF():
	size = len(WCD)
	for doc in WCD:
		for word in WCD[doc]['count']:
			if word not in IDF:
				IDF[word] = 1
			else:
				IDF[word] += 1
	for word,count in IDF.items():
		IDF[word] = 1+log(size/count)


def populate_TF_IDF():
	for doc in WCD:
		tf_count = WCD[doc]['count']
		size = len(tf_count)
		for key,value in tf_count.items():
			tf = value / float(size)
			tf_count[key] = tf * IDF[key]
		TF_IDF[doc] = tf_count


def search_word(input_str):
	input_str = p_stemmer.stem(input_str)
	score_rank = {}
	for doc in TF_IDF:
		if input_str in TF_IDF[doc]:
			score_rank[doc] = TF_IDF[doc][input_str]
	return {key: value for key, value in sorted(score_rank.items(), key=lambda item: item[1], reverse=True)}

def update_db():
	populate_WCD()
	populate_IDF()
	populate_TF_IDF()
	db['tf-idf'].drop()
	db['tf-idf'].insert_one({'WCD':WCD,'IDF':IDF, 'TF-IDF':TF_IDF})


def get_all_values():
	wocodo = {}
	for url_obj in db['tf-idf'].find():
		wocodo.update(url_obj['WCD'])
	return wocodo

def populate_all_values():
	for url_obj in db['tf-idf'].find():
		WCD.update(url_obj['WCD'])
		IDF.update(url_obj['IDF'])
		TF_IDF.update(url_obj['TF-IDF'])

def get_search(input_str):
	input_str = str(input_str)
	populate_all_values()
	token = word_tokenize(input_str)
	temp_dict = {}
	token = [p_stemmer.stem(w) for w in token if not w in stopwords.words('english')]
	for elem in token:
		temp_dict[elem] = search_word(elem)
	df = DataFrame(temp_dict).fillna(0)
	df = df.sum(axis=1).sort_values(ascending=False)
	uid_dict=dict(df)
	final_dict={}
	for uid in uid_dict:
		final_dict[uid]={'url':WCD[uid]['url'],'title':WCD[uid]['title']}
	return final_dict
