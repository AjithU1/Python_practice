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
    
if __name__ == '__main__':
    N = int(input())
    a = []
    b_list = []
    for i in range(N):
        b = input().split()
        b_list.append(b)
    print(b_list)
    for b in b_list:
        if b[0] == 'insert':
            a.insert(int(b[1]), int(b[2]))
        if b[0] == 'print':
            print(a)
        if b[0] == 'remove':
            a.remove(int(b[1]))
        if b[0] == 'append':
            a.append(int(b[1]))
        if b[0] == 'sort':
            a.sort()
        if b[0] == 'pop':
            a.pop()
        if b[0] == 'reverse':
            a.reverse()
    print(a)


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
