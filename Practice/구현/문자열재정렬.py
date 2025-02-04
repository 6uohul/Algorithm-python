# Q2. 문자열 재정렬
# 알파멧 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

# 입력조건
# - 첫째줄에 하나의 문자열 s가 주어집니다,(1<=S의 길이<=10,000)

# 출력 조건
# - 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

# 입력 예시 : K1KA5CB7
# 출력 예시 : ABCKK13

import sys

input = input()
num = 0
result = []
for char in input:
    if char.isdigit():
        num += int(char)
    else:
        result.append(char)

result.sort()

if num != 0:
    result.append(str(num))
    
print("".join(result))