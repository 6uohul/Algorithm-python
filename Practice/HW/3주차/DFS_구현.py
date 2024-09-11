def dfs_recursive(graph, node, visited):
    visited.append(node)

    # 인접한 노드
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(graph, adj, visited)

    return visited

# 먼저 들어간게 나중에 나오는게 스택
def dfs_stack(graph, start):
    visited = []

    # 방문해야하는 노드들의 목록
    stack = [start]

    while stack:
        node = stack.pop() # 방문해야하는 노드를 일단 꺼냄
        visited.append(node)

        for adj in graph[node]:
            if adj not in visited:
                dfs_stack(graph, adj)

    return  visited

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 두가지 방법 존재함
assert dfs_recursive(graph, 1, []) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert dfs_stack(graph, 1) == [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]

