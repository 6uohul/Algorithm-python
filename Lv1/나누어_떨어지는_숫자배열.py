def solution(arr, divisor):
    answer = []

    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    answer.sort()
    if len(answer) == 0:
        return [-1]
    else:
        return answer



solution([3,2,6],5)