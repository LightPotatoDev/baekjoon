cy,cm,cd = map(int,input().split('-'))
n = int(input())
cnt = 0
for _ in range(n):
    y,m,d = map(int,input().split('-'))
    if y > cy:
        cnt += 1
        continue
    if y == cy:
        if m > cm:
            cnt += 1
            continue
        if m == cm:
            if d >= cd:
                cnt += 1
print(cnt)