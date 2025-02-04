'''
곱하기 혹은 더하기
각 자리가 숫자로만 이루어진 문자열 S가 주어질 때, 
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'X'또는 '+'연산자를 넣어 만들 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, 일반적인 사칙연산 방식 이아닌, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

*입력 조건
- 첫째줄에 여러개의 숫자로 구성된 하나의 문자열 S가 주어집니다.(1<=S의길이<=20)

*출력 조건
- 첫째줄에 만들 수 있는 가장 큰수를 출력합니다.
'''

input = list(map(int, input()))
result = 0

for i in input:
    if i > 1 and result > 1:
        result *= i
    else :
        result += i

print(result)