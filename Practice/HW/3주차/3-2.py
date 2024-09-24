# 순열 생성하기
# 문제 설명:
#
# 주어진 정수 배열에서 모든 가능한 순열을 생성하는 프로그램을 작성하세요.
# 배열에는 중복된 숫자가 없다고 가정합니다.

def backtraking(num, path, visited):
    if len(path) == len(num):
        print(path)

    for i in range(len(num)):
        if not visited[i]:
            visited[i] = True
            backtraking(num, path + [num[i]], visited)
            visited[i] = False


def solution():
    num = list(map(int, input().split()))
    visited = [False] * len(num)
    backtraking(num, [], visited)


solution()