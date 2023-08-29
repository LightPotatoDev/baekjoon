n = int(input())
p = [0] + list(map(int,input().split()))

for i in range(1,n+1):
    p[i] = min([p[j] + p[i-j] for j in range(i//2+1)])
print(p[n])