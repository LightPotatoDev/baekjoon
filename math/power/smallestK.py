L = [1]
x = 2
r = 1
ans = 1
start = 1
incre = 4
MAX = int(1e20)

while r < 20:
    x *= pow(2,incre,MAX)
    x %= MAX
    ans += incre

    while 1 <= ((x // 10**r) % 10) <= 2:
        r += 1
        L.append(ans)
        incre *= 5

T = int(input())
for _ in range(T):
    n = int(input())
    print(L[n-1])
