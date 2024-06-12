# Reverse a number without built-in method
x = 1234564
y = 0
while x > 0:
    c = x % 10
    y = y * 10 + c
    x = x // 10
print(y)