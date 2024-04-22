def solution():
    N = int(input())
    box = list(map(int, input().split(' ')))
    dp = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if box[i] > box[j]: # 뒤에 상자가 더 큰 경우
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))

solution()