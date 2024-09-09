def solution(n):
    if int(n**(1/2)) == n**(1/2):
        print(int((n**(1/2)+1)**2))
    else:
        print(-1)

solution(121)