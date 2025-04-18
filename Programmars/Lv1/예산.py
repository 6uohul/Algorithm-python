'''
'''

def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    print(budget)
    for i in d:
        budget -= i
        if budget < 0:
            break
        else:
            print(budget)
            answer += 1
    return answer

print(solution([1,3,2,5,4], 9))