s = 'HackerRank.com presents "Pythonist 2".'
res = ''
for i in s:
    if i.isupper():
        n = i.lower()
        res += n
    elif i.islower():
        n = i.upper()
        res += n
    else:
        res += i
print(res)

"""
def swap_case(s):
    res = ''
    for i in s:
        if i.isupper():
            n = i.lower()
            res += n
        elif i.islower():
            n = i.upper()
            res += n
        else:
            res += i
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
"""
