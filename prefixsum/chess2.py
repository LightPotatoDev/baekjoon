import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = []

for _ in range(n):
    L = []
    for i in input().rstrip():
        if i == 'W': L.append(0)
        else: L.append(1)
    board.append(L)

board2 = [[] for _ in range(n)]
board3 = [[] for _ in range(n)]

for col,y in enumerate(board):
    for row, x in enumerate(y):
        board2[col].append((x-col%2-row%2)%2)

for col,y in enumerate(board):
    for row, x in enumerate(y):
        board3[col].append((x-col%2-row%2-1)%2)

def makePrefixsum(L):
    for i in range(0,n):
        for j in range(1,m):
            L[i][j] += L[i][j-1]
    for j in range(0,m):
        for i in range(1,n):
            L[i][j] += L[i-1][j]
    return L

def getPrefixsum(L,y1,x1,y2,x2):
    initial = L[y2][x2]
    minus1 = L[y1-1][x2] if y1 != 0 else 0
    minus2 = L[y2][x1-1] if x1 != 0 else 0
    dupe = L[y1-1][x1-1] if y1 != 0 and x1 != 0 else 0

    return initial - minus1 - minus2 + dupe

board2 = makePrefixsum(board2)
board3 = makePrefixsum(board3)

minRecolor = int(2e6)
for i in range(n-k+1):
    for j in range(m-k+1):
        minRecolor = min(minRecolor, getPrefixsum(board2, i, j, i+k-1, j+k-1))
        minRecolor = min(minRecolor, getPrefixsum(board3, i, j, i+k-1, j+k-1))

print(minRecolor)