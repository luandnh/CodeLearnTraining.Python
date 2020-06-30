def minMaxOfSum(arr):
    arr.sort()
    return (2*sum(arr)-min(arr)-max(arr)) % 2147483647

print(minMaxOfSum([5,1,2,3,4]))