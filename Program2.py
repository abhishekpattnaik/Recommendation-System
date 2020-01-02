from pymongo import MongoClient
client = MongoClient()
db = client.testdatabase
courses = db.courses
course = {
	'author':"balaji",
	'course':"MongoTutorial",
	'price':300,
	'rating':5
}
res = courses.insert_one(course)
print(res)