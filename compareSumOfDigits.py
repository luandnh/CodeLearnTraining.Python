def compareSumOfDigits(input):
    totalEven = totalOdd = 0
    for i in range(len(input)):
        num = int(input[i])
        if num % 2 == 0:
            totalEven += num
        else:
            totalOdd += num
    return totalOdd - totalEven
print(compareSumOfDigits("012345"))
