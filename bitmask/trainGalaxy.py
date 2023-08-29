n,m = map(int,input().split())
Trains = [0]*(n+1)
mask = 2**20-1

def setKthBit(n,k,mode):
    pos = 2**19 >> (k-1)
    if mode == 1:
        return (pos | n)
    elif mode == 0:
        return (mask ^ pos) & n

for _ in range(m):
    cmd = list(map(int,input().split()))

    if cmd[0] == 1:
        i,x = cmd[1],cmd[2]
        Trains[i] = setKthBit(Trains[i],x,1)
    elif cmd[0] == 2:
        i,x = cmd[1],cmd[2]
        Trains[i] = setKthBit(Trains[i],x,0)
    elif cmd[0] == 3:
        i = cmd[1]
        Trains[i] = (Trains[i] >> 1)
    elif cmd[0] == 4:
        i = cmd[1]
        Trains[i] = ((Trains[i] << 1) & mask)

##    for i in Trains[1:]:
##        print(i,end= ' ')
##    print('')
##    for i in Trains[1:]:
##        print(bin(i)[2:].zfill(20), end=' ')

S = set(Trains[1:])
print(len(S))