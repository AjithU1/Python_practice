"""
l = ["a", 5, "a123", 6, "bc23"]
alpha = alnum = num = 0

for i in l:
    s = str(i)  # Convert the item to string first
    if s.isalpha():
        alpha += 1
    elif s.isdigit():
        num += 1
    elif s.isalnum():
        alnum += 1
    else:
        num += 1  # This line will never be executed due to above conditions

print(f"alphabets: {alpha}, alphanum: {alnum}, numbers: {num}")
"""
v = "a5a1236bc23"
alpha = num = 0
for s in v:
    if s.isalpha():
        alpha += 1
    elif s.isdigit():
        num += 1
    else:
        num += 1
print(f"alphabets: {alpha}, numbers: {num}")