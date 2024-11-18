n,k,m = map(int,input().split())
multitab = list(map(int,input().split()))
device = list(map(int,input().split()))

multitab.sort(reverse=True)
device.sort()



ans = 0

def tabConnect(layer,depth,connect):

    oldConnect = connect
    ans = max(ans,connect)

    if depth == n:
        return

    for i,x in enumerate(layer):
        if x > 0:
            layer[i] -= 1
            layer[i+1] += multitab[depth]
            tabConnect(layer,depth+1,connect)
            layer[i] += 1
            layer[i+1] -= multitab[depth]

l = [0]*(n+1)
l[0] = k
tabConnect(l,0,0)

print(ans)