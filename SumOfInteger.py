def sumOfInteger(n, x, y):
    total = 0
    for i in range(1, n+1):
        if (str(i).count(str(x)) >= 1) or (str(i).count(str(y)) >= 1):
            continue
        else:
            total +=i
    return total


print(sumOfInteger(10, 4, 5))
