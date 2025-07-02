import nltk

# Ladataan tarvittavat NLTK-resurssit
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    print("Ladataan punkt_tab tokenizer...")
    nltk.download('punkt_tab')

sample_text = 'I am learning Generativa AI'
tokens = nltk.word_tokenize(sample_text.lower())

print('Tokens:', tokens)