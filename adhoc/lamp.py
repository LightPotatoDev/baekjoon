import sys
input = sys.stdin.readline

class Line:
    def __init__(self, data):
        self.shape = data
        self.num = 0
        self.switch = 0

    def __repr__(self):
        return str([self.shape,self.num,self.switch])

n,m = map(int,input().split())
lines = dict()

for _ in range(n):
    l = input().rstrip()
    if l in lines:
        lines[l].num += 1
    else:
        lines[l] = Line(l)
        lines[l].num = 1
        lines[l].switch = l.count('0')

k = int(input())
ans = 0

for l in lines:
    if (k >= lines[l].switch) and (k%2 == lines[l].switch%2):
        ans = max(ans, lines[l].num)

print(ans)