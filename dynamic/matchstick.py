sticks = [6,2,5,5,4,5,6,3,7,6]

def small_number(L):
    non_zero = []
    zeros = 0
    res = []
    L.sort()
    for n in L:
        if n != 0:
            non_zero.append(n)
        else:
            zeros += 1

    res.append(non_zero[0])
    for _ in range(zeros):
        res.append(0)
    for i in range(1,len(non_zero)):
        res.append(non_zero[i])

    final_res = 0
    for i,x in enumerate(res):
        final_res += 10 ** (len(L)-i-1) * x

    if final_res == 0:
        final_res = int(1e20)
    return final_res

dp = [[] for _ in range(15)]
for i in [[],[1],[7],[4],[2],[0],[8]]:
    dp[0].append(i)
for i in range(1,15):
    for j in range(7):
        for k in range()



dp[6] = [6]

##T = int(input())
##for _ in range(T):
##    n = int(input())

