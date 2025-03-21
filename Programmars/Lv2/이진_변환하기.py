def solution(s):
    answer = []
    length = 0
    count = 0
    count_zero = 0

    while s != "1":

        length = 0

        # length
        for i in s:
            if i == "1":
                length += 1
            else:
                count_zero += 1
        
        # count 세기
        count += 1

        # 이진법으로 바꾸기
        s = format(int(length), 'b')
        
    return [count, count_zero]

print(solution("110010101001"))
