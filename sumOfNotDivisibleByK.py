def sumOfNotDivisibleByK(n, k):
    total = 0
    if n == 0 or k == 1:
        return 0
    elif k > n:
        return n*(n+1)/2
    for i in range(1, n+1):
        if (i % k) != 0:
            total += i
    return total


print(sumOfNotDivisibleByK(3, 2))
