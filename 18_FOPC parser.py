def parse_fopc (expr):
    if "(" in expr and ")" in expr:
        predicate  = expr.split("(")[0]
        args = expr[expr.find("(")+1:expr.find(")")].split(",")
        return predicate , args
    return None

print(parse_fopc ("Loves(John,Mary)" ))