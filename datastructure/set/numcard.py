import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n = int(input())
cards = list(map(int,input().split()))
cards.sort()
m = int(input())
finds = list(map(int,input().split()))

output = []
for i in finds:
    r_i = bisect_right(cards, i)
    l_i = bisect_left(cards,i)
    output.append(r_i-l_i)

print(' '.join(map(str,output)))