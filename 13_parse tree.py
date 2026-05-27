import nltk

grammar = nltk.CFG.fromstring( """
S -> NP VP
NP -> 'I'
VP -> 'run'
""")

parser = nltk.ChartParser( grammar)

for tree in parser.parse("I run".split()):
    tree.pretty_print()