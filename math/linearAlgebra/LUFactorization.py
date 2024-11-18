import sys
input = sys.stdin.readline

class Matrix:
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

    def row_swap(self,r1,r2):
        pass

    def row_sort(self):
        pass

    def row_echolon(self):
        pass

n = int(input())
A = Matrix([list(map(int,input().split())) for _ in range(n)])

for i in range(n-1):
    for j in range(i+1,n):
        Mat.row_add(i,j,-Mat.M[j][i]/Mat.M[i][i])

ans = [0]*n
for i in range(n-1,-1,-1):
    b = Mat.M[i][n]
    for j in range(i+1,n):
        b -= Mat.M[i][j]*ans[j]
    ans[i] = b / Mat.M[i][i]

for i in range(n):
    print(round(ans[i]), end=' ')