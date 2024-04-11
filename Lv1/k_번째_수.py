def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        start_index = commands[i][0]
        end_index = commands[i][1]
        select_index = commands[i][2]
        new_array = array[start_index-1:end_index]
        new_array = sorted(new_array)
        answer.append(new_array[select_index-1])
    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])