import requests
from bs4 import BeautifulSoup
from constants import URL_COLLECTION_NAME, URL_DATA_COLLECTION
from configurations import db
from helper import is_not_present, remove_spec_char, most_count_list



def get_agg():
    '''This will sort top ten domains according to the frequency'''
    domain_list = []
    count = 1
    for num in db[URL_COLLECTION_NAME].aggregate([{"$group":{'_id':"$domain", 'count':{'$sum':1}}}, {'$sort':{"count":-1}}]):
        domain_list.append(num['_id'])
        count += 1
        if count>10:
            break 
    return domain_list


def agg_scrape(url_obj):
    '''This method scrapes the given url '''
    artilce_string = ''
    res = requests.get(url_obj)
    main_soup = BeautifulSoup(res.text, 'html.parser')
    for elem in main_soup.find_all('div'):
        for text in elem.find_all('p'):
            artilce_string = artilce_string+text.get_text()
    artilce_string = remove_spec_char(artilce_string)
    return artilce_string


def agg_main():
    '''This method triggers process '''
    print('Processing.')
    domain_list = get_agg()
    for dom in domain_list:
        for url_obj in db[URL_COLLECTION_NAME].find({'domain':dom}):
            req_url=url_obj['urls']
            if is_not_present(url_obj['urls'], URL_DATA_COLLECTION):
                artilce_string = agg_scrape(req_url)
                mcl = most_count_list(artilce_string)
                db[URL_DATA_COLLECTION].insert_one({'urls':url_obj['urls'], 'page artilce':artilce_string, 'word_count':mcl})
                print(mcl)
agg_main()