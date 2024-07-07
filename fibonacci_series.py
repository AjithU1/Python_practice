# Fibonacci series
n = int(input("Enter the no of terms \n"))
a = 0
b = 1
li = [a, b]
while n > 0:
    c = a + b
    a = b
    b = c
    li.append(c)
    n -= 1
print(li)

