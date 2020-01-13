from math import log
from re import sub
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from collections import Counter
from constants import WORD_COUNT_DICT as WCD


p_stemmer = SnowballStemmer("english")

doc1 = 'When I published the article “Understanding Blockchain” many of you wrote me to ask me if I could make one dedicated to Artificial Intelligence. The truth is that I hadn’t had time to get on with it and before sharing anything, I wanted to finish some courses in order to add value to the recommendations.The problem with Artificial Intelligence is that it’s much more fragmented, both technologically and in use cases, than Blockchain, making it a real challenge to condense all the information and share it meaningfully. Likewise, I have tried to make an effort in the summary of key concepts and in the compilation of interesting sources and resources, I hope it helps you as well as it did to me!'
doc2 = 'The way Stefan got an idea to write an article about natural language processing is simple — every once in a while he would stumble across a good article and save bits and pieces here and there.Once he decided to accumulate these thoughts and put them in o ne place — that worked out as an ultimated NLP guide. In this 23-minute read, the author managed to put enough insights and wisdom, that someone could write a book based on this post.The article describes the possible applications, challenges, and work mechanisms of natural language processing. It might not be an “easy” read — your head feels “stuffed” after you are done, but it’s definitely t he one you’ll always come back to.'
doc3 = 'Goroutines are otherwise normal functions that Go executes concurrently. We could write an entire article digging into how Goroutines work under the hood, but at a high level, Goroutines are lightweight threads managed automatically by the Go runtime. Many Goroutines can fit on a single OS thread, and if a Goroutine blocks an OS thread, the Go runtime automatically moves the rest of the Goroutines over to a new OS thread.Goroutines also offer a feature called “channels,” which allow Goroutines to pass messages between themselves, allowing us to schedule requests and prevent race conditions.Implementing all of this functionality in Python may be doable with recent tools like asyncio, but the fact that Go is designed with this use case in mind makes our lives much easier.'
doc4 = 'The final note I’ll make on why we ultimately built Cortex in Go is that Go is just nice.Relative to Python, Go is a bit more painful to get started with. Go’s unforgiving nature, however, is what makes it such a joy for large projects. We still heavily test our software, but static typing and compilation — two things that make Go a bit less comfortable for beginners — act as sort of guard rails for us, helping us to write (relatively) bug-free code.There may be other languages you could argue offer a particular advantage, but on balance, Go best satisfies our technical and aesthetic needs.'
doc5 = 'We still love Python, and it has its place within Cortex, specifically around inference processing.Cortex serves TensorFlow, PyTorch, scikit-learn, and other Python models, which means that interfacing with the models—as well as pre and post inference processing—are done in Python. However, even that Python code is packaged up into Docker containers, which are orchestrated by code that is written in Go.If you’re interested in becoming a machine learning engineer, knowing Python is more or less non-negotiable. If you’re interested in working on machine learning infrastructure, however, you should seriously consider using Go.'

doc_dict = {'doc1':doc1,'doc2':doc2,'doc3':doc3,'doc4':doc4,'doc5':doc5}
# doc_dict = {'docA' : "The car is driven on the road.",'docB' : "The truck is driven on the highway."}

def populate_WCD(doc_dict):
	'''initializes the  WORD_COUNT_DICT by filtering and tokenizing'''
	for doc in doc_dict:
		doc_str = doc_dict[doc].lower()
		doc_str = sub('\W+', ' ', doc_str)
		doc_dict[doc] = doc_str
		token = word_tokenize(doc_dict[doc])
		token = [p_stemmer.stem(w) for w in token if not w in stopwords.words('english')]
		count = dict(Counter(token))
		WCD[doc] = count


def get_idf_dict():
	idf = {}
	size = len(WCD)
	for doc in WCD:
		for word in WCD[doc]:
			if word not in idf:
				idf[word] = 1
			else:
				idf[word] += 1
	for word,count in idf.items():
		idf[word] = log(size/count)
	return idf


def get_tf_idf_dict():
	idf = get_idf_dict()
	tf_idf = {}
	for doc in WCD:
		tf_count = WCD[doc]
		size = len(tf_count)
		for key,value in tf_count.items():
			tf = value / float(size)
			tf_count[key] = tf * idf[key]
		tf_idf[doc] = tf_count
	return tf_idf


def search_word(input_str):
	populate_WCD(doc_dict)
	input_str = p_stemmer.stem(input_str)
	tf_idf = get_tf_idf_dict()
	score_rank = {}
	for doc in tf_idf:
		if input_str in tf_idf[doc]:
			score_rank[doc] = tf_idf[doc][input_str]
	return {key: value for key, value in sorted(score_rank.items(), key=lambda item: item[1], reverse=True)}


print(search_word(input('enter the string')))



''' 


def get_tf_dict():
	tf_dict = {}
	for doc in WCD:
		tf_count = WCD[doc]
		size = len(tf_count)
		for key,value in tf_count.items():
			tf = value / float(size)
			tf_count[key] = tf
		tf_dict[doc] = tf_count
	return tf_dict


'''