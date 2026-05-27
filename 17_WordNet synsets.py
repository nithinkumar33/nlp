from nltk.corpus import wordnet
import nltk
nltk.download( 'wordnet' )

synsets = wordnet.synsets( "bank")

for syn in synsets:
    print(syn.name(), "-", syn.definition())