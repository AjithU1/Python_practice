# ideas2IT
# program to create a child class inheriting parent class and accessing parent class method
class A:
    def method_a(self):
        print("Hello")


class B(A):
    def method_b(self):
        print("world")


ob = B()
ob.method_a()

#####################################

# calculate the sum of each student and sort the dict based on total marks of students in asc order
d = {
    "vijay": {"physics": 35, "chemistry": 45, "maths": 60},
    "ajith": {"physics": 38, "chemistry": 48, "maths": 63},
    "rakesh": {"physics": 36, "chemistry": 46, "maths": 61},
    "zivam": {"physics": 37, "chemistry": 47, "maths": 62}
}

# for student, marks in d.items():
#    print(marks.values())
total_marks = {student: sum(marks.values()) for student, marks in d.items()}

# Sort the dictionary based on total marks in ascending order

sorted_total_marks = dict(sorted(total_marks.items(), key=lambda item: item[1]))

# Print the sorted dictionary
print(sorted_total_marks)
