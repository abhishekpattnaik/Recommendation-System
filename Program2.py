from pymongo import MongoClient
client = MongoClient()
db = client.testdatabase
courses = db.courses
x = int(input("please enter the no of times"))
for i in range(x):
	a=input("Author")
	c=input("course")
	p=input("price")
	r=input("rating")
	course = {
		'author':a,
		'course':c,
		'price':p,
		'rating':r
	}
	res = courses.insert_one(course)
	print(res)
	aAuthor=author()
aHeadline=headline()
aDescription=description()
aType=articleType()
aClaps=claps()
arcticleDict={'Author':aAuthor,'Headline':aHeadline,'Description':aDescription,'Type':aType,'claps':aClaps}
print(arcticleDict)