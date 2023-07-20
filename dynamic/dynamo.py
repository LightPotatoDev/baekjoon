n, m = map(int,input().split())

"""
def grid(x, y):
    if x==1 and y==1:
        return 1

    elif x == 1 and y > 1:
        return grid(x, y-1)
    elif x > 1 and y == 1:
        return grid(x-1, y)
    else:
        return grid(x-1,y-1) + grid(x-1,y) + grid(x,y-1)
"""

L = [[0]*m for _ in range(n)]
def grid(x,y):
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                L[i][j] = 1
            elif i == 0 and j > 0:
                L[i][j] = L[i][j-1]
            elif i > 0 and j == 0:
                L[i][j] = L[i-1][j]
            else:
                L[i][j] = L[i-1][j-1] + L[i-1][j] + L[i][j-1]

    return L[n-1][m-1]

print(grid(m,n)%1000000007)