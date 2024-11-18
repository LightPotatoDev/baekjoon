n,k = map(int,input().split())
table = list(input())
taken = [0]*n

for i in range(n):
    if table[i] == 'P':
        for j in range(max(0,i-k),min(n,i+k+1)):
            if table[j] == 'H' and taken[j] == 0:
                taken[j] = 1
                break

print(sum(taken))