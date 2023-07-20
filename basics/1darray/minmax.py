L = []

for i in range(9):
    L.append(int(input()))

largest = max(L)
print(largest)
print(L.index(largest) + 1)