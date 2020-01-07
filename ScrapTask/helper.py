'''This file is for all the required dependencies '''
import json
from urllib.parse import urlparse
from collections import Counter
import re
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from configurations import db

def remove_spec_char(input_str):
    '''This will remove all the special characters from the given string '''
    return re.sub('\W+', ' ', input_str)


def most_count_list(input_str):
    '''Returns the list of top ten repeated keywords '''
    input_str = remove_spec_char(input_str)
    tokens = nltk.word_tokenize(input_str)
    filtered = [w for w in tokens if not w in stopwords.words('english')]    
    count = Counter(filtered)
    return count.most_common(10)


def is_not_present(url, db_collection): 
    '''To check whether the url present in the corresponding database'''
    for items in db[db_collection].find({"urls":url}):
        return False
    return True


def is_url_present(url, db_collection):
    '''To check whether the url is present in the database or not '''
    for collection_obj in db[db_collection].find({}):
        if url in str(collection_obj["urls"]):
            return True
    return False


def article(url, url_id):
    '''To return a scraped dict according to the given url '''
    res = requests.get(url)
    main_soup = BeautifulSoup(res.text, 'html.parser')
    json_soup = BeautifulSoup(res.text, 'html.parser').find(type="application/ld+json")
    for element in json_soup:
        json_string = element
    data = json.loads(json_string)

    def full_article():
        '''To return full article of the medium page '''
        artilce_string = ''
        for elem in main_soup.find_all('p'):
            artilce_string = artilce_string+elem.get_text()
        return artilce_string

    def author():
        '''To return article's user name '''
        return data['author']['name']

    def description():
        '''To return the short description of the article '''
        return data['description']

    def headline():
        '''To return the headline of the article '''
        return data['headline']

    def article_type():
        '''To return the type of article  '''
        return data['@type']

    def claps():
        '''To return the number of claps of the article '''
        claps = str(0)        
        for elem in main_soup.find_all('button'):
            if 'claps' in elem.get_text():
                claps = elem.string
                break
        return str(claps)
    return {'author':author(), 'Headline':headline(), 'Description':description(), 'Type':article_type(), 'Claps':claps(), 'Full Article':full_article(), 'url':url, 'url_id':url_id}


def is_scrapped(demo_dict): 
    '''To check whether the dictionay is scrapped or not'''
    if demo_dict['status'] == False:
        return True
    return False


def check(user_input, url): 
    '''To check whether the domain is present in the url or not'''
    if user_input in url and url.count('http') == 1:
        return True
    return False


def get_domain(url):
    '''To get the domain name of the given article '''
    parsed_uri = urlparse(url)
    result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return result
