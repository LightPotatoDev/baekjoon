x = int(input())
cnt = [0]*(2**(x-1))

for i in range(1,2**x):
    for j in range(1,2**x):
        k = i^j
        if i < j < k:
            print(i,j,k)
            cnt[i] += 1

print(cnt)