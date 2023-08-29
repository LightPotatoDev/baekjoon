n = int(input())

if n == 1 or n == 3:
    print(-1)
    exit(0)

cnt = (n-5) // 5
n -= cnt * 5

plus = (1,3,2,4,3)
cnt += plus[n-5]
print(cnt)