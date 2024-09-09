def solution(clothes):
    answer = 1 # 곱해야 하기 때문에 초기값을 1로 둠
    clothes_dic = {}
    for cloth in clothes:
        name, type = cloth
        if type not in clothes_dic: # 옷의 종류에 없는 경우
            clothes_dic[type] = 2   # 입지 않는 경우의 수도 더해서 2
        else :
            clothes_dic[type] += 1

    for count in clothes_dic.values():
        answer *= count
    print(answer -1)
    return answer - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])