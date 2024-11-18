import sys
input = sys.stdin.readline

SIZE = int(1e6)+2
start = [0]*SIZE
end = [0]*SIZE
studs = [0]*SIZE
st = 0

n = int(input())
for _ in range(n):
    s,e = map(int,input().split())
    start[s] += 1
    end[e+1] += 1

q = int(input())
Q = list(map(int,input().split()))

for i in range(SIZE):
    st += start[i]
    st -= end[i]
    studs[i] = st

for i in Q:
    print(studs[i])