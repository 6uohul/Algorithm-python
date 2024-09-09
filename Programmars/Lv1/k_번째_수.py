def solution(array, commands):
    result = []
    for command in commands:
        start, end, select = command
        result.append(sorted(array[start - 1:end])[select - 1])
    return result


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])