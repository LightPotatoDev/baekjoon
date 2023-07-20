L = []

i = 0
while len(L) < 10000:
    i += 1
    if "666" in str(i):
        L.append(i)

print(L[int(input())-1])