def messageFromBinaryCode(code):
    result = ""
    for i in range(0, len(code), 8):
        temp_data = code[i:i+8]
        decimal_data = int(temp_data, 2)
        result = result + chr(decimal_data)
    return result
print(messageFromBinaryCode('010010000110010101101100011011000110111100100001'))
