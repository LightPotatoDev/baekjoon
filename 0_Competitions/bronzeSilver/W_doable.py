import sys
input = sys.stdin.readline

j,n = map(int,input().split())
L = []
for _ in range(n):
    inp = input().rstrip()
    size = 0
    for i in inp:
        if i.isupper():
            size += 4
        elif i.islower() or i.isdigit():
            size += 2
        elif i == " ":
            size += 1
    L.append(size)

ans = 0
for i in L:
    if i <= j:
        ans += 1
print(ans)