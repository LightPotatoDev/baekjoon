t = input()
p = input()

table = [0] * len(p)
j = 0
for i in range(1,len(p)):
    if p[j] == p[i]:
        j += 1
    elif p[0] == p[i]:
        j = 1
    else:
        j = 0
    table[i] = j

j = 0
match = []
for i in range(len(t)):
    print(j,t[i],p[j])
    if t[i] == p[j]:
        j += 1
    elif t[i] == p[j - table[j-1]]:
        j = j - table[j-1]
    else:
        j = j - table[j-1] - 1

    if j == len(p):
        match.append(i-j+2)
        j = table[j-1]

print(len(match))
print(*match)