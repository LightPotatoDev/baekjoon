import sys
input = sys.stdin.readline

n,w = map(int,input().split())
Board = []

for _ in range(n):
    nick = input().rstrip()
    L = [""]*w*7 + ["X"]
    for i in range(7):
        row = list(input().rstrip())
        for j,x in enumerate(row):
            L[7*j+i] = x

    longest = 0
    lFreeze = int(1e8)
    lStart = int(1e8)
    failed = 0

    streak = 0
    freeze = 0
    start = 0
    for i,x in enumerate(L):
        if x == "O":
            if streak == 0:
                start = i
            streak += 1
        elif x == "F":
            freeze += 1
        elif x == "X":
            if streak > longest:
                longest = streak
                lFreeze = freeze
                lStart = start
            elif streak == longest:
                if freeze < lFreeze:
                    lFreeze = freeze
                    lStart = start
            streak = 0
            freeze = 0
            failed += 1

    Board.append([nick,longest,lFreeze,lStart,failed])

Board.sort(key = lambda x:(-x[1],x[2],x[3],x[4],x[0]))
place = 0
for i in range(n):
    if i >= 1 and all([Board[i-1][j]==Board[i][j] for j in range(1,5)]):
        pass
    else:
        place = i+1
    print(f"{place}. {Board[i]}")