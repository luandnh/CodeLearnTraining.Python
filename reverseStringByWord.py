def reverse_string_by_word(s):
    str = list(filter(None, s.strip().split(" ")))
    result = ''
    for i in reversed(str):
        result += i.strip() + " "
    return result.strip()


print(reverse_string_by_word(" code,    learn "))
