def solution(lottos, win_nums):
    answer = []
    count = 0
    zero_count = 0

    for num in lottos:
        if num in win_nums:
            count += 1
    zero_count = lottos.count(0)
    print(count, zero_count)
    answer.append(checkLevel(count + zero_count))
    answer.append(checkLevel(count))  # 현재 레벨
    print(answer)
    return answer

def checkLevel(count):
    level = 0
    if count == 0 or count == 1:
        level = 6
    if count == 2:
        level = 5
    if count == 3:
        level = 4
    if count == 4:
        level = 3
    if count == 5:
        level = 2
    if count == 6:
        level = 1
    return level

solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])