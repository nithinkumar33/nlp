import nltk

text = "The cat sits on the mat"
tokens = nltk.word_tokenize( text)
pos = nltk.pos_tag( tokens)

noun_phrases  = [word for word, tag in pos if tag.startswith( 'NN')]
print(noun_phrases )