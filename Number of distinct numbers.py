from collections import Counter
def number_of_distinct_numbers(a,b):
    result = []
    for b_i in b:
        num_of_distinct = len(Counter(a[b_i-1:]).values())
        result.append(num_of_distinct)
    return result

print(number_of_distinct_numbers([1,3,8,6,2,2,7],[4,2,6,3,4,4,6,2,7,4]))