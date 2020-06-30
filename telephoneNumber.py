def telephoneNumber(s):
    pos = 0
    if s.count("8") == 0:
        return "NO"
    pos = s.find("8") + 1
    if (len(s) - pos) +1 >= 11:
        return "YES"
    return "NO"

print(telephoneNumber("7818005553535"))
