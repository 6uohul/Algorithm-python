'''
세준이는 N개의 빨대를 가지고 있다. N개의 빨대 중에 3개의 빨대를 선택했을 때,
이 빨대로 삼각형을 만들 수 있다면, 세 변의 길이의 합의 최댓값을 구하고 싶다.

입력
첫째 줄에 빨대의 개수 N이 주어진다.
N은 3보다 크거나 같고, 1,000,000보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 빨대의 길이가 한 줄에 하나씩 주어진다.
빨대의 길이는 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 삼각형 세 변의 길이의 합의 최댓값을 출력한다.
만약 삼각형을 만들 수 없으면 -1을 출력한다.
'''

import sys
input = sys.stdin.readline

N = int(input())
straws = []
for i in range(N):
    straws.append(int(input()))

straws.sort(reverse=True)

result = 0

for i in range(len(straws) - 2):
    if straws[i] < straws[i+1] + straws[i+2]:
        result = straws[i] + straws[i+1] + straws[i+2]
        break
    else:
        result = -1

print(result)
