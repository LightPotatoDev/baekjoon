t = input()
p = input()

table = [0] * (len(p)+1)
start,match = 1,0
while start+match < len(p):
    if p[start+match] == p[match]:
        match += 1
        table[start+match] = match
    else:
        if match == 0:
            start += 1
        else:
            start += match - table[match]
            match = table[match]

j = 0
Matches = []
for i in range(len(t)):

    if t[i] == p[j]:
        j += 1
    else:
        while j > 0:
            j = table[j]
            if t[i] == p[j]:
                j += 1
                break

    if j == len(p):
        Matches.append(i-j+2)
        j = table[j]

print(len(Matches))
print(*Matches)