def transform_tag (word, tag):
    if word.endswith( "ing"):
        return "VBG"
    return tag

print(transform_tag ("running" , "NN"))