### 토마토 BFS

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        # 익은 토마토 상하좌우 돌면서 일수 저장하기
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] =  graph[x][y] + 1
                q.append([nx, ny])

ans = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
        
    ans = max(ans, max(line))

print(ans - 1)