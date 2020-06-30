def isSubsequence(s,t):
    if len(s) == 0 and len(t) ==0:
        return True
    elif len(s) == 0 or len(t) == 0:
        return False
    arrChar = []
    for character in s:
        if t.count(character) == 0:
            return False
        for i in range(0,len(t)):
            if character == t[i]:
                arrChar.append([character,i])
    for i in range(0,len(arrChar)):
        for j in range(i,len(arrChar)):
            if arrChar[i][1] > arrChar[j][1]:
                return False
    return True
print(isSubsequence("axc","ahbgdc"))