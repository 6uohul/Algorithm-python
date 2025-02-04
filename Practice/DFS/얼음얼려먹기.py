'''
Q1. 음료수 얼려 먹기
 N*M 크기의 얼음틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 
 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 
 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 갯수를 구하는 프로그램을 작성하시오. 

 * 입력 조건
- 첫째줄에 얼음 틀의 세로 길이 N과 가로길이 M이 주어진다.(1<= N,M <= 1000)
- 둘째줄부터 N+1번째 줄까지 얼음틀의 형태가 주어진다.
- 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

* 출력 조건
- 한번에 만들 수 있는 아이스크림의 갯수를 출력한다.

* 입력 예시
4 5
00110
00011
11111
00000

* 출력 예시
3
'''
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [1, -1, 0 , 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)  # 재귀 호출
            
        return True

    return False

count = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)