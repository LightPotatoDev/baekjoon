import sys
input = sys.stdin.readline
from math import gcd

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

T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    mod = int(1e9)+7
    A = Matrix([[1,1],[1,0]])
    g = gcd(n,m)

    print(((A**g).M[0][1]) % mod)