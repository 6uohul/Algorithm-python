'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

from collections import deque

def coinChange(coins, amount):
    result = 0
    visited = [0 for i in range(amount)]
    if amount == 0: return 0

    q = deque([(0,0)])

    while q:
        num_of_coin, current_value = q.popleft()
        num_of_coin += 1

        for coin in coins:
            next_value = current_value + coin
            
            if next_value == amount:
                return num_of_coin
            
            elif next_value < amount:
                if visited[next_value] == 0:
                    visited[next_value] = 1
                    q.append((num_of_coin, next_value))

    return -1

print(coinChange([1,2,5], 11))
print(coinChange([1], 0))