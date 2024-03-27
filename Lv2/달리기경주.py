def solution(players, callings):
    for c in callings:
        index = players.index(c)
        players[index], players[index - 1] = players[index - 1], players[index]

    print(players)
    return players

solution(["a","b","c"], ["b", "c", "c"])
