def code_to_digit(code):
    if code == "||:::":
        return 0
    elif code == ":::||":
        return 1
    elif code == "::|:|":
        return 2
    elif code == "::||:":
        return 3
    elif code == ":|::|":
        return 4
    elif code == ":|:|:":
        return 5
    elif code == ":||::":
        return 6
    elif code == "|:::|":
        return 7
    elif code == "|::|:":
        return 8
    elif code == "|:|::":
        return 9