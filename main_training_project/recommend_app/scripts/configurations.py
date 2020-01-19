'''
This will be used for connection with TestDB database of mongo 
    connects to: mongodb://127.0.0.1:27017/TestDB
    by default it connects to port number 27017
'''

from pymongo import MongoClient

client = MongoClient()            
db = client.TestDB
