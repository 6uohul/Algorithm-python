def solution(a, b):
    answer = 0
    if a > b:
        return sum(range(b, a+1))
    else:
        return sum(range(a, b+1))
    return sum
