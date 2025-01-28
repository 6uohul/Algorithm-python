from collections import deque

### 바이러스
### 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
### 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성

N = int(input())    # 컴퓨터 수
M = int(input())    # 연결된 컴퓨터 쌍의 수

graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(M):
    visited[M] = True
    for n in graph[M]:
        if visited[n] == False:
            dfs(n)

# dfs(1)
# print(sum(visited) - 1)

####### BFS #######

visited[1] = True  #1번 컴퓨터부터 시작이니까 True 표시
q = deque([1])
while q:
    v = q.popleft()
    for n in graph[v]:
        if visited[n] == False:
            q.append(n)
            visited[n] = True

print(sum(visited) - 1)