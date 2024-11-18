T = int(input())

def place_mines(M):

    def check_nearby_mines(i):
        mines = 0
        for j in [-1,0,1]:
            if 0 <= i+j < n and M[i+j] == '*':
                mines += 1
        return mines

    if check_nearby_mines(0) > hint[0]:
        return -1

    for i in range(n):
        if i+1 < n and check_nearby_mines(i) < hint[i]:
            M[i+1] = '*'

    if check_nearby_mines(n-1) == hint[n-1]:
        return M.count('*')
    else:
        return -1

for _ in range(T):
    n = int(input())
    hint = list(map(int,input()))
    tile = list(input())

    tile1 = tile[:]
    tile2 = tile[:]
    tile2[0] = '*'

    print(max(place_mines(tile1),place_mines(tile2)))