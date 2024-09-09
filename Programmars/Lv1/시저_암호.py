#   A~Z 65~90
#   a~z 97~122
def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    answer = "".join(s)
    print(answer)
    return answer

solution("AB",1)
solution("a B z", 4)
solution("  a   b  c  Z", 1)