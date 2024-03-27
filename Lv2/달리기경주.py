def solution(players, callings):
    racing_dic = {player: index for index, player in enumerate(players)}
    for calling in callings:
        current_position = racing_dic[calling]
        player_to_swap = players[current_position - 1]

        players[current_position], players[current_position-1] = players[current_position-1], players[current_position]
        racing_dic[calling], racing_dic[player_to_swap] = current_position - 1, current_position
    return players

solution(["a","b","c"], ["b", "c", "c"])
