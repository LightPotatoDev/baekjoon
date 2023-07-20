s = input()
q = int(input())
D = dict()

for i,x in enumerate(s):
    if x not in D:
        D[x] = [i]
    else:
        D[x] += [i]

for _ in range(q):
    a,l,r = input().split()
    if a in D:
        print(len([i for i in D[a] if int(l) <= i <= int(r)]))
    else:
        print(0)