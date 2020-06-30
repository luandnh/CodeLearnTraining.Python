def charactersInString(n):
    strChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t = (n % (len(strChar))) - 1
    if t == -1:
        result = strChar[len(strChar) - 1]
    else:
        for i in range(len(strChar)):
            if i == n - 1 or i == t:
                result = strChar[i]
                break
    return result
print (charactersInString(23))
