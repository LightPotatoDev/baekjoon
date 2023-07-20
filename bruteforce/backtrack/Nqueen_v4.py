n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

def placeable(board,y,x):
    queens = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queens.append([i,j])

    for q in queens:
        if y == q[0]: return False #세로
        if x == q[1]: return False #가로
        if y-x == q[0]-q[1]: return False #오른쪽 아래 대각선
        if y+x == q[0]+q[1]: return False #왼쪽 아래 대각선

    return True

def placequeen(board,y):
    global cnt

    if y == n:
        cnt += 1
        return

    for x in range(n):
        if placeable(board,y,x):
            board[y][x] = 1
            placequeen(board,y+1) #퀸을 배치하는 경우
            board[y][x] = 0 #backtrack

placequeen(board,0)
print(cnt)