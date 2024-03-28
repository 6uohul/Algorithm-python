def solution(n):
    answer = '수박'
    if n % 2 == 1:
        answer = answer * ((n-1)//2) + '수'
    else:
        answer = answer * (n // 2)
    return answer

solution(4)