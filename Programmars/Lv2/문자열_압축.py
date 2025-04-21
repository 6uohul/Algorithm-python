def solution(s):
    n = len(s)
    min_length = n  # 최소 길이 저장

    for window_size in range(1, n//2 + 1):
        result = ""
        prev = s[0:window_size]
        count = 1

        for i in range(window_size, n, window_size):
            cur = s[i:i + window_size]
            if cur == prev:
                count += 1
            else:
                result += (str(count) + prev) if count > 1 else prev
                prev = cur
                count = 1

        result += (str(count) + prev) if count > 1 else prev

        min_length = min(min_length, len(result))
    return min_length

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
