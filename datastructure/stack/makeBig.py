n,k = map(int,input().split())
s = list(map(int,input()))

for i in range(k):
    for j in range(n-i):
        if j == n-i-1:
            s.pop(j)
            break
        if s[j] < s[j+1]:
            s.pop(j)
            break

print(''.join(map(str,s)))