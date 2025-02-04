'''

Q1. 미로 탈출
 동빈이는 N*M 크기의 직사각형 형태의 미로에 갇혀있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야한다.
 동빈이의 위치는 (1,1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한번에 한칸씩 이동할 수 있다. 
 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어있다. 
 미로는 반드시 탈출할 수 있는 형태로 제시된다. 
 이때 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하시오. 
 칸을 셀때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

* 입력 조건
- 첫째줄에 두 정수 N,M(4<= N,M <= 200)이 주어집니다. 
다음 N개의 줄에는 각각 M의 정수(0혹은 1)로 미로의 정보가 주어진다. 
각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.

* 출력 조건
- 첫째줄에 최소 이동 칸의 개수를 출력한다.

* 입력 예시
5 6
101010
111111
000001
111111
111111

* 출력 예시
10

'''

from collections import deque

N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]


q = deque([(0,0)])

while q:
    x, y = q.popleft()
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 벗어난 경우
        if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
            continue

        if graph[nx][ny] == 1:
            q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[N-1][M-1])