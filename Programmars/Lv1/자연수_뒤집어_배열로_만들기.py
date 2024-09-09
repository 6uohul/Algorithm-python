def solution(n):

    n = str(n)[::-1] 
    answer = list(map(int, n))
    print(answer)
    return answer

solution(12345)