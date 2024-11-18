from collections import defaultdict

t = int(input())
n = int(input())
A = [0]+list(map(int,input().split()))
m = int(input())
B = [0]+list(map(int,input().split()))

def prefixSum(L):
    for i in range(1,len(L)):
        L[i] += L[i-1]
    return L

def subarraySum(L):
    sumDict = defaultdict(int)
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            sumDict[L[j]-L[i]] += 1
    return sumDict

subA = subarraySum(prefixSum(A))
subB = subarraySum(prefixSum(B))

ans = 0
for i in subA:
    if t-i in subB:
        ans += subA[i] * subB[t-i]
print(ans)