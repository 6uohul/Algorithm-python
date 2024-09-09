def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        m = x * i
        answer.append(m)
    return answer

solution(-2,4)