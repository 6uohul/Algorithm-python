'''
문제
양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 
최하위 비트(least significant bit, lsb)의 위치는 0이다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. (1 ≤ T ≤ 10, 1 ≤ n ≤ 106)

출력
각 테스트 케이스에 대해서, 1의 위치를 공백으로 구분해서 줄 하나에 출력한다. 위치가 낮은 것부터 출력한다.
'''


def binaryNum(n, list):
    a, b = divmod(n, 2)
    list.append(b)
    if a == 0:
        return list
    else:
        return binaryNum(a, list)

tc_num = int(input())
n = []

for i in range(tc_num):
    n.append(int(input()))

for i in range(tc_num):
    result = binaryNum(n[i], [])
    for j in range(len(result)):
        if result[j] == 1:
            print(j, end=" ")