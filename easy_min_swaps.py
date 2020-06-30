def easy_min_swaps(arr):
    arr_dup = arr.copy()
    result = 0
    for i in range(0, len(arr)):
        min_arr = min(arr_dup)
        if arr[i] == min_arr:
            arr_dup.remove(min_arr)
            continue
        for j in range(i, len(arr)):
            if arr[j] == min_arr:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                result += 1
                arr_dup.remove(min_arr)
                break
    return result
print(easy_min_swaps([1,3,5,2,4,6,7]))
