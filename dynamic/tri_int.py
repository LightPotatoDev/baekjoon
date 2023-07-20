n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            L[i][j] += L[i-1][j]
        elif j == i:
            L[i][j] += L[i-1][j-1]
        else:
            L[i][j] += max(L[i-1][j-1],L[i-1][j])

print(max(L[n-1]))