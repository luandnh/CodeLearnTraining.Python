def number_move(a):
    strA = str(a)
    if strA[0:1]=="-":
        return int("-"+strA[2:]+strA[1:2])
    return int(strA[1:]+strA[0:1])
print(number_move(-2345))