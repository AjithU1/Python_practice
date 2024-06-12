"""string = input().strip()
sub_string = input().strip()
a = []
for i in range(len(string)):
    b = string.find(sub_string, i, len(string))
    print(b)
    if b != -1 and b not in a:
        a.append(b)
        print(a)
print(len(a))
"""

"""
def count_substring(string, sub_string):
    a = []
    for i in range(len(string)):
        b = string.find(sub_string, i, len(string))
        if b != -1 and b not in a:
            a.append(b)

    return len(a)



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
"""

if __name__ == '__main__':
    s = input()
    ls = m = n = o = p = False
    for i in s:
        if i.isalnum():
            ls = True
        if i.isalpha():
            m = True
        if i.isdigit():
            n = True
        if i.islower():
            o = True
        if i.isupper():
            p = True
    print(f"{ls}\n{m}\n{n}\n{o}\n{p}")