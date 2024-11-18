s = [['.']*2000 for _ in range(2000)]
for i in range(2000):
    for j in range(2000):
        if i != 0 and j != 0 and i != 1999 and j != 1999 and (i+j)%2 == 0:
            s[i][j] = '#'

for i in range(2000):
    s[i] = ''.join(s[i])
ss = '\n'.join(s)
print(s)

f = open('island7.txt', 'w')
f.write(ss)
f.close()