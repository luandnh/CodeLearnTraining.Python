def equalString(a, b, c):
    ListA = list(a)
    ListB = list(b)
    ListC = list(c)
    lenght= len(ListA)
    for i in range(lenght):
        if ListA[i] == ListB[i]:
            continue
        elif ListA[i] != ListB[i]:
            if ListA[i] == ListC[i]:
                tmp = ListB[i]
                ListB[i] = ListC[i]
                ListC[i] = tmp
            else:
                tmp = ListA[i]
                ListA[i] = ListC[i]
                ListC[i] = tmp
    return ListA == ListB


print(equalString("vyglmujgkmsp","sjmvklmuypgg","jluygmkgpmvs"))
