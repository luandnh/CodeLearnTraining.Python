def sum_aB(a, b):
    if a > b:
        return 0
    if a == b:
        return a
    if a < 0:
        if abs(a) > b:
            return (a-b-1)*(abs(a)-b)/2
        if abs(a) < b:
            return (b+abs(a)+1)*(b-abs(a))/2
        if abs(a) == b:
            return 0
    else:
        return (b+a)*(b-a+1)/2


print(sum_aB(1, 10**9))
