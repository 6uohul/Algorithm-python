'''
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
n은 2 이상 100,000 이하인 자연수입니다.
'''

def solution(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-2] + dp[i-1])
    return dp[-1] % 1234567


print(solution(5))