T = int(input())

def is_seat_possible_init(i,j,m):
    seat = str(bin(j))[2:].zfill(m)
    seat = seat[::-1]
    for k in range(m):
        if grid[i][k] == 'x' and seat[k] == '1':
            return 0
        for d in [-1,1]:
            nk = k + d
            if not (0 <= nk < m):
                continue
            if seat[k] == '1' and seat[nk] == '1':
                return 0
    return 1

def is_seat_possible_dp(i,j,k,m):
    seat_front = str(bin(k))[2:].zfill(m)
    seat_back = str(bin(j))[2:].zfill(m)

    for l in range(m):
        for d in [-1,1]:
            nl = l + d
            if not (0 <= nl < m):
                continue
            if seat_back[l] == '1' and seat_front[nl] == '1':
                return 0
    return 1

for _ in range(T):
    n,m = map(int,input().split())
    grid = [input() for _ in range(n)]
    dp = [[0]*(1<<m) for _ in range(n)]

    possible_seat_comb = [[0] * (1<<m) for _ in range(n)]
    for i in range(n):
        for j in range(1<<m):
            possible_seat_comb[i][j] = is_seat_possible_init(i,j,m)

    for j in range(1<<m):
        if possible_seat_comb[0][j] == 1:
            dp[0][j] = j.bit_count()

    for i in range(1,n):
        for j in range(1<<m):
            if possible_seat_comb[i][j] == 0:
                continue
            for k in range(1<<m):
                if possible_seat_comb[i-1][k] == 0:
                    continue
                if is_seat_possible_dp(i,j,k,m) == 1:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + j.bit_count())

    print(max([max(row) for row in dp]))