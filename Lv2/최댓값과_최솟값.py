def solution(s):
    intArray = list(map(int, s.split()))  # 문자열에서 정수 리스트로 변환

    # 초기 최솟값과 최댓값을 설정합니다. 첫 번째 요소로 초기화합니다.
    minValue = maxValue = intArray[0]

    # 리스트를 순회하면서 최솟값과 최댓값을 찾음
    for num in intArray[1:]:
        if num < minValue:
            minValue = num
        elif num > maxValue:
            maxValue = num

    answer = str(minValue) + " " + str(maxValue)
    print(answer)

solution("1 2 3 -4")