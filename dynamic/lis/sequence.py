n = int(input())
L = list(map(int,input().split()))
Inc = [1]
Dec = [1]

for i in range(1,n):
    if L[i-1] < L[i]:
        Inc.append(Inc[i-1]+1)
        Dec.append(1)
    elif L[i-1] > L[i]:
        Inc.append(1)
        Dec.append(Dec[i-1]+1)
    else:
        Inc.append(Inc[i-1]+1)
        Dec.append(Dec[i-1]+1)

print(max(max(Inc),max(Dec)))