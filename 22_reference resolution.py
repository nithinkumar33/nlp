def resolve_reference (text):
    sentences  = text.split(".")
    if len(sentences ) > 1 and "He" in sentences [1]:
        return sentences [0].split()[ 0]
    return None

print(resolve_reference ("John went home. He slept." ))