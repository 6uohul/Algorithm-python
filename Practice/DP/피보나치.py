# 1, 1, 2, 3
# 단순 재귀함수 코드

def fib(x):
    if x == 1 or x == 2:
        return 1
    return fib(x-1) + fib(x-2)
    
print(fib(4))

##################################

# 탑다운

d = [0] * 100
def fib(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:   #이미 방문한 적이 있는 경우
        return d[x]
    d[x] = fib(x-1) + fib(x-2)
    return d[x]

print(fib(4))

##################################

# 바텀업
# 작은 것 -> 큰 것

nd = [0] * 100
d[1] = 1
d[2] = 1
n = 99
def bottomUp_fib(x):
    for i in range(3, n + 1):
        d[i] = d[i-1] + d[i-2]
    
    print(d[n])

print(bottomUp_fib(99))