import math

n,k = map(int,input().split())
s = list(input())

def maximize(k):
    def leftmost_c(x):
        for i in range(x,n):
            if s[i] == 'C':
                return i
            if i == n-1:
                return n

    def rightmost_p(x):
        for i in range(x,-1,-1):
            if s[i] == 'P':
                return i
            if i == 0:
                return -1

    i = 0
    j = n-1
    while k > 0:
        i = leftmost_c(i)
        j = rightmost_p(j)

        if i >= j:
            break
        s[i],s[j] = s[j],s[i]
        k -= 1

def prefix_sum(L):
    for i in range(1,len(L)):
        L[i] += L[i-1]
    return L

maximize(k)

p_prefix = [int(s[i]=='P') for i in range(n)]
p_prefix = prefix_sum(p_prefix)

ans = 0
for i in range(n):
    if s[i] == 'C':
        ans += math.comb(p_prefix[i],2)
print(ans)