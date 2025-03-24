'''
문제 설명
자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.

x에 n을 더합니다
x에 2를 곱합니다.
x에 3을 곱합니다.
자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요.
이때 x를 y로 만들 수 없다면 -1을 return 해주세요.
'''

def solution(x, y, n):
    m = [10e9] * (y+1)
    m[x] = 0

    for i in range(x, y+1):
        # m[x] = 방문한적없는 경우 10e9인 경우엔 계속하기
        if m[x] == 10e9:
            continue
        # i+5 <= y 인경우
        if i+n <= y:
            m[i+n] = min(m[i+n], m[i]+1)
        # i*2 <= y
        if i*2 <= y:
            m[i*2] = min(m[i*2], m[i]+1)
        # i*3 <= y
        if i*3 <= y:
            m[i*3] = min(m[i*3], m[i]+1)
        # m[y] == 10e9인경우
    if m[y] == 10e9:
        m[y] = -1

    return m[y]

print(solution(2,5,4))


################################################

# BFS로 풀어보기

from collections import deque
 
def solution(x, y, n):
    visited = [0] * 1000001
 
    q = deque()
    q.append((x, 0))
    visited[x] = 1
    while q:
        num, cnt = q.popleft()
        if num == y:
            return cnt
        for next_num in (num + n, num * 2, num * 3):
            if next_num <= y and not visited[next_num]:
                visited[next_num] = 1
                q.append((next_num, cnt + 1))
 
    return -1