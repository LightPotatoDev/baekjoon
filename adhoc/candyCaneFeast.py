import sys
input = sys.stdin.readline

class Cow:
    def __init__(self,i,h):
        self.idx = i
        self.height = h

n,m = map(int,input().split())
heights = list(map(int,input().split()))
canes = list(map(int,input().split()))
cows = [Cow(i,heights[i]) for i in range(n)]

def feed_cows(c):
    max_h = 0
    eaten = 0
    for cow in cows:
        if eaten == c:
            break
        if cow.height > max_h:
            max_h = cow.height
            eat = min(max_h,c) - eaten
            cow.height += eat
            eaten += eat

for c in canes:
    feed_cows(c)

for cow in cows:
    print(cow.height)