T = int(input())

def fibo(n,zero,one):
    if n == 0:
        return zero, one
    return fibo(n-1, one, zero+one)


for i in range(T):
    result = fibo(int(input()),1,0)
    print(' '.join(map(str,result)))