T = int(input())

def is_seat_possible(y,x):
    # <- -> checking
    if possible_seat_comb[x] == 0:
        return False

    #'x' checking
    seat = str(bin(x))[2:]
    for j in range(len(seat)):
        if grid[y][]

    # diagonal checking
    if y == 0:
        return True

    seat = str(bin(x))[2:]




for _ in range(T):
    n,m = map(int,input().split())
    grid = [input() for _ in range(n)]
    dp = [[0]*(1<<m) for _ in range(n)]

    possible_seat_comb = [[[1] * (1<<10)] for _ in range(n)]
for i in range(1<<10):
    seat = str(bin(i))[2:]
    for j in range(len(seat)):
        for d in [-1,1]:
            nj = j + d
            if not (0 <= nj < len(seat)):
                continue
            if seat[j] == '1' and seat[nj] == '1':
                possible_seats[i] = 0

    for j in range(1<<m):
        if is_seat_possible(0,j):
            dp[0][j] = j.bit_count()

    for i in range(1,n):
        for j in range(1<<m):


    for row in dp:
        print(row)
    print(max([max(row) for row in dp]))