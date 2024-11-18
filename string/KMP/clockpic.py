MAX_ANGLE = 360000

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def failure(s):
    l = len(s)
    lps = [0] * (l+1)
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

def search(pat,txt):
    n,m = len(txt), len(pat)
    lps = failure(pat)
    i,j = 0,0
    res = False

    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                res = True
                j = lps[j-1]
                break
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    return res

A.sort()
B.sort()
A_diff = [(A[(i+1)%n]-A[i]) % MAX_ANGLE for i in range(n)]
B_diff = [(B[(i+1)%n]-B[i]) % MAX_ANGLE for i in range(n)]

res = search(A_diff, B_diff+B_diff)
print('possible' if res == True else 'impossible')