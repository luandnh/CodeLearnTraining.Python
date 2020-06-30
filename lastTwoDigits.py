def lastTwoDigits(a,b):
    result = str(pow(a, b,100));
    if len(result) == 1:
        result = "0"+result
    return result