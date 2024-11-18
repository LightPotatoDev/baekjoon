s = input()

def manacher(s):
    S = ['#']
    for x in s:
        S.append(x)
        S.append('#')

    n = len(S)
    P = [0]*n
    r = 0
    c = 0

    for i in range(n):
        if r < i:
            P[i] = 0
        else:
            P[i] = min(P[2*c-i], r-i)

        while (i-P[i]-1 >= 0 and i+P[i]+1 < n and S[i-P[i]-1] == S[i+P[i]+1]):
            P[i] += 1

        if (r < i+P[i]):
            r = i+P[i]
            c = i

    return P

ans = 0
for x in manacher(s):
    ans += (x+1) // 2
print(ans)