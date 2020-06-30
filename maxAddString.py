def max_add_string(arr, k):
    i = 1
    arrStr = []
    result = ""
    while i <= k:
        maxNum = max(arr)
        arrStr.append(str(maxNum))
        arr.remove(maxNum)
        i += 1
    i = 1
    print(arrStr)
    while i <= k:
        maxStr = max(arrStr)
        result = result + maxStr
        arrStr.remove(maxStr)
        i += 1
    return result if int(result) != 0 else 0


print(max_add_string([253,269,968,226,785,408,316,642,626,113,255,210,978,853,162,43,753,261,297,997,267,354,741,902,350,120,228,288,609,522,799,415,694,399,89,75,344,973,50,288,663,886,744,296,34,35,238,882,31,987,827,848,294,70,417,382,897,553,195,384,898,636,807,0,207,673,458,424,588,933,898,357,882,899,126,866,942,814,446,288,254,683,511,746,725,255,809,606,842,714,63,183,63,39,18,8,409,852,441,305],13))
