import sys
input = sys.stdin.readline

n = int(input())
village = [tuple(map(int,input().split())) for _ in range(n)]

def dist(center):
    s = 0
    for pos,ppl in village:
        s += abs(pos-center) * ppl
    return s

for i in range(20):
    print(dist(i))