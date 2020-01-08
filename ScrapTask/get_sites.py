from configurations import db
from constants import URL_DATA_COLLECTION
def get_urls(user_str):
	cursor_object = db[URL_DATA_COLLECTION].find()
	url_data_list = []
	url_list = []
	for elem in cursor_object:
		url_data_list.append(elem)
	for url_dict in url_data_list: 
	     for wc in url_dict['word_count'].keys(): 
	         if user_str == wc: 
	            url_list.append(url_dict['urls']) 
	return(url_list)
print(get_urls('artificial'))