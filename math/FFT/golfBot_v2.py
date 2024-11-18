import cmath
import math

def FFTSwap(p):
    n = len(p)
    i = n
    p2 = [0]*n
    while i > 0:
        for j in range(n//i):
            for k in range(i):
                p2[k//2 + int(k%2==1)*(i>>1) + i*j] = p[k+i*j]

        p = p2[:]
        i >>= 1
    return p


def FFT(p, inv):
    n = len(p)
    i = n//2
    p = FFTSwap(p)

    while i > 0:
        s = n//i
        w = cmath.exp(2j*cmath.pi/s)
        if inv:
            w = cmath.exp(-2j*cmath.pi/s)
        for j in range(i):
            off = j*s
            pe = [p[k] for k in range(off, off+s//2)]
            po = [p[k] for k in range(off+s//2, off+s)]
            for k in range(s//2):
                p[k + off] = pe[k] + w**k * po[k]
                p[k + off + s//2] = pe[k] - w**k * po[k]
        i >>= 1

    return p

def polyMul(A,B):
    #zero padding -> n = 2**m
    n = 2**math.ceil(math.log2(len(A)+len(B)))
    for i in range(n-len(A)):
        A.append(0)
    for i in range(n-len(B)):
        B.append(0)

    #do polyMul using FFT
    va,vb = FFT(A,False), FFT(B,False)
    V = [va[i]*vb[i] for i in range(n)]
    res = FFT(V,True)
    for i in range(len(res)):
        res[i] = 1/n*res[i]
    resInt = [round(res[i].real) for i in range(n)]
    return resInt

n = int(input())
A = [0]*(200001)
for _ in range(n):
    A[int(input())] = 1

B = polyMul(A,A)

ans = 0
m = int(input())
for _ in range(m):
    i = int(input())
    if A[i] >= 1 or B[i] >= 1:
        ans += 1
print(ans)