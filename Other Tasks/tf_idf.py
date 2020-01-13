from math import log
from re import sub
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from collections import Counter
from constants import WORD_COUNT_DICT as WCD
from constants import INVERSE_DOCUMENT_FREQUENCY as IDF 
from constants import TF_IDF
from configurations import db
from pandas import DataFrame 
from sklearn.metrics.pairwise import cosine_similarity


p_stemmer = SnowballStemmer("english")
# doc_dict = {'docA' : "The car is driven on the road.",'docB' : "The truck is driven on the highway."}

def populate_WCD(db_collection='url_data'):
	'''initializes the  WORD_COUNT_DICT by filtering and tokenizing'''
	flag = 0
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
		print(flag)
		# if flag == 10:
		# 	break
		flag += 1


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

def all_values():
	for url_obj in db['tf-idf'].find():
		WCD.update(url_obj['WCD'])
		IDF.update(url_obj['IDF'])
		TF_IDF.update(url_obj['TF-IDF'])

	# print(type(TF_IDF))

# def main():
# 	update_db()
# # 	all_values()
# 	print(WCD)
# # 	input_str = input('enter the string')
# # 	d = search_word(input_str)
# # 	for uid in d:
# # 		print(WCD[uid]['url'],'=',WCD[uid]['count'][input_str])


def main():
	# update_db()
	all_values()
	# print(WCD)
	input_str = 'how are you doing tonight artificial intelligence is crazy' 
	token = word_tokenize(input_str)
	# token = word_tokenize(input('enter the string'))
	temp_dict = {}
	token = [p_stemmer.stem(w) for w in token if not w in stopwords.words('english')]
	for elem in token:
		temp_dict[elem] = search_word(elem)
	df = DataFrame(temp_dict).fillna(0)
	# print(df.values)
	df = df.sum(axis=1).sort_values(ascending=False)
	uid_dict=dict(df)
	final_dict={}
	# uid_list=[]
	for uid in uid_dict:
		final_dict[WCD[uid]['title']]=WCD[uid]['url']
	for uid in final_dict:
		print(final_dict[uid])
	# print(final_dict)


if __name__ == '__main__':
	main()