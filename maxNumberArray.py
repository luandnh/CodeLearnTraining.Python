def max_number_array(a):
    a.sort()
    check = False
    maxFind = a[len(a) - 1] - 1
    while check == False:
        if a.count(maxFind) >= 1:
            check = False
            maxFind -= 1
        else:
            check = True
    return maxFind

print(max_number_array([19,18,4,6]))
