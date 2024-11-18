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
        return '\n'.join(s) + '\n'

    def row_add(self,mul,targ,a):
        for i in range(self.m):
            self.M[targ][i] += a*self.M[mul][i]

    def row_swap(self,a,b):
        for i in range(self.m):
            self.M[a][i], self.M[b][i] = self.M[b][i], self.M[a][i]

SIZE = 8
m = int(input())
k = int(input())
grid = [list(map(lambda x:int(x)-m, input().split())) for _ in range(SIZE)]
mat = []

def same_rc(y,x):
    L = []
    for i in range(SIZE):
        for j in range(SIZE):
            if y == i or x == j:
                L.append(1)
            else:
                L.append(0)
    return L

for i in range(SIZE):
    for j in range(SIZE):
        L = same_rc(i,j)+[grid[i][j]]
        mat.append(L)
mat = Matrix(mat)

n = SIZE**2
for i in range(n-1):
    for j in range(i+1,n):
        sub = True
        for k in range(i+1,n):
            if mat.M[i][i] != 0:
                break
            if k == n-1:
                sub = False
            mat.row_swap(i,k)
        if sub == True:
            mat.row_add(i,j,-mat.M[j][i]/mat.M[i][i])

ans = [0]*n
for i in range(n-1,-1,-1):
    b = mat.M[i][n]
    for j in range(i+1,n):
        b -= mat.M[i][j]*ans[j]
    ans[i] = b / mat.M[i][i]

symbol = ['-', '.', '+']
for i in range(n):
    if i % SIZE == 0 and i != 0:
        print('')
    a = round(ans[i])
    print(symbol[a+1], end= ' ')