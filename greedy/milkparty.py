n = int(input())
L = list(map(int,input().split()))
state = 0
cnt = 0
for i in L:
    if i == state:
        state = (state+1) % 3
        cnt += 1
print(cnt)
