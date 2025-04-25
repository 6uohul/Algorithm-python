from collections import deque

def solution(n, edge):

    graph = [[] for _ in range(n + 1)]

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    distance = [-1] * (n+1)
    distance[1] = 0

    q = deque([1])

    while q:
        x = q.popleft()
        for adj_node in graph[x]:
            if distance[adj_node] == -1:
                distance[adj_node] = distance[x] + 1
                q.append(adj_node)

    return distance.count(max(distance))

print(solution(8, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))