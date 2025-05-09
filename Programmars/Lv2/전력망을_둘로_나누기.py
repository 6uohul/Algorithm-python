def DFS(start, graph, visited, check_link):
    cnt = 1
    visited[start] = True  # 일단 v 노드는 방문함
    for adj_v in graph[start]:  # v에 연결 되어있는 다른 노드
        if visited[adj_v] == False and check_link[start][adj_v]:  # 인접한 연결되어 있는 노드가 방문한 적없고
            cnt += DFS(adj_v, graph, visited, check_link)
    return cnt  # 인접 연결 노드들 다 카운트


def solution(n, wires):
    answer = float("inf")

    check_link = [[True] * (n + 1) for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]  # 송전탑 그래프

    # 그래프 채우기
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [False] * (n + 1)
        check_link[a][b] = False
        cnt_a = DFS(a, graph, visited, check_link)  # 그때 a랑 붙어 있는 송전탑 개수
        cnt_b = DFS(b, graph, visited, check_link)  # 그때 b랑 붙어 있는 송전탑 개수
        check_link[a][b] = True

        answer = min(answer, abs(cnt_a - cnt_b))

    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
print(solution(n, wires))