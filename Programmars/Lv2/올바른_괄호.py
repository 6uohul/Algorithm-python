def solution(s):
    stack = []
    
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if "(" in stack:
                stack.remove("(")
    if len(stack) > 0:
        print("false")
        return False
    else:
        print("true")
        return True
   

solution("(()(")