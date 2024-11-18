n = int(input())
L = list(map(int,input().split()))
ans = 0

def consecutive(a,b):
    res = 0
    max_res = 0
    for x in L:
        if x not in [a,b]:
            res = 0
        else:
            res += 1
        max_res = max(max_res,res)

    return max_res

for i in range(1,10):
    for j in range(1,10):
        if i != j:
            ans = max(ans, consecutive(i,j))

print(ans)