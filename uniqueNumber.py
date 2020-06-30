from collections import Counter
def uniqueNumber(arr):
    counter = Counter(arr)
    result = [w for w in counter if counter[w] == 1]
    return result[0]
print(uniqueNumber([86, 51, 51, 72, 57, 57, 78, 78, 86]))