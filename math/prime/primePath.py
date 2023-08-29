import sys
input = sys.stdin.readline
from collections import deque

def sieve(n):
    p = 2
    isPrime = [1] * (n+1)
    for i in range(2,int(n**0.5)+1):
        if isPrime[i]:
            for j in range(i**2, n+1, i):
                isPrime[j] = 0

    isPrime[0],isPrime[1] = 0,0
    return isPrime
P = sieve(9999)

def addGraph(n):
    N = list(str(n))
    for i in range(4):
        A = N[:]
        for j in range(10):
            A[i] = str(j)
            p = int(''.join(A))
            if p >= 1000 and p != n and P[p] == 1:
                graph[n].append(p)

graph = [[] for _ in range(10000)]
for i in range(1000,10000):
    if P[i] == 1:
        addGraph(i)

T = int(input())

for _ in range(T):
    a,b = map(int,input().split())
    visited = [0]*10000
    visited[a] = 1
    dq = deque([a])

    while dq:
        p = dq.popleft()

        for i in graph[p]:
            if visited[i] == 0:
                visited[i] = visited[p]+1
                dq.append(i)

    if visited[b] == 0:
        print("Impossible")
    else:
        print(visited[b]-1)