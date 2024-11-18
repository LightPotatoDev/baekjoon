n = int(input())
m = int(input())
fixed = [int(input()) for _ in range(m)]

fibo = [1,1]
for i in range(40):
    fibo.append(fibo[-1]+fibo[-2])

subseq = []
combo = 0
for i in range(1,n+1):
    if i not in fixed:
        combo += 1
    else:
        subseq.append(combo)
        combo = 0
subseq.append(combo)

ans = 1
for i in subseq:
    ans *= fibo[i]
print(ans)