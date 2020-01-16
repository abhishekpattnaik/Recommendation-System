from bs4 import BeautifulSoup
from recommend_app.scripts.constants import *
import requests
from recommend_app.scripts.configurations import db
from recommend_app.scripts.scrap_helper import get_domain, is_not_present
from tqdm import tqdm

def populate_raw_data():
    '''This will populate all the raw data picked up from hackernews.com and all the new contetnt will be updated'''
    print('populating in rawCollection...')
    for page_no in tqdm(range(1, 21)):
        res = requests.get('https://news.ycombinator.com/news?p='+str(page_no))
        soup=BeautifulSoup(res.text, 'html.parser')
        for tag_obj in soup.find_all('a', class_='storylink'):
            if is_not_present(tag_obj.attrs['href'], URL_COLLECTION_NAME) and 'http' in str(tag_obj.attrs['href']): 
                db[URL_COLLECTION_NAME].insert_one({'urls':tag_obj.attrs['href'], 'domain':get_domain(tag_obj.attrs['href']), 'status':False}) 
