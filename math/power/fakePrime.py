import sys
input = sys.stdin.readline

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

while True:
    p,a = map(int,input().split())
    if p == 0:
        break

    if isPrime(p):
        print('no')
        continue

    if pow(a,p,p) == a:
        print('yes')
    else:
        print('no')