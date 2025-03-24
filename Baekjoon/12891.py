'''
DNA 비밀번호

입력
첫 번째 줄에 민호가 임의로 만든 DNA 문자열 길이 |S|와 비밀번호로 사용할 부분문자열의 길이 |P| 가 주어진다. (1 ≤ |P| ≤ |S| ≤ 1,000,000)
두번 째 줄에는 민호가 임의로 만든 DNA 문자열이 주어진다.
세번 째 줄에는 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수가 공백을 구분으로 주어진다. 각각의 수는 |S| 보다 작거나 같은 음이 아닌 정수이며 총 합은 |S| 보다 작거나 같음이 보장된다.

출력
첫 번째 줄에 민호가 만들 수 있는 비밀번호의 종류의 수를 출력해라.
'''

from collections import deque

s, p = map(int, input().split())
string = list(str(input()))
A, C, G, T = map(int, input().split())

dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
left, right = 0, p-1
arr = deque(string[left:right])
for i in arr:
    dic[i] += 1
cnt = 0

while right < s:

    # 구간 완성
    dic[string[right]] += 1 # 가장 오른쪽 원소 추가

    # 계산
    if dic['A'] >= A  and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
        cnt += 1

    # 구간이동
    dic[string[left]] -= 1 # 가장 왼쪽 원소 제거
    left += 1
    right += 1

print(cnt)