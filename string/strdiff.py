a,b = input().split()

diff = 50
for i in range(len(b)-len(a)+1):
    d = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            d += 1
    diff = min(diff,d)

print(diff)

