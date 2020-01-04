from pymongo import MongoClient
# connects to: mongodb://127.0.0.1:27017/TestDB
client = MongoClient()            #by default it connects to port number 27017
db = client.TestDB