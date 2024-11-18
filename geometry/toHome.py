import math

x,y,d,t = map(int,input().split())
dist = math.sqrt(x**2 + y**2)
dist2 = dist
if d <= t:
    print(dist)
    exit()

#1 - 점프 -> 걸어감
ans = 0
jumps = math.floor(dist/d)
ans += jumps*t
dist -= jumps*d
ans += min(dist, t+abs(dist-d))

#2 - 점프 연속
jumps2 = max(2,math.ceil(dist2/d))
ans2 = jumps2*t

print(min(ans,ans2))