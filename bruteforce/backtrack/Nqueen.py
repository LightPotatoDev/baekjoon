n = int(input())
chessboard = [[0 for _ in range(n)] for _ in range(n)]
state = [0 for _ in range(n**2)]
cnt = 0

def blockplacing(L,y,x):
    for i in range(n):
        L[y][i] = 1
    for i in range(n):
        L[i][x] = 1

    i = y - min([y,x])
    j = x - min([y,x])
    while i < n and j < n:
        L[i][j] = 1
        i += 1
        j += 1

    i = y - min([y,n-x-1])
    j = x + min([y,n-x-1])
    while i < n and j > 0:
        L[i][j] = 1
        i += 1
        j -= 1

    L[y][x] = 2
    return L


def placequeen(L,num,place):
    global cnt

    if place >= n**2:
        return

    if num >= n:
        cnt += 1
        for k in L:
            print(k)
        print('')
        return

    spot = [place//n,place%n]
    state[place] = L[:]

    if L[spot[0]][spot[1]] == 0:
        L = blockplacing(L,spot[0],spot[1])
        placequeen(L,num+1,place+1) #퀸을 배치하는 경우

    L = state[place][:]
    L[spot[0]][spot[1]] = 1
    placequeen(L,num,place+1) #퀸을 배치하지 않는 경우

placequeen(chessboard,0,0)
print(cnt)