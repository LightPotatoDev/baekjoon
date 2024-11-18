winRate = [[0]*8 for _ in range(8)]
L = list(map(int,input().split()))
A = [-1,5,10,14,17,19,20,20]

for i in range(7):
    for j in range(i+1,8):
        winRate[i][j] = L[A[i]+j] / 100
        winRate[j][i] = 1 - L[A[i]+j] / 100

for row in winRate:
    print(row)