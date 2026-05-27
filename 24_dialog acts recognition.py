def dialog_act (sentence ):
    if sentence .endswith( "?"):
        return "Question"
    elif sentence .lower().startswith( "please" ):
        return "Request"      else:
        return "Statement"

print(dialog_act ("How are you?" ))