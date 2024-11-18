from collections import deque
import sys
input = sys.stdin.readline

cog = []
for _ in range(4):
    cog.append(deque(list(map(int,input().rstrip()))))

def rotateCog(n,d,rotated):
    rotated[n] = 1
    if (n > 0 and cog[n-1][2] != cog[n][6] and rotated[n-1] == 0):
        rotateCog(n-1,d*-1, rotated)
    if (n < 3 and cog[n][2] != cog[n+1][6] and rotated[n+1] == 0):
        rotateCog(n+1,d*-1, rotated)
    cog[n].rotate(d)

k = int(input())
for _ in range(k):
    n,d = map(int,input().split())
    n -= 1
    rotateCog(n,d,[0,0,0,0])

ans = 0
for i in range(4):
    ans += (cog[i][0] == 1) * (2**i)

print(ans)