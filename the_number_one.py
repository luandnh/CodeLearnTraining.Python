def the_number_one(n):
    if n == 0:
        return True
    if n<=2:
        return False
    totalEven = 0
    totalOdd = 0
    for i in range(1, n+1):
        uocSo = n % i
        if uocSo == 0:
            print(i)
            if i % 2 == 0:
                totalEven += 1
            else:
                totalOdd += 1
    return totalEven == totalOdd
print(the_number_one(2))
