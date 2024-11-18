L = [list(input()) for _ in range(8)]

white = 0
black = 0
D = {"k":0, "p":1, "n":3, "b":3, "r":5, "q":9, ".":0}
for i in range(8):
    for j in range(8):
        t = L[i][j]
        if t.isupper():
            white += D[t.lower()]
        else:
            black += D[t]

print(white-black)