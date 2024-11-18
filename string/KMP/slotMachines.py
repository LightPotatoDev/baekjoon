n = int(input())
A = list(map(int,input().split()))

def failure(s):
    l = len(s)
    lps = [0] * l
    i,match = 1,0

    while i < l:
        if s[i] == s[match]:
            match += 1
            lps[i] = match
            i += 1
        else:
            if match == 0:
                i += 1
            else:
                match = lps[match-1]

    return lps

lps = failure(A[::-1])
k,p = n+1,12343214 # p > 0 im stupid :(
for i in range(n):
    np = (i+1)-lps[i]
    nk = n-i-1
    if nk+np < k+p or (nk+np == k+p and np < p):
        k,p = nk,np

print(k,p)