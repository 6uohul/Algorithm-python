# 미로 탈출 결로 찾기

from collections import deque

def miro_bfs(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    N, M = len(grid), len(grid[0])

    # 방문할 곳을 저장
    q = deque([(0, 0)])
    grid[0][0] = 1  # 거리

    while q:
        x, y = q.popleft()

        if x == N - 1 and y == M - 1:
            print(grid[x][y])


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx, ny))

    print(grid)


grid=[
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

miro_bfs(grid)

