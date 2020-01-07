import nltk
from collections import Counter
import string

def get_tokens(input_str):
	return nltk.word_tokenize(input_str.translate(None, string.punctuation))

if __name__ == "__main__":

	tokens = get_tokens()
	print("tokens[:20]=", tokens[:20])

	count = Counter(tokens)
	print("len(count) = ", len(count))
	print("most_common =", count.most_common(10))

	tagged = nltk.pos_tag(tokens)
	print("tagged[:20]=", tagged[:20])