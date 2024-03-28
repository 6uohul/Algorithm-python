def solution(arr):
    result = []
    prev_element = None

    # 리스트를 순회하면서 중복을 제거합니다.
    for element in arr:
        if element != prev_element:
            result.append(element)
            prev_element = element

    return result


# 함수를 테스트합니다.
print(solution([1, 1, 3, 3, 0, 1, 1]))