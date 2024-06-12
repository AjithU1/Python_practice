"""
# namemain.py

print(__name__, type(__name__))
"""

# Python program to execute
# main directly
#print("practice", __name__)
"""
print("Hello")
def my_function():
    print("I am Ajith")
    print("practice_inside", __name__)


# class example
class SuperClass1:
    def info(self):
        print("Super Class 1 method called")


class SuperClass2:
    def info(self):
        print("Super Class 2 method called")


class Derived(SuperClass1, SuperClass2):
    pass


d1 = Derived()
d1.info()
"""

# Output: "Super Class 1 method called"
# file operations
f = open("AK.txt", "x")
list_d = ["hahaa\n", "Ajith kumar\n"]
f.write("I am not Indian\n")
f.writelines(list_d)
print(f)
f.close()
