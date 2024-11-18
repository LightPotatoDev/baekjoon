import sys
input = sys.stdin.readline

class Matrix:
    def __init__(self,M):
        self.M = M

    def __repr__(self):
        s = []
        for i in self.M:
            s.append(' '.join(map(str,i)))
        return '\n'.join(s)

    def __add__(self,other):
        A = self.M
        B = other.M
        n = len(A)
        res = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                res[i][j] = (A[i][j] + B[i][j]) % mod

        return Matrix(res)

    def __sub__(self,other):
        A = self.M
        B = other.M
        n = len(A)
        res = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                res[i][j] = (A[i][j] - B[i][j]) % mod

        return Matrix(res)

    def __mul__(self,other):
        A = self.M
        B = other.M
        n = len(A)
        res = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += A[i][k] * B[k][j]

        for i in range(n):
            for j in range(n):
                res[i][j] %= mod

        return Matrix(res)

    def __pow__(self,p):
        A = self
        n = len(A.M)
        res = Matrix([[0]*n for _ in range(n)])
        for i in range(n):
            res.M[i][i] = 1

        while p:
            if p & 1:
                res = A*res
            A = A*A
            p >>= 1

        return res

    def __mod__(self,m):
        A = self.M
        for i in range(n):
            for j in range(n):
                A[i][j] %= m

        return Matrix(A)

def matrixExpSum(A,p):
    if p == 2:
        return A**2

    if p % 4 == 0:
        return matrixExpSum(A,p//2)*(I+A**(p//2))

    if p % 4 == 2:
        return matrixExpSum(A,p//2-1)*(I+A**(p//2-1)) + A**p

n = int(input())
mod = int(1e9)+7
A = Matrix([[1,1],[1,0]])
B = Matrix([[1,1],[1,0]])
I = Matrix([[0]*2 for _ in range(2)])
for i in range(2):
    I.M[i][i] = 1

if n == 1:
    print(0)
    exit(0)

if n%2 == 1:
    n -= 1

print(matrixExpSum(A,n).M[0][1] % mod)

