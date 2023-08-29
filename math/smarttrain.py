L = [0]*5
for i in range(4):
    a,b = map(int,input().split())
    L[i+1] = L[i] + b - a

print(max(L))