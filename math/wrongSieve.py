import math

n = int(input())
ans = 0
L = []

n -= 1
for i in range(1,int(math.sqrt(n))+1):
    ans += n//i
    L.append(n//i)
L.append(int(math.sqrt(n)))

for i in range(1,int(math.sqrt(n))+1):
    ans += (L[i-1]-L[i])*i
ans += n+1
print(ans)


exit(0)
def wrongSieve(n):
    iter = [0]*(n+1)
    counting = [0]*(n+1)

    for i in range(1,n+1):
        for j in range(1,n+1,i):
            iter[j] += 1

    for i in range(1,n+1):
        counting[i] = iter.count(i)
    return iter

for i in range(1,30+1):
    print(wrongSieve(i))