# program to divide the list of elements by a common divisor and sort the list elements based on their
# remainders in asc order
# note for same reminders ex: 7 and 22 will have reminders as 2, in that case based on asc sorting,
# append 7 first followed by 22
divisor = 5
list1 = [7, 15, 14, 13, 11, 23, 22]
d = {}
list2 = []
for i in list1:
    c = i % divisor
    d[i] = c
    list2.append(c)
# print(d.items())
list2.sort()
# print(list2)
new = sorted(d.items(), key=lambda x: x[1])
# print(new)
s = dict(new)
print(list(s.keys()))
