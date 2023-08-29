S = list(input())
S.sort()

odd = ""
p = 0
L = []
while p < len(S):
    if p+2 <= len(S) and S[p] == S[p+1]:
        L.append(S[p])
        p += 2
    elif odd == "":
        odd = S[p]
        p += 1
    else:
        print("I'm Sorry Hansoo")
        exit(0)

print(''.join(L) + odd + ''.join(L[::-1]))