# 프로그래머스 알고리즘 테스트 문제풀이
'''

평균 구하기
[문제 설명]
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

'''

def solution(arr):
    answer = 0
    sum = 0
    for i in arr:
        sum += i
    answer = sum / len(arr)
    print(answer)
    return answer

solution([1,2,3,4])