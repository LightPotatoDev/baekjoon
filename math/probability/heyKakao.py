a,d,k = map(int,input().split())
d /= 100
k /= 100
ans = d
i = 1
lose = []
while d < 1:
    lose.append(1-d)
    prev = 1
    for j in range(i):
        prev *= lose[j]

    i += 1
    d *= (1+k)
    ans += prev * min(1,d) * i

print(a*ans)