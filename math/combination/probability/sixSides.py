D1 = list(map(int,input().split()))
D2 = list(map(int,input().split()))

p1win = 0
p2win = 0
for i in D1:
    for j in D2:
        if i > j:
            p1win += 1
        elif i < j:
            p2win += 1
n = round(p1win / (p1win+p2win),5)
print("{:.5f}".format(n))