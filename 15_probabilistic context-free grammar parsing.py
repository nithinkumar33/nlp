import nltk
 grammar = nltk.PCFG.fromstring( """
S -> NP VP [1.0]
NP -> 'she' [1.0]
VP -> 'runs' [1.0]
""")

parser = nltk.ViterbiParser( grammar)

for tree in parser.parse("she runs" .split()):
    print(tree)