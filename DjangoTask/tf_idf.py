from math import log
from re import sub
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from collections import Counter
from constants import WORD_COUNT_DICT as WCD
from configurations import db

p_stemmer = SnowballStemmer("english")

doc_dict = {'docA' : "The car is driven on the road.",'docB' : "The truck is driven on the highway."}

def populate_WCD(doc_dict):
	'''initializes the  WORD_COUNT_DICT by filtering and tokenizing'''
	for doc in doc_dict:
		doc_str = doc_dict[doc].lower()
		doc_str = sub('\W+', ' ', doc_str)
		doc_dict[doc] = doc_str
		token = word_tokenize(doc_dict[doc])
		token = [p_stemmer.stem(w) for w in token if not w in stopwords.words('english')]
		count = dict(Counter(token))
		WCD[doc] = count


def get_idf_dict():
	idf = {}
	size = len(WCD)
	for doc in WCD:
		for word in WCD[doc]:
			if word not in idf:
				idf[word] = 1
			else:
				idf[word] += 1
	for word,count in idf.items():
		idf[word] = log(size/count)
	return idf


def get_tf_idf_dict():
	idf = get_idf_dict()
	tf_idf = {}
	for doc in WCD:
		tf_count = WCD[doc]
		size = len(tf_count)
		for key,value in tf_count.items():
			tf = value / float(size)
			tf_count[key] = tf * idf[key]
		tf_idf[doc] = tf_count
	return tf_idf


def search_word(input_str):
	populate_WCD(doc_dict)
	input_str = p_stemmer.stem(input_str)
	tf_idf = get_tf_idf_dict()
	score_rank = {}
	for doc in tf_idf:
		if input_str in tf_idf[doc]:
			score_rank[doc] = tf_idf[doc][input_str]
	return {key: value for key, value in sorted(score_rank.items(), key=lambda item: item[1], reverse=True)}


print(search_word(input('enter the string')))

