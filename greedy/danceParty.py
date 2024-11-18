n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
manMinus = []
manPlus = []
womanMinus = []
womanPlus = []

for i in A:
    if i < 0:
        manMinus.append(i)
    if i > 0:
        manPlus.append(i)
for i in B:
    if i < 0:
        womanMinus.append(i)
    if i > 0:
        womanPlus.append(i)

def pair(minus,plus):
    minus.sort(reverse=True)
    plus.sort()
    res = 0
    j = 0
    for i in minus:
        if j >= len(plus):
            break
        if abs(i) > plus[j]:
            j += 1
            res += 1

    return res

print(pair(manMinus,womanPlus) + pair(womanMinus,manPlus))