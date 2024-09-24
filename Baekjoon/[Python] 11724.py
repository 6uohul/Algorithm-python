sys.setrecursionlimit(1000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def appendGraph():
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

appendGraph()

def solution():
    result = 0
    for i in range(1, n+1):
        if not visited[i]:
          dfs(i)
          result += 1
    return result

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

solution()