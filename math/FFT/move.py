import cmath
import math

def FFT(p, inv):
    n = len(p)
    if n == 1:
        return p
    pe = [p[i] for i in range(0,n,2)]
    po = [p[i] for i in range(1,n,2)]
    ye, yo = FFT(pe,inv), FFT(po,inv)

    y = [0]*n
    w = cmath.exp(2j*cmath.pi/n)
    if inv:
        w = cmath.exp(-2j*cmath.pi/n)
    for i in range(n//2):
        y[i] = ye[i] + w**i * yo[i]
        y[i+n//2] = ye[i] - w**i * yo[i]

    return y

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


##n = int(input())
##A = list(map(int,input().split()))
##B = list(map(int,input().split()))
##print(polyMul(A,B))
print(polyMul([1,2,3,0],[0,1,1,1]))