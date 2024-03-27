def solution(s):
    intArray = list(map(int, s.split()))  # 문자열에서 정수 리스트로 변환
    answer = str(min(intArray)) + " " + str(max(intArray))

solution("1 2 3 -4")