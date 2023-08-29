r,c,w = map(int,input().split())

tri = [[1],[1,1]]
for i in range(1,r+w-1):
    L = [1]
    for j in range(i):
        L.append(tri[i][j] + tri[i][j+1])
    L.append(1)
    tri.append(L)

s = 0
for i in range(w):
    s += sum(tri[r-1+i][c-1:c+i])
print(s)