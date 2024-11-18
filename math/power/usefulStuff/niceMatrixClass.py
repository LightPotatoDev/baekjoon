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
        n = len(A)
        res = [[0]*n for _ in range(n)]

        if isinstance(other, int):
            B = other
            for i in range(n):
                for j in range(n):
                    res[i][j] = (A[i][j] * B) % mod
            return Matrix(res)

        B = other.M

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += A[i][k] * B[k][j]

        for i in range(n):
            for j in range(n):
                res[i][j] %= mod

        return Matrix(res)

    def __rmul__(self,other):
        return other * self

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

E3 = Matrix([[1,0,0],
            [0,1,0],
            [0,1,1]])
E2 = Matrix([[1,0,0],
            [0,1,0],
            [0,-2,1]])
E1 = Matrix([[1,0,0],
            [-3,1,0],
            [0,0,1]])
A = Matrix([[2,1,1],
            [6,4,5],
            [4,1,3]])
mod = int(1e9)
print(E1*E2*E3*A)
