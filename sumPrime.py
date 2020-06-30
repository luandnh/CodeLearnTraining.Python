def sumPrime(s):
    total = 0
    for i in range(len(s)):
        strCheck = ""
        for j in range(i, len(s)):
            strCheck = strCheck + s[j]
            if prime(int(strCheck)):
                total += int(strCheck)
    return total if sum != 0 else -1

def prime(x):
    if x > 1:
        for i in range(2, x + 1):
            if x % i == 0 and i != x and i != 1:
                return False
        else:
            return True
    else:
        return False


print(sumPrime("1234"))
