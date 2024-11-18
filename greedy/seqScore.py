import sys
input = sys.stdin.readline

n = int(input())
plus = []
zeros = 0
minus = []
for _ in range(n):
    a = int(input())
    if a == 0:
        zeros += 1
    if a > 0:
        plus.append(a)
    if a < 0:
        minus.append(a)
plus.sort()
minus.sort(reverse=True)

ans = 0
while len(plus) >= 2:
    p1 = plus.pop()
    p2 = plus.pop()
    if p1 == 1 or p2 == 1:
        ans += p1+p2
    else:
        ans += p1*p2
while len(minus) >= 2:
    p1 = minus.pop()
    p2 = minus.pop()
    ans += p1*p2

if len(plus) == 1:
    ans += plus.pop()
if len(minus) == 1 and zeros == 0:
    ans += minus.pop()

print(ans)