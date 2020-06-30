def convert_number_max(n):
    str_n = list(map(int,str(n)))
    print(str_n)
    min_n = min(str_n)
    max_n = max(str_n)
    i_of_min = str(n).find(str(min_n))
    if i_of_min == 0:
        str_n[i_of_min] = max_n
        return int("".join(map(str,str_n)))
    else:
        for i in range(0,len(str_n)-1):
            if int(str_n[i]) == max_n:
                continue
            elif  int(str_n[i]) < max_n:
                str_n[i] = max_n
                break
    return int("".join(map(str,str_n)))
print(convert_number_max(3525))