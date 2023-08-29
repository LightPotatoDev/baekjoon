s = input()

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

    return max(table)

ans = 0
for i in range(len(s)):
    ans = max(KMP(s[i:]), ans)
print(ans)
