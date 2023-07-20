s = input().upper()
L = [0]*26

for i in s:
    L[ord(i)-65] += 1

M = max(L)
indices = [i for i, val in enumerate(L) if val == M]

if len(indices) >= 2:
    print('?')
else:
    print(chr(L.index(M)+65))

#list.count(element) : returns number of occurence of an element