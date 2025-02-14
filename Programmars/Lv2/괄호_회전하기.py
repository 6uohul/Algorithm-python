def solution(s):
    answer = 0
    s = list(s) ## list로 변환
    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        if len(stack) == 0:
            answer += 1
        s.append(s.pop(0))
    return answer

solution("[](){}")

'''
생각 못했던 점: s = s[1:] + s[0]를 하면 list로 바꿔주지 않아도 된다...!!!!!!
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
    return len(stack) == 0

def rotate(s):
    return s[1:] + s[:1]

def solution(s):
    count = 0
    for _ in range(len(s)):
        if is_valid(s):
            count += 1
        s = rotate(s)
    return count