def restore_ip_address(s):
    begin = 0
    while begin < len(s):
        subStr = s[begin : begin + 2]
        if int(subStr) < 255:
            subStr = s[begin: begin + 3]
            begin += 3
        else:
            begin += 2
        print(subStr)
restore_ip_address("25525511135")