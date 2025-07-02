import nltk
from nltk import word_tokenize
from nltk.util import ngrams

sample_text = 'JUST LEAVE ME ALONE, I KNOW WHAT TO DO.'
tokens = word_tokenize(sample_text)

# Unigram
unigrams = list(ngrams(tokens, 1))
print ('Unigrams:', unigrams)

# Bigram
bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

# Trigram
trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)