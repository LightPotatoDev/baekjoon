p1 = input()
p2 = input()
cnt = 1
for i in range(4):
    if p1[i] != p2[i]:
        cnt *= 2
print(cnt)