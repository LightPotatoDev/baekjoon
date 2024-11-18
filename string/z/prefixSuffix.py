import sys
input = sys.stdin.readline

s = input().rstrip()

def z_array(s):
    n = len(s)
    l,r = 0,0
    z = [0]*n
    z[0] = n

    for i in range(1,n):
        if i > r:
            l,r = i,i
            while r < n and s[r-l] == s[r]:
                r += 1
            z[i] = r-l
            r -= 1
        else:
            k = i-l
            if (z[k] < r-i+1):
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r-l] == s[r]:
                    r += 1
                z[i] = r-l
                r -= 1

    return z

z = z_array(s)
n = len(s)
cnt = [0]*(n+1)
for i in range(n):
    cnt[z[i]] += 1
for i in range(n-1,-1,-1):
    cnt[i] += cnt[i+1]

ans = []
for i in range(n-1,-1,-1):
    if i + z[i] == n:
        ans.append((n-i, cnt[n-i]))

print(len(ans))
for a,b in ans:
    print(a,b)