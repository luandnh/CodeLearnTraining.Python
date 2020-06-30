def minSumOfTwoProducts(a,b):
    n  = a + b
    minSum = 10**7+9
    for x in range(0,9):
        for y in range(0,9):
            sum_a_b = a*x + b*y
            if sum_a_b < minSum and sum_a_b > n:
                minSum = sum_a_b
    return minSum

print(minSumOfTwoProducts(5,7))
#chua xong