def medianLine(a):
    if min(a) == 0 or min(a) == 1:
        return 0
    canh_huyen = max(a)
    a.remove(canh_huyen)
    sum_cgv = a[0]*a[0]+a[1]*a[1]
    if canh_huyen * canh_huyen != sum_cgv:
        return 0
    return float(canh_huyen /2)


print(medianLine([6,8,10]))
