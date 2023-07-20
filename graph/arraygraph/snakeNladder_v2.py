from collections import deque

n,m = map(int,input().split())
laddersnake = [tuple(map(int,input().split())) for _ in range(n+m)]

tiles = [-1]*101
tiles[1] = 0
dq = deque([1])

def checkladder(position):
    l_starts = [l[0] for l in laddersnake]
    if position in l_starts:
        ind = l_starts.index(position)
        return laddersnake[ind][1]
    return 0


while tiles[100] == -1:
    p = dq.popleft()
    for i in range(1,7):
        if p+i <= 100:
            l_pos = checkladder(p+i)
            if l_pos == 0:
                if tiles[p+i] == -1:
                    tiles[p+i] = tiles[p] + 1
                    dq.append(p+i)
            elif tiles[l_pos] == -1:
                tiles[l_pos] = tiles[p] + 1
                dq.append(l_pos)

print(tiles[100])