n,k = map(int,input().split())
pos = {n}
visited = {n}
steps = 0
found = False

while not found:
    S = set()
    A = pos.copy()
    for i in pos:
        if i == k:
            found = True
            break
        elif i < k:
            for j in [i-1,i+1,2*i]:
                if 0 <= j <= 100000 and j not in visited:
                    S.add(j)
                    visited.add(j)
        else:
            S.add(i-1)
            visited.add(i-1)

    for i in A:
        pos.remove(i)
    for i in S:
        pos.add(i)
    if not found:
        steps += 1

print(steps)


""" by goodjob22

from collections import deque

def bfs():
    q = deque([n])
    while q:
        cur_pos = q.popleft()
        if cur_pos == k:
            return array[cur_pos]
        for next_pos in (cur_pos-1, cur_pos+1, 2*cur_pos):
            if 0 <= next_pos < MAX and array[next_pos] == 0:
                array[next_pos] = array[cur_pos] + 1
                q.append(next_pos)


n, k = map(int, input().split())
MAX = 100001
array = [0] * MAX
print(bfs())
"""
