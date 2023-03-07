result_str = ""
    in_run = False
    for i in range(n):
        if in_run and (i == n-1 or values[i] != values[i+1]):
            result_str += ") "
            in_run = False
        if not in_run and i < n-1 and values[i] == values[i+1]:
            result_str += "( "
            in_run = True
        result_str += str(values[i]) + " "
    if in_run:
        result_str += ")"