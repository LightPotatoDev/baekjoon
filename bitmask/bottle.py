n,k = map(int,input().split())

ans = 0
while n.bit_count() > k:
    ans += 1
    n += 1
print(ans)

"""by cks537
111000 -> 1000000
110001 -> 110010
110011 -> 110100
1의 개수를 효율적으로 줄이기

import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0
while bin(N).count('1') > K :
    idx = bin(N)[::-1].index('1')
    cnt += 2**idx
    N += 2**idx

print(cnt)
"""