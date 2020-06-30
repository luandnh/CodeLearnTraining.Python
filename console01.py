import re
def max_number_in_string(str):
    result = int(-1)
    tmp = re.findall(r'\d+',str)
    res = list(map(int,tmp))
    for x in res:
        if x > result:
            result = x
    return result

print(max_number_in_string("a123b4"))