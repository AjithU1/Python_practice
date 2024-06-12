"""
l = [1, 0, 2, 11, 4, 1, 1, 9, 3, 2, 1, 1]
n = []
for i in l:
    if i not in n:
        n.append(i)
print(n)
"""
s = "The sun is the biggest star present in the milky way galaxy"
ls = s.split()

# list comprehension method
v = [i[::-1] if i in 'the' or i in 'The' else i for i in ls]
print(v)

# traditional iteration
n = []
for i in ls:
    if i == 'the' or i == 'The':
        b = i[::-1]
        n.append(b)
    else:
        n.append(i)
print(n)

# 'n' or 'v' can be used with 'join' for the output
n = " ".join(n)
print(n)


