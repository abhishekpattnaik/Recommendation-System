from string import punctuation
import requests
from bs4 import BeautifulSoup

from constants import URL_COLLECTION_NAME, URL_DATA_COLLECTION
from configurations import db
from helper import is_not_present

def remove_spec_char(in_str):
    '''This will remove all the special characters from the given string '''
    for spec_char in punctuation:
        in_str = in_str.replace(spec_char, '')
    return in_str


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


def agg_scrape():
    '''Still to be processed'''
    pass

    
def agg_main():
    '''This method triggers process '''
    domain_list = get_agg()
    for dom in domain_list:
        for url_obj in db[URL_COLLECTION_NAME].find({'domain':dom}):
            artilce_string = ''
            res = requests.get(url_obj['urls'])
            main_soup = BeautifulSoup(res.text, 'html.parser')
            if  is_not_present(url_obj['urls'], URL_DATA_COLLECTION):
                for elem in main_soup.find_all('p'):
                    artilce_string = artilce_string+elem.get_text()
                artilce_string = remove_spec_char(artilce_string)
                db[URL_DATA_COLLECTION].insert_one({'urls':url_obj['urls'], 'page artilce':artilce_string})
            else:
                print('Already Present')


# agg_main()
