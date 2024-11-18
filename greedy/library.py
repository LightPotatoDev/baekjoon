n,m = map(int,input().split())
L = list(map(int,input().split()))
minus = []
plus = []
for i in L:
    if i < 0:
        minus.append(i)
    if i > 0:
        plus.append(i)
minus.sort(reverse=True)
plus.sort()
ans = 0

def putback(L,m):
    s = abs(L[-1])
    while L and m > 0:
        L.pop()
        m -= 1
    return s

if len(minus) != 0 and (len(plus) == 0 or abs(minus[-1]) > plus[-1]):
    ans += putback(minus,m)
else:
    ans += putback(plus,m)

while minus:
    ans += putback(minus,m)*2
while plus:
    ans += putback(plus,m)*2

print(ans)