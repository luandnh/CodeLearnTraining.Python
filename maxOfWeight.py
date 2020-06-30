from itertools import permutations


def maxOfWeight(weight, m):
    max_weight = -1
    arr_weight = list(permutations(weight, 3))
    for weight_check in arr_weight:
        sum_of_weight = sum(weight_check)
        if sum_of_weight > max_weight and sum_of_weight <= m:
            max_weight = sum_of_weight
    return max_weight


print(maxOfWeight([100,100,100,100], 290))
