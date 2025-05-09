from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range (N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

def bfs(V):
    q = deque([V])
    visited_bfs[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if graph[V][i] and not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True

def dfs(V):
    visited_dfs[V] = True
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited_dfs[i] and graph[V][i]:
            dfs(i)


dfs(V)
print()
bfs(V)