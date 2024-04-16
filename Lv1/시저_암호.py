#   A~Z 65~90
#   a~z 97~122
def solution(s, n):
    answer = ''
    array = list(s)
    for i in range(0,len(array)):
        if array[i] != " ":
            ordNum = ord(array[i])
            if ordNum <= 90: # 대문자인 경우
                if ordNum + n > 90:
                    ordNum += n - 26
                    array[i] = array[i].replace(array[i], chr(ordNum))
                    continue
                array[i] = array[i].replace(array[i], chr(ordNum + n))
            else:   # 소문자인 경우
                if ordNum + n > 122:
                    ordNum += n - 26
                    array[i] = array[i].replace(array[i], chr(ordNum))
                    continue
                array[i] = array[i].replace(array[i], chr(ordNum + n))
    answer = "".join(array)
    print(answer)
    return answer

solution("AB",1)
solution("a B z", 4)
solution("  a   b  c  Z", 1)