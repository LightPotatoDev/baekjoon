L = []
s = ""

for _ in range(5):
    L.append(input())

for i in range(15):
    for j in range(5):
        try:
            s += L[j][i]
        except:
            pass

print(s)