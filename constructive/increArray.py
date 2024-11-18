n,m,k = map(int,input().split())

if (n+m-1 > k):
    print("NO")
    exit(0)

print("YES")
for i in range(n):
    print(*[i+j+1 for j in range(m)])