import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

# 유니온 파인드
N, M = int(input()), int(input())
parent = [i for i in range(N)]
for i in range(N):
    link = list(map(int, input().split()))
    for j in range(N):
        # 길이 있는 경우
        if link[j] == 1:
            union(i, j)

# 경로 체크
isValid = True
parent = [-1] + parent
path = list(map(int, input().split()))
start = parent[path[0]]
for i in range(1, M):
    if parent[path[i]] != start:
        print("NO")
        isValid = False
        break
if isValid:
    print("YES")