from collections import deque

n,k = map(int,input().split())
durability = deque(map(int,input().split()))
robot = deque([0]*(2*n))
ans = 1

def reduce_dur(pos):
    global k
    durability[pos] -= 1
    if durability[pos] == 0:
        k -= 1

while True:
    durability.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0

    for i in range(n-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and durability[i+1] > 0:
            robot[i] = 0
            reduce_dur(i+1)
            robot[i+1] = 1
    robot[n-1] = 0

    if durability[0] > 0:
        robot[0] = 1
        reduce_dur(0)

    if k <= 0:
        break

    ans += 1

print(ans)