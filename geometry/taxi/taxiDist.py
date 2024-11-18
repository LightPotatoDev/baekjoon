n,m = map(int,input().split())
ones = []
for i in range(n):
    row = list(map(int,input().split()))
    for j,x in enumerate(row):
        if x == 1:
            ones.append([i,j])

x1,y1 = ones[0]
x2,y2 = ones[1]
print(abs(x1-x2) + abs(y1-y2))