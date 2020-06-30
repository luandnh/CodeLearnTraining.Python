def countSubarraySums(n,arr):
    result = 0
    for i in range(len(arr)):
        sum_total = 0
        for j in range(i,len(arr)):
            sum_total += arr[j]
            if sum_total == n:
                result += 1
    return result