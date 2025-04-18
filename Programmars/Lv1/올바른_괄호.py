def solution(s):
    '''
    스택으로 (는 넣고, )가 들어온 경우 stack에 (가 있으면 ( pop
    '''

    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) > 0:
        return False
    else:
        return True
