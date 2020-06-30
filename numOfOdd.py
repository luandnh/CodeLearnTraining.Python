def numOfOdd(n, k):
    if k % 2 == 0:
        return 0
    if (n/k) % 2 == 0:
        return int((n/k)/2)
    return int(((n/k)+1)/2)

print(numOfOdd(11, 3))
