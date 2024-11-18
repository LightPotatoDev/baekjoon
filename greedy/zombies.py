from collections import deque
import sys
input = sys.stdin.readline

l = int(input())
ml,mk = map(int,input().split())
c = int(input())
zombies = [int(input()) for _ in range(l)]
damages = []
mine_log = deque([])
ans = "YES"

for i in range(l):
    hits = min(ml,i+1) - len(mine_log)
    dmg = hits * mk

    if dmg < zombies[i]:
        if c > 0:
            c -= 1
            mine_log.append(i)
        else:
            ans = "NO"
            break

    if mine_log and mine_log[0] <= i-ml:
        mine_log.popleft()

print(ans)