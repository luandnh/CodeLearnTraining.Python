import itertools
def generate_binary(n):
    lst = list(map(list, itertools.product([0, 1], repeat=n)))
    result = []
    for binList in lst:
        s = [str(i) for i in binList]
        result.append("".join(s))
    return result
print(generate_binary(3))
