from collections import Counter


def find_team(arr, k):
    counter = Counter(arr)
    result = [w for w in counter if counter[w] == k]
    result.sort()
    return result


print(find_team([1, 2, 3, 4, 3, 2, 1, 3, 4, 4, 1], 3))
