import sys
input = sys.stdin.readline

n,m,t = map(int,input().split())
bubbles = dict()
ans = 0

def bubble_spread():
    global bubbles, ans

    new_bubbles = dict()
    for y,k in bubbles.items():
        ans -= k
        if k//5 < 1:
            continue
        for i in range(-1,2):
            if not (1 <= y+i <= n):
                continue
            if y+i in new_bubbles:
                new_cnt = min(m,new_bubbles[y+i] + k//5)
                ans += new_cnt - new_bubbles[y+i]
                new_bubbles[y+i] = new_cnt
            else:
                new_bubbles[y+i] = k//5
                ans += k//5

    bubbles = new_bubbles.copy()

for _ in range(t):
    y,k = map(int,input().split())
    if y in bubbles:
        new_cnt = min(m,bubbles[y]+k)
        ans += new_cnt - bubbles[y]
        bubbles[y] = new_cnt
    else:
        ans += k
        bubbles[y] = k
    bubble_spread()
    print(ans)