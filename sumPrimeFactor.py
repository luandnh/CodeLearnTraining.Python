def sum_prime_factor(n):
    if n == 0:
        return -1
    if n<=2:
        return -1
    result = 0
    for i in range(1, n+1):
        uocSo = n % i
        if uocSo == 0 and prime(i):
                result += i
    return result

def prime(x):
    if x > 1:
        for i in range(2, x + 1):
            if x % i == 0 and i != x and i != 1:
                return False
        else:
            return True
    else:
        return False

print(sum_prime_factor(30))