T = int(input())

def partition(n):
    L = [0]*11
    L[1] = 1
    L[2] = 2
    L[3] = 4
    for i in range(4,n+1):
        L[i] = L[i-1] + L[i-2] + L[i-3]
    return L[n]

for _ in range(T):
    print(partition(int(input())))