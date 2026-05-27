import nltk

patterns  = [
    (r'.*ing$' , 'VBG'),
    (r'.*ed$' , 'VBD'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN')
]

tagger = nltk.RegexpTagger( patterns )
print(tagger.tag(["running" , "played" , "cats", "tree"]))