'''
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 
컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
'''

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    
    def dfs(node):
        visited[node] = 1
        for adj_node in range(n):
            if visited[adj_node] == 0 and computers[node][adj_node] == 1:
                visited[adj_node] = 1
                dfs(adj_node)
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1

    return answer



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

print("------------------------------------------------------")


def solution_ver2(n, computers):
    result = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0:
            dfs(visited, i, computers)
            result += 1

    return result

def dfs(visited, index, graph):
    visited[index] = 1

    for adj_node in range(len(graph)):
        if visited[adj_node] == 0 and graph[index][adj_node] == 1:
            dfs(visited, adj_node, graph)

print(solution_ver2(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution_ver2(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))