from nltk.tokenize  import sent_tokenize

def coherence_score (text):
    sentences  = sent_tokenize (text)
    return len(sentences )

print(coherence_score ("This is a sentence. This is another one." ))