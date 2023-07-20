L = [i for i in range(1,31)]

for _ in range(28):
    L.remove(int(input()))

print(min(L))
print(max(L))