# count the number of constants in the given word
def constant_count():
    input_str = input("Enter any string: \n")
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in input_str:
        if i not in vowels:
            count += 1
    return count


result = constant_count()
print("The number of constants is: ", result)
