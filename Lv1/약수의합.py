def solution(n):
    answer = 0
    i = 1
    while n >= i:
        if n == 0:
            answer = 0
        elif n % i == 0:
            answer += i
        i += 1
    print(answer)

solution(12)