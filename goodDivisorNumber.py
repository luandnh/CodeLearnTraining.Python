def goodDivisorNumber(n):
    arr = []
    if n == 0:
        return False
    for i in range(1, n+1):
        uocSo = n % i
        if uocSo == 0:
            arr.append(i)
    arr.reverse()
    for i in range(0, len(arr)-1):
        sub_i = arr[i]-arr[i+1]
        if n % sub_i != 0:
            return False
    return True


print(goodDivisorNumber(10))
