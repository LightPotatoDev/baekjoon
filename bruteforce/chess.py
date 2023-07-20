n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(input())

def chesscheck(L):
    wrong = [0,0]
    target = ["BWBWBWBW","WBWBWBWB"]
    for first in range(2):
        for i in range(8):
            for j in range(8):
                if L[i][j] != target[i%2-first][j]:
                    wrong[first] += 1
    return wrong

wrongs = []

for j in range(m-7):
    for k in range(n-7):
        L = [i[j:j+8] for i in board[k:k+8]]
        wrongs.append(chesscheck(L))

print(min([min(r) for r in wrongs]))