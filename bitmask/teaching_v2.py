from itertools import combinations
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
if k < 5:
    print(0)
    exit()

words = []

for _ in range(n):
    S = set(list(input().rstrip()))
    bits = 0
    for i in S:
        if i not in ["a","n","t","i","c"]:
            bits += 2**(122-ord(i))
    words.append(bits)

N = [1,3,4,5,6,7,9,10,11,12,14,15,16,17,18,20,21,22,23,24,25]
Teach = []
for comb in combinations(N,k-5):
    num = 0
    for i in comb:
        num += 2**(25-i)
    Teach.append(num)

mask = 2**26-1

##for w in words:
##    print(bin(w)[2:].zfill(26))
##print('')
##for t in Teach:
##    print(bin(t)[2:].zfill(26))

ans = 0
for teached in Teach:
    cnt = 0
    for word in words:
        if ((word^mask) | teached) == mask:
            cnt += 1
    ans = max(ans,cnt)

print(ans)
