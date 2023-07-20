from collections import deque

T = int(input())

def f_D(n):
    return (2*n) % 10000
def f_S(n):
    return (n-1) % 10000
def f_L(n):
    dq = deque(str(n))
    dq.rotate(-1)
    return int(''.join(dq))
def f_R(n):
    dq = deque(str(n))
    dq.rotate(1)
    return int(''.join(dq))

func = ["D","S","L","R"]
for _ in range(T):
    a,b = map(int,input().split())
    dq = deque([a])
    visited = [[] for _ in range(10000)]

    while not visited[b]:
        p = dq.popleft()
        for i,x in enumerate([f_D(p), f_S(p), f_L(p), f_R(p)]):
            if not visited[x]:
                visited[x] = visited[p][:]
                visited[x].append(func[i])
                dq.append(x)

    print(''.join(visited[b]))