n,m,k = map(int,input().split())
L = list(input())

def infect(ind):
    i = ind
    for _ in range(k):
        i -= 1
        if i < 0:
            break
        if L[i] == ".":
            L[i] = "r"

    i = ind
    for _ in range(k):
        i += 1
        if i >= n:
            break
        if L[i] == ".":
            L[i] = "r"


for i,x in enumerate(L):
    if x == "R":
        infect(i)

if L.count("R")+L.count("r") <= m:
    print("Yes")
else:
    print("No")