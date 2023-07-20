import sys
from bisect import bisect_left, bisect_right

n = int(input())
L = [int(sys.stdin.readline()) for _ in range(n)]

print(round(sum(L)/n))

L.sort()
print(L[n//2])

counts = dict()
for i in L:
    r_i = bisect_right(L, i)
    l_i = bisect_left(L,i)
    counts[i] = r_i-l_i
most = [k for k,v in counts.items() if v == max(counts.values())]
print(most[int(len(most)!=1)])

print(L[-1]-L[0])

#최빈값 Alternative
##cnt = Counter(nums)
##
### 상위 두 개만 보기
##if len(cnt) != 1:
##  mode = cnt.most_common(2)
##  if mode[0][1] == mode[1][1]:
##    print(mode[1][0])
##  else:
##    print(mode[0][0])
##else:
##  mode = cnt.most_common(1)
##  print(mode[0][0])