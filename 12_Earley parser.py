import nltk

grammar = nltk.CFG.fromstring( """
S -> NP VP
NP -> 'she'
VP -> 'runs'
""")

parser = nltk.EarleyChartParser( grammar)
sentence  = "she runs" .split()

for tree in parser.parse(sentence ):
    print(tree)