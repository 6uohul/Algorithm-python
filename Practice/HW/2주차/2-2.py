# 주어진 문자열에서 중복 문자가 없는 가장 긴 부분 문자열의 길이를 찾는 문제입니다.
# 이 문제를 해결하기 위해 해시테이블을 사용하여 문자의 위치를 추적합니다.
#
# 요구 조건:
# 문자열에 포함된 모든 문자에 대해 최근 위치를 저장하는 해시테이블을 사용합니다.
# 중복된 문자가 발견될 때, 부분 문자열의 시작 위치를 업데이트합니다.
# 중복되지 않는 가장 긴 부분 문자열의 최대 길이를 반환합니다.

def length_of_longest_substring(s: str) -> int:
    # 문자와 해당 문자의 위치를 저장할 딕셔너리
    char_index_map = {}
    start = 0
    max_length = 0

    for index in range(len(s)):
        current_char = s[index]

        if current_char in char_index_map and char_index_map[current_char] >= start:
            start = char_index_map[current_char] + 1

        char_index_map[current_char] = index

        max_length = max(max_length, index - start + 1)

    print(max_length)

length_of_longest_substring("abcacdbe")