grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased" ]]
}

def parse(symbol, words):
    if symbol not in grammar:         return words[0] == symbol
    for rule in grammar[symbol]:
        if all(parse(r, [w]) for r, w in zip(rule, words)):
            return True
    return False

print(parse("NP", ["the", "cat"]))