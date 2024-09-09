def solution(s):
    answer = ''

    words = s.split(' ')

    for i in range(len(words)):
        words[i] = words[i].capitalize()

    answer = ' '.join(words)
    print(answer)
    return answer

solution(" a")
solution(" A")
solution("for the last week")