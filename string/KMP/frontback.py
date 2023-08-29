n = int(input())

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

    maxK = max(table)
    if maxK == 0:
        print(-1)
    else:
        print(maxK, table.count(maxK))

KMP(list(map(int,input().split()))[::-1])