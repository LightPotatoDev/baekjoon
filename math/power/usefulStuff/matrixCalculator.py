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
                res[i][j] = (A[i][j] + B[i][j])

        return Matrix(res)

    def __sub__(self,other):
        A = self.M
        B = other.M
        n = len(A)
        res = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                res[i][j] = (A[i][j] - B[i][j])

        return Matrix(res)

    def __mul__(self,other):
        A = self.M
        n = len(A)
        res = [[0]*n for _ in range(n)]

        if isinstance(other, int) or isinstance(other,float):
            B = other
            for i in range(n):
                for j in range(n):
                    res[i][j] = (A[i][j] * B)
            return Matrix(res)

        B = other.M

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += A[i][k] * B[k][j]

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

A = Matrix([[5,3],
            [3,2]])
B = Matrix([[-1,3],
            [3,-4]])
C = Matrix([[4,-2],
            [-6,3]])
X = Matrix([[2,-4],
            [-3,6]])
print(X*A+C)
