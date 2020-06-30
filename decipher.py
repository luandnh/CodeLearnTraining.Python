def decipher(cipher):
    begin = 0
    result = ""
    while begin < len(cipher):
        subStr = cipher[begin: begin + 2]
        if int(subStr) <97:
            subStr = cipher[begin: begin + 3]
            begin += 3
        else:
            begin += 2
        result += chr(int(subStr))
    return result
print(decipher("10197115121"))
