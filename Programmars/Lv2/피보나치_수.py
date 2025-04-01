'''
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
n은 2 이상 100,000 이하인 자연수입니다.
'''

def solution(n):
    answer = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        answer = solution(n-2) + solution(n-1)
    
    print(answer % 1234567)