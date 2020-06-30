def checkPerfectNumber(n):
    arr = []
    if n == 0:
        return False
    for i in range(1, n+1):
        uocSo = n % i
        if uocSo == 0:
            arr.append(i)
    return sum(arr)-n == n


print(checkPerfectNumber(6))
