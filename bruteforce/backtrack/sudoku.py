board = []
blanks = []

for i in range(9):
    line = list(map(int,input().split()))
    zeros = [j for j,x in enumerate(line) if x == 0]
    for j in zeros:
        blanks.append(9*i+j)
    board.append(line)

def placeable(index,n):
    y = blanks[index] // 9
    x = blanks[index] % 9

    for i in range(9):
        if board[i][x] == n or board[y][i] == n: #세로, 가로
            return False

    #정사각형 구간
    for i in range(3*(y//3), 3*(y//3)+3):
        for j in range(3*(x//3), 3*(x//3)+3):
            if board[i][j] == n:
                return False
    return True

def solve(index):

    if index == len(blanks):
        for i in board:
            print(' '.join(map(str,i)))
        exit(0)

    y = blanks[index] // 9
    x = blanks[index] % 9

    for n in range(1,10):
        if placeable(index,n):
            board[y][x] = n
            solve(index+1)
            board[y][x] = 0

solve(0)

""" by zmfhtmgjsej
arr = [list(map(int, input().split())) for _ in range(9)]
zeroIdx = []

for i in range(81) :
    if arr[i // 9][i % 9] == 0 : zeroIdx.append(i)

append zeros faster
"""