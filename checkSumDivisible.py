def check_sum_divisible(n):
    arr = [int(i) for i in n]
    total = sum(arr)
    n = list(set(n))
    for i in n:
        if total % int(i) != 0:
            return False
    return True
print(check_sum_divisible("77183285"))