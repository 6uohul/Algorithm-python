# BFS 사용, 모든 노드를 방문하는 것이 아니기 때문에 시간 적게 소요됨
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
			
            # if문 하나에서 여러 조건을 확인하는 것 보다 아래처럼 쪼개는 것이 속도가 빠름
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1: 
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return

bfs(0, 0)