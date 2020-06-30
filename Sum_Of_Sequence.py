def sum_of_sequence(n):
    total = 0
    for i in range(1, n+1):
        total += i*i
    return total
print(sum_of_sequence(5))
