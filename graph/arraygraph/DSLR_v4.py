import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def rotate(n,dir):
    d1 = n // 1000
    d2 = (n % 1000) // 100
    d3 = (n % 100) // 10
    d4 = n % 10

    if dir == 0:
        return 1000 * d2 + 100 * d3 + 10 * d4 + d1
    else:
        return 1000 * d4 + 100 * d1 + 10 * d2 + d3

func = ["D","S","L","R"]
for _ in range(T):
    a,b = map(int,input().split())
    dq = deque([a])

    trace = [0] * 10000
    trace[a] = -1
    usedfunc = [0] * 10000

    while trace[b] == 0:
        p = dq.popleft()
        for i,x in enumerate([(2*p) % 10000, (p-1) % 10000, rotate(p,0), rotate(p,1)]):
            if trace[x] == 0:
                trace[x] = p
                usedfunc[x] = i
                dq.append(x)

    back = trace[b]
    ans = []
    while back != -1:
        ans.append(usedfunc[back])
        back = trace[back]

    print(ans[::-1])