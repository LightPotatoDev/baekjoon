L = [list(map(int,input().split())) for _ in range(9)]
x,y = 0,0
maxV = 0

for i in range(9):
    for j in range(9):
        if L[i][j] > maxV:
            maxV = L[i][j]
            x,y = i,j

print(maxV)
print(x+1,y+1)