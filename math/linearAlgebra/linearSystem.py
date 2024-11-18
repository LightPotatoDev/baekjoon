import sys
input = sys.stdin.readline

class matrix:
    def __init__(self,M):
        self.M = M
        self.n = len(M)
        self.m = len(M[0])

    def __repr__(self):
        s = []
        for i in self.M:
            s.append(' '.join(map(str,i)))
        return '\n'.join(s)

    def row_add(self,mul,targ,a):
        for i in range(self.m):
            self.M[targ][i] += a*self.M[mul][i]

n = int(input())
mat = matrix([list(map(int,input().split())) for _ in range(n)])

for i in range(n-1):
    for j in range(i+1,n):
        if mat.M[i][i] != 0:
            mat.row_add(i,j,-mat.M[j][i]/mat.M[i][i])

ans = [0]*n
for i in range(n-1,-1,-1):
    b = mat.M[i][n]
    for j in range(i+1,n):
        b -= mat.M[i][j]*ans[j]
    ans[i] = b / mat.M[i][i]

for i in range(n):
    print(round(ans[i]), end=' ')