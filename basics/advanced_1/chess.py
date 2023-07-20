req = (1,1,2,2,2,8)
chessNum = list(map(int,input().split()))
L = [0]*6

for i in range(6):
    L[i] = req[i] - chessNum[i]

print(' '.join(map(str,L)))