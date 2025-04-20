'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
'''

def dailyTemperatures(temperatures):
    counter = {k: 0 for k in range(len(temperatures))} 
    stack = [0] # 첫번째 인덱스 저장
        
    for i in range(1,len(temperatures)):
        temp = temperatures[i]
        while True:
            cur_idx = stack.pop()
            cur_temp= temperatures[cur_idx]
            if cur_temp >= temp:
                print("cur_temp >= temp") # 아직 따뜻한 날 아님
                stack.append(cur_idx) # cur_temp 다시 push
                stack.append(i) # temp도 뒤이어 push
                print(stack)
                break # while loop 탈출 -> temp 변경
            else: # 탐색 성공
                counter[cur_idx] = i-cur_idx # counter 업데이트하는 부분을 수정
                if not stack: # when stack is empty
                    stack.append(i)
                    print("else -> append 후")
                    print(stack)
                    break
                                    
    while stack:
        counter[stack.pop()] = 0
        
    return list(counter.values())

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
# print(dailyTemperatures([30,40,50,60]))
# print(dailyTemperatures([30,60,90]))
# print(dailyTemperatures([1,2,3,4,3,2,1]))
