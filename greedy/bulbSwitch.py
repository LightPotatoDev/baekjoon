n = int(input())
state = list(map(int,list(input())))
target = list(map(int,list(input())))
ans = int(1e8)

def switching(inp):
    s = 0
    for i in range(1,n):
        if inp[i-1] != target[i-1]:
            inp[i-1] = 1-inp[i-1]
            inp[i]   = 1-inp[i]
            if i+1 < n:
                inp[i+1] = 1-inp[i+1]
            s += 1

    if inp == target:
        return s
    else:
        return int(1e8)

ans = min(ans,switching(state[:]))
state[0] = 1-state[0]
state[1] = 1-state[1]
ans = min(ans,switching(state[:])+1)
if ans == int(1e8):
    print(-1)
else:
    print(ans)
