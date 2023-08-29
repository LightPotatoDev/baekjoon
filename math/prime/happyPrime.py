import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def sangen(n):
    while True:
        if n == 1:
            return True
        elif n == 4:
            return False

        digits = [n // 10**i % 10 for i in range(int(math.log10(n))+1)]
        n = 0
        for i in digits:
            n += i**2

T = int(input())
for _ in range(T):
    t,x = map(int,input().split())
    result = ""
    if isPrime(x) and sangen(x):
        result = "YES"
    else:
        result = "NO"
    print(t,x,result)