# reverse a string
s = "Ajit Kumar"
rev_str = ""
for i in s:
    rev_str = i + rev_str
print(rev_str)

l = ['A','J', 'I', 'T', 'H']
rev_l = []
for i in range(len(l)-1, -1, -1):
    print(i)
    rev_l.append(l[i])

print(l, rev_l)

i_l = []
for i in range(len(l)):
    i_l.insert(0, l[i])
print(i_l)


# program to reverse the words in a sentence in the same order
# output: "Ajith Afternoon Good"
a = "Good Afternoon Ajith"
b = a.split()
print(b)
b.reverse()
s = " ".join(b)
print(s)
