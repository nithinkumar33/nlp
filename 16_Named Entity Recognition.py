import spacy
nlp = spacy.load("en_core_web_sm" )

doc = nlp("Apple is opening a new office in Chennai." )

for ent in doc.ents:
    print(ent.text, ent.label_)