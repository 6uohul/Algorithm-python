def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, i, visited)

graph =[
  [], # 노드번호가 1부터 시작하기 때문에 인덱스 0은 비워둔다
  [2,3,8], # 1번 노드와 인접한 노드 2,3,8
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9
dfs(graph, 1, visited)