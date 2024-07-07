"""This approach will handle the string that contains both variables and parenthesis"""


def equation_validator(input_string):
    stack = []
    mapping = {"(": ")", "[": "]", "{": "}"}
    for i in input_string:
        if i in mapping.keys():
            stack.append(i)
        elif i in mapping.values():
            if stack and i == mapping[stack[-1]]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


s = "((3^2 + 8)*(5/2))/(2+6)"  # output - True
# s = ")([])" # output - false
print(equation_validator(s))

"""Another one method to solve the problem for only parenthesis and not any other variables in the equation"""


def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


b = is_valid_parentheses("({[]})")
print(b)

"""below are the sample inputs and their outputs"""
# Input: s = "()[]{}"
# Output: true
#
# Input: s = "({}[])"
# Output: true
#
# Input: s = ")]}{[("
# Output: false
#
# Input: s = "(]{{"
# Output: false


""" my code - This method counts the number of each type of parenthesis. 
 If for every type the counts of the openings and closings are equal, the parentheses are balanced. 
 This quick method fails with nested structures, but works for simple cases where nesting doesn’t occur. """

s = "({}[])"
l = list(s)
open_para = close_para = open_sq = close_sq = open_d = close_d = 0
for i in l:
    if i == '(':
        open_para += 1
    elif i == ')':
        close_para += 1
    elif i == '[':
        open_sq += 1
    elif i == ']':
        close_sq += 1
    elif i == '{':
        open_d += 1
    elif i == '}':
        close_d += 1

if (open_para == close_para) & (open_sq == close_sq) & (open_d == close_d):
    print('True')
else:
    print('False')
