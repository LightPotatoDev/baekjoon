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

T = int(input())
for _ in range(T):
    L = [list(map(int,input().split())) for _ in range(3)]
    A1 = Matrix([[L[i][j] for j in [3,1,2]] for i in range(3)])
    A2 = Matrix([[L[i][j] for j in [0,3,2]] for i in range(3)])
    A3 = Matrix([[L[i][j] for j in [0,1,3]] for i in range(3)])
    A = Matrix([[L[i][j] for j in [0,1,2]] for i in range(3)])

    dets = [A1.det(),A2.det(),A3.det(),A.det()]
    print(*dets)
    if dets[3] == 0:
        print("No unique solution")
    else:
        print("Unique solution: ",end='')
        for i in range(3):
            x = dets[i]/dets[3]
            if not (-0.0005 < x < 0.0005):
                print('{:.3f}'.format(round(x, 3)), end=' ')
            else:
                print('0.000', end=' ')
        print('')
    print('')