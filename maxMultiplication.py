from itertools import combinations
def maxMultiplication(a):
    arr = list(combinations(a,2))
    result = 0
    for numbers in arr:
        multi_numbers = numbers[0] * numbers[1]
        if result < multi_numbers:
            result=multi_numbers
    return result if result != 0 else -1
print(maxMultiplication([-2,5,0,0,-6]))