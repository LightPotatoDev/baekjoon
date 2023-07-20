import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def f_L(n):
    dq = deque(str(n).zfill(4))
    dq.rotate(-1)
    return int(''.join(dq))

def f_R(n):
    dq = deque(str(n).zfill(4))
    dq.rotate(1)
    return int(''.join(dq))

func = ["D","S","L","R"]
for _ in range(T):
    a,b = map(int,input().split())
    dq = deque([a])

    visited = [0] * 10000
    visited[a] = [-1,-1]
    while visited[b] == 0:
        p = dq.popleft()
        for i,x in enumerate([(2*p) % 10000, (p-1) % 10000, f_L(p), f_R(p)]):
            if visited[x] == 0:
                visited[x] = [p,i]
                dq.append(x)

    back = visited[b]
    ans = ""
    while back[0] != -1:
        ans += func[back[1]]
        back = visited[back[0]]

    print(ans[::-1])