def solution(s):
    stack = []
    
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) > 0:
        print("f")
        return False
    else:
        print("t")
        return True
   

solution("(()(")