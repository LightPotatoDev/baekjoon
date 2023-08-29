s = input()
bomb = list(input())
l=len(bomb)

L = []
for i in s:
    L.append(i)
    if len(L) >= l and L[-l:] == bomb:
        for j in range(l):
            L.pop()

print(''.join(L))
