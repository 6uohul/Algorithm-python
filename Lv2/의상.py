def solution(clothes):
    answer = 1 # 곱해야 하기 때문에 초기값을 1로 둠
    clothes_dic = {}
    for cloth in clothes:
        name, type = cloth
        if type not in clothes_dic:
            clothes_dic[type] = 0
        clothes_dic[type] += 1

    for count in clothes_dic.values():
        answer *= count + 1

    return answer - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])