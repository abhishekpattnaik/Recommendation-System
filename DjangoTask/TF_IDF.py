import math
from configurations import db
from constants import URL_DATA_COLLECTION, URL_DF_COLLECTION, URL_TF_IDF_COLLECTION

def get_def(giver_collection = URL_DATA_COLLECTION, taker_collection = URL_DF_COLLECTION):
	''' inserts the updated df into the taker_collection '''
	DF = {}
	print('Processing,Please wait')
	for elem in db[URL_DATA_COLLECTION].find(): 
	    for words in elem['word_count']: 
	        if words not in DF: 
	            DF[words]=1 
	        else: 
	            DF[words]=DF[words]+1 
	db[URL_DF_COLLECTION].drop()
	db[URL_DF_COLLECTION].insert_one(DF)
	print('Done')
	# return DF

# def sun_word_count(word_count_dict):
# 	pass


def get_TF_IDF():
	'''This will update the TF_IDF collections for each word '''
	url_list = []
	DF = dict(db[URL_DF_COLLECTION].find_one())
	doc_count = db[URL_DATA_COLLECTION].count()
	for url_obj in db[URL_DATA_COLLECTION].find():
		tf_idf=[]
		for key_obj,val_obj in url_obj['word_count'].items():
			# print(key_obj,val_obj)
			idf = math.log(doc_count/DF[key_obj])
			tf = val_obj/url_obj['Total words']
			tf_idf.append((key_obj, tf * idf))
			# print(idf)
		db[URL_TF_IDF_COLLECTION].insert_one({'url':url_obj['urls'], 'title':url_obj['title'], 'tf-idf count':tf_idf})
		# print(url_obj['urls'],'->',url_obj['Total words'])
		print(tf_idf)


get_TF_IDF()