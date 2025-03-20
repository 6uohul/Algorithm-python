def solution(n, m, x, y, queries):
    sr, sc, er, ec = x, y, x, y
    for d, dx in reversed(queries):
        if d == 0:  # 왼쪽으로 이동
            if sc == 0: # 제일 왼쪽에 있으면
                ec = min(m-1, ec+dx)
            else:   # 제일 왼쪽X
                if sc + dx > m-1: return 0
                sc = min(sc+dx, m-1)
                ec = min(ec+dx, m-1)
        elif d == 1: # 오른쪽으로 이동
            if ec == m-1 :  # 제일 오른쪽에 있는 경우
                sc = max(0, sc-dx)
            else:
                if ec - dx < 0: return 0
                sc = max(sc-dx, 0)
                ec = max(ec-dx, 0)
        elif d == 2:    # 위로 이동
            if sr == 0:
                er = min(n-1, er+dx)
            else:
                if sr + dx > n-1 : return 0
                sr = min(sr+dx, n-1)
                er = min(er+dx, n-1)
        else:   # 아래로 이동
            if er == n-1:
                sr = max(0, sr-dx)
            else:   # 중간에 있는 경우
                if er - dx < 0: return 0
                sr = max(0, sr-dx)
                er = max(0, er-dx)

    return (er-sr+1)*(ec-sc+1)

print(solution(2,5,0,1,[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))