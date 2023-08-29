L = []
for i in range(5):
    L.append(int(input()))

for i in L:
    if L.count(i) % 2 == 1:
        print(i)
        break