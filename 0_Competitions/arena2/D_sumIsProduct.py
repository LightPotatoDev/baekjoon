n = int(input())
L = list(map(int,input().split()))

sumL = [0] + L[:]
for i in range(n):
    sumL[i+1] += sumL[i]
prodL = [1] + L[:]
for i in range(n):
    prodL[i+1] *= prodL[i]
print(sumL)
print(prodL)