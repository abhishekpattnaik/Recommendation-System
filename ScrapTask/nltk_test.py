import nltk
from collections import Counter
import string

def get_tokens():
	with open('/home/abhishek/Dev/assignmentsADC/trainingADC/ScrapTask/Pearl3.txt') as pearl:
		tokens = nltk.word_tokenize(pearl.read().translate(None, string.punctuation))
	return tokens

if __name__ == "__main__":

	tokens = get_tokens()
	print("tokens[:20]=", tokens[:20])

	count = Counter(tokens)
	print("len(count) = ", len(count))
	print("most_common =", count.most_common(10))

	tagged = nltk.pos_tag(tokens)
	print("tagged[:20]=", tagged[:20])