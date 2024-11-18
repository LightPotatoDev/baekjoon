import sys
import heapq
input = sys.stdin.readline

n = int(input())
coords = [list(map(int,input().split())) for _ in range(n)]
hori = []
verti = []
h_line_ban = [0]*(int(1e6)+1)
v_line_ban = [0]*(int(1e6)+1)

for i in range(n):
    a,b = coords[i-1]
    c,d = coords[i]
    if a == c:
        verti.append((min(b,d), max(b,d)))
        h_line_ban[a] = 1
    if b == d:
        hori.append((min(a,c), max(a,c)))
        v_line_ban[b] = 1

def calc_inter_points(A,h):
    A.sort()
    not_included = []
    included = []
    res = 0
    for x in A:
        heapq.heappush(not_included,x)

    for x in range(-500000.5,500001.5):

        while not_included:
            s = not_included[0][0]
            if s <= x:
                a,b = heapq.heappop(not_included)
                heapq.heappush(included, (b,a))
            else:
                break

        while included:
            e = included[0][0]
            if e < x:
                heapq.heappop(included)
            else:
                break
        res = max(res, len(included))

    return res

print(max(calc_inter_points(hori,True), calc_inter_points(verti,False)))