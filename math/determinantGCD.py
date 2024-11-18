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

        #scalar * matrix
        if (isinstance(other, int)):
            b = other
            for i in range(n):
                for j in range(n):
                    res[i][j] = ((A[i][j] % mod) * (b % mod)) % mod

            return Matrix(res)

        #matrix * matrix
        B = other.M
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += A[i][k] * B[k][j]
        for i in range(n):
            for j in range(n):
                res[i][j] %= mod

        return Matrix(res)

    def __rmul__(self, other):
        return self * other

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

    def det(self):
        A = self.M
        n = len(A)

        if n == 1:
            return A[0][0]

        _sum = 0
        for k in range(n):
            res = [[0]*(n-1) for _ in range(n-1)]
            for i in range(n-1):
                r = 0
                for j in range(n):
                    if j != k:
                        res[i][r] = A[i+1][j]
                        r += 1
            _sum += Matrix(res).det() * A[0][k] * (-1) ** k
        return _sum

mod = int(1e9)+7
for n in range(1,10):
    M = [[0]*n for _ in range(n)]
    for i in range(n):
        M[i][i] = 1
    for i in range(n-1):
        M[i][i+1] = 1
    for i in range(1,n):
        M[i][i-1] = -1
    print(Matrix(M).det())


