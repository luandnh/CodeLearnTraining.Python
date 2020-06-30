def maxlength(n, A):
    result = 0
    arr = []
    for soBiChia in range(2, 10):
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[j] % soBiChia == 0:
                    arr.append(A[i:j+1])
                else:
                    break
    return max(len(x) for x in arr)
        
print(maxlength(5, [4, 6, 9, 12, 8]))
