# reverse a string
# output: "ramuK tijA"
s = "Ajit Kumar"
rev_str = ""
for i in s:
    rev_str = i + rev_str
print(rev_str)

# reverse a list using for loop
s = ['ajith', 'kumar']
# output "Kumar Ajith"

for i in range(len(s) - 1, -1, -1):
    print(i)
    print(s[i])

# program to reverse the words in a sentence in the same order
# output: "Ajith Afternoon Good"
a = "Good Afternoon Ajith"
b = a.split()
print(b)
b.reverse()
s = " ".join(b)
print(s)
