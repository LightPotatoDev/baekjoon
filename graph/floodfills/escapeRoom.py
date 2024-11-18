import sys
input = sys.stdin.readline
from collections import deque
from itertools import product

n = int(input())
m = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

primes = []
def sieve(n):
    is_prime = [1]*(n+1)
    for i in range(2,n+1):
        if is_prime[i] == 1:
            for j in range(i*2,n+1,i):
                is_prime[j] = 0
    primes = []
    for i in range(2,n+1):
        if is_prime[i] == 1:
            primes.append(i)

    return primes

def factorize(n):
    factor = dict()
    for p in primes:
        while n % p == 0:
            n //= p
            if p in factor:
                factor[p] += 1
            else:
                factor[p] = 1
        if n == 1:
            break
    return factor

def get_measure(n):
    factor = factorize(n)
    exp = factor.values()
    measures = []
    prod = product(*[list(range(e+1)) for e in exp])
    for p in prod:
        m = 1
        for i,k in enumerate(factor.keys()):
            m *= k ** p[i]
        measures.append(m)

    return measures

def coords(a):
    measures = get_measure(a)
    coords = []
    for y in measures:
        x = a // y
        if x <= m and y <= n:
            coords.append((y-1,x-1))

    return coords

primes = sieve(1000)
dq = deque([(0,0)])
visited[0][0] = 1
while dq:
    y,x = dq.popleft()
    for ny,nx in coords(grid[y][x]):
        if visited[ny][nx] == 0:
            visited[ny][nx] = 1
            dq.append((ny,nx))

print('yes' if visited[n-1][m-1] == 1 else 'no')
