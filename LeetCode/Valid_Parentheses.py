'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

'''
stack이 비어있거나 
'''

def is_valid(s):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in pair.values():
            stack.append(char)
        elif char in pair:
            if not stack or pair[char] != stack.pop():
                return False

    if stack:
        return False      
    return True

print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([])"))
print(is_valid("["))
print(is_valid("]"))