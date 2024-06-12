"""
# file operations
f = open("Ajit.txt", "w")
list_d = ["AK\n", "Ajit\n"]
f.write("I am an Indian\n")
f.writelines(list_d)
f.close()

# file read
c = open("Ajith.txt", 'r')
a = c.readlines()
print(a)
c.close()

# Using open() function
file_path = "new_file.txt"

# Open the file in write mode
with open(file_path, 'w') as file:

    file.write("Hello, this is a new text file created using open() function.")

print(f"File '{file_path}' created successfully.")



# class example
class Dog:
    # class attribute
    att1 = "mammal"

    # instance attribute
    def __init__(self, name):
        self.name = name


ob1 = Dog("Ajit")
ob2 = Dog("karthik")

# instance attribute
print(f"My name is {ob1.name}")
print(f"My name is {ob2.name}")
# class attribute
print(f"My char is {Dog.att1}")  # one way to access class attr
print(f"My origin is {ob1.__class__.att1}")  # second way to access class attr
print(f"My native is {ob2.__class__.att1}")


# 'self' parameter example


def distance(x, y):
    print(x + y)


class Point:
    pass


distance(5,5)
"""
