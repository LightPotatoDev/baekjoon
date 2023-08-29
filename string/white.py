L = []
for _ in range(8):
    L.append(list(input()))

cnt = 0
for i in range(8):
    for j in range(8):
        if L[i][j] == "F" and (i+j)%2 == 0:
            cnt += 1
print(cnt)