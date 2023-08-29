from math import comb, factorial

T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    allCase = (n-1)**n
    thatCase = comb(n,k) * factorial(k-1) * (n-1)**(n-k)
    print(thatCase / allCase)