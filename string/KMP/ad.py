l = int(input())
p = input()

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

print(l-table[l])