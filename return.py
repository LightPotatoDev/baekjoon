n = int(input())
X = [0]+list(map(int,input().split()))
T = [0]+list(map(int,input().split()))
ans = 0
prev_x = X[-1]*2

while X:
    x = X.pop()
    t = T.pop()
    ans = max(t,ans+prev_x-x)
    prev_x = x

print(ans)