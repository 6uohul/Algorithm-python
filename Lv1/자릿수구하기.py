def solution(n):
    answer = 0
    while n != 0 :
        answer  = answer + n % 10
        n //= 10
    print(answer)

solution(123)