n,m = map(int,input().split())
grid = [list(map(int,input())) for _ in range(n)]
dp_v = [[[0,0] for _ in range(m)] for _ in range(n)] #[i][j][l or r]

for j in range(m):
    dp_v[0][j][0] = grid[0][j]
    dp_v[0][j][1] = grid[0][j]

for i in range(1,n):
    for j in range(m):
        if grid[i][j] == 0:
            continue
        if j == 0:
            dp_v[i][j][0] = grid[i][j]
        else:
            dp_v[i][j][0] = dp_v[i-1][j-1][0] + 1
        if j == m-1:
            dp_v[i][j][1] = grid[i][j]
        else:
            dp_v[i][j][1] = dp_v[i-1][j+1][1] + 1

for i in range(n):
    for j in range(m):
        dp_v[i][j] = min(dp_v[i][j])

dp_w = [[[0,0] for _ in range(m)] for _ in range(n)] #[i][j][l or r]

for j in range(m):
    dp_w[n-1][j][0] = grid[n-1][j]
    dp_w[n-1][j][1] = grid[n-1][j]

for i in range(n-2,-1,-1):
    for j in range(m):
        if grid[i][j] == 0:
            continue
        if j == 0:
            dp_w[i][j][0] = grid[i][j]
        else:
            dp_w[i][j][0] = dp_w[i+1][j-1][0] + 1
        if j == m-1:
            dp_w[i][j][1] = grid[i][j]
        else:
            dp_w[i][j][1] = dp_w[i+1][j+1][1] + 1

for i in range(n):
    for j in range(m):
        dp_w[i][j] = min(dp_w[i][j])

def find_diamond(A,B):
    global ans
    i = 0
    j = 0
    n = len(A)
    for i in range(n):
        j = i+ans #size N diamond is found -> no need to find smaller ones
        for step in range(1+ans,A[i]+1):
            if j >= n:
                break
            if step <= B[j]:
                ans = max(step, ans)
            j += 1

ans = 0
for j in range(m):
    col1_1 = [dp_w[i][j] for i in range(0,n,2)]
    col1_2 = [dp_v[i][j] for i in range(0,n,2)]
    col2_1 = [dp_w[i][j] for i in range(1,n,2)]
    col2_2 = [dp_v[i][j] for i in range(1,n,2)]
    find_diamond(col1_1,col1_2)
    find_diamond(col2_1,col2_2)

print(ans)