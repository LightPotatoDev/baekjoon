from itertools import permutations

def KMP(p):
    l = len(p)
    table = [0] * (l+1)
    start,match = 1,0
    while start+match < l:
        if p[start+match] == p[match]:
            match += 1
            table[start+match] = match
        else:
            if match == 0:
                start += 1
            else:
                start += match - table[match]
                match = table[match]

    repeat = l - table[-1] #반복 문자열의 길이
    if l % repeat == 0:
        return l // repeat #반복 횟수
    else:
        return 1

n = int(input())
L = [input().rstrip() for _ in range(n)]
k = int(input())
perm = permutations(L,n)
ans = 0

for p in perm:
    s = ''.join(p)
    if KMP(s) == k:
        ans += 1
print(ans)