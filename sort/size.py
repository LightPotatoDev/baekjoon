n = int(input())

ppl = [tuple(map(int,input().split())) for _ in range(n)]
ranks = [1]*n

for i in range(n):
    w,h = ppl[i]
    for j in ppl:
        if j[0] > w and j[1] > h: #더 작은 덩치
            ranks[i] += 1

print(' '.join(map(str,ranks)))
