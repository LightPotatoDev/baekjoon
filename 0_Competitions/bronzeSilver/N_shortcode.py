n,m = map(int,input().split())
L = list(map(int,input().split()))

left = []
right = []

lMin = int(1e8)
for i in range(m+1):
    lMin = min(lMin,L[i])
    left.append(lMin)

rMax = 0
for i in range(m+1):
    rMax = max(rMax,L[n-i-1])
    right.append(rMax)

ans = -int(1e8)
for i in range(m+1):
    ans = max(ans, right[i]-left[m-i])
print(ans)