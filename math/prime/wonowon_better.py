ans = 0
for n in range(7, int(input()) + 1):
    d = 2
    prime = True
    while d*d <= n:
        if n % d == 0:
            prime = False
            break
        d += 1
    if prime:
        w = m = 1
        while m > 0:
            w += 2
            m = (m*100 + 1) % n
        ans += n == w + 2
print(ans)
