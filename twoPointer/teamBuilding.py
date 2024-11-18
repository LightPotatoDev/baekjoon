n = int(input())
L = list(map(int,input().split()))

L_idx = [[L[i],i] for i in range(n)]
L_idx.sort()
left = 0
right = n-1
select = [1]*n
ans = 0

for m,idx in L_idx[:-1]:
    ans = max(ans, m*(idx-left-1), m*(right-idx-1))
    select[idx] = 0
    while select[left] == 0:
        left += 1
    while select[right] == 0:
        right -= 1

print(ans)