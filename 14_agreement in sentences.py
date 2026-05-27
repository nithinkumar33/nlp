def check_agreement (subject, verb):
    if subject == "he" and verb.endswith( "s"):
        return True
    return False

print(check_agreement ("he", "runs"))