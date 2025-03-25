def max_sum(nums, k):
    current_sum = 0
    max_sum = float('-inf')

    for i in range(len(nums)):
        current_sum += nums[i]
        # 슬라이딩 윈도우를 움직여야하는 조건
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[i-(k-1)]
    return max_sum



print(max_sum([2,1,5,1,3,2], 3))