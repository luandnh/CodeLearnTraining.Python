def factorial_calc(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    return n*factorial_calc(n-1)