def solution():
    N, M = map(int, input().split(' '))
    ticket_nums = []
    for _ in range(0,N):
        ticket_nums.append(int(input()))

    for i in range(1, M + 1):
        for j in range(0, N - 1):
            if ticket_nums[j] % i > ticket_nums[j + 1] % i:
                ticket_nums[j], ticket_nums[j+1] = ticket_nums[j+1], ticket_nums[j]

    for ticket in ticket_nums:
        print(ticket)

solution()