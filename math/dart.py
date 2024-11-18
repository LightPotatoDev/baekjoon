import math

L = [0]+list(map(float,input().split()))+[int(1e9)]
std = float(input())
sq2 = 2**0.5

score = [50,25,10.5,31.5,10.5,21,0]
ans = 0

def func(x):
    return math.sqrt(math.pi/2) / std * math.erf(x/(sq2*std))

for i in range(7):
    ans += score[i] * (func(L[i+1]) - func(L[i]))
print(ans)