n = int(input())
L = [0]+list(map(int,input().split()))
ans = 0
length = 0

for i in range(n):
    if L[i+1] > L[i]:
        length += 1
    else:
        length = 1
    ans += length

print(ans)
