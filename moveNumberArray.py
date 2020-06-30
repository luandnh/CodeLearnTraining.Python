def move_number_array(a):
    arrEven = []
    arrOdd = []
    for number in a:
        if number % 2 == 0:
            arrEven.append(number)
        else:
            arrOdd.append(number)
    return arrEven + arrOdd
print(move_number_array([2,0,3,5,6]))