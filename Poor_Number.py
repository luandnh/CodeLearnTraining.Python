def poorNumber(n):
    arr = []
    for i in range(1, n+1):
        uocSo = n % i
        if uocSo == 0 and n != i:
            arr.append(i)
    return sum(arr) < n

print(poorNumber(4))
