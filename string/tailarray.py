s = input()
L = []
for i in range(len(s)):
    L.append(s[i:])
L.sort()
for i in L:
    print(i)