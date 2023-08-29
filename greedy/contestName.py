n,m = map(int,input().split())
s = input()
L = []

cnt = 0
vowel = ("A","E","I","O","U")
for i in s[::-1]:
    if cnt == 0:
        if i not in vowel:
            L.append(i)
            cnt += 1
    elif cnt <= 2:
        if i == "A":
            L.append(i)
            cnt += 1
    else:
        if cnt < m:
            L.append(i)
            cnt += 1

if cnt == m:
    print("YES")
    print(''.join(L[::-1]))
else:
    print("NO")