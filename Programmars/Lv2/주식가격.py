'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

'''
from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

def solution_with_queue(prices):
    answer = []
    q = deque(prices)
    
    while q:
        count = 0
        x = q.popleft()

        for i in q:
            if x <= i:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer



print(solution_with_queue([1, 2, 3, 2, 3]))
print(solution_with_queue([0, 0, 0, 0]))