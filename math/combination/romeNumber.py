n = int(input())
Roman = [1,5,10,50]
S = set()

def numGen(lim,L,pos):
    if lim == n:
        s = 0
        for i in range(4):
            s += Roman[i] * L[i]
        S.add(s)
        return

    if pos < 3:
        numGen(lim,L,pos+1)
        L[pos] += 1
        numGen(lim+1,L,pos+1)
        L[pos] -= 1
    L[pos] += 1
    numGen(lim+1,L,pos)
    L[pos] -= 1

numGen(0,[0]*4,0)
print(len(S))

"""by larpore2
from itertools import combinations_with_replacement
N = int(input())
arr = [1,5,10,50]
answer = []
result = list(combinations_with_replacement(arr,N))
for col in result:
    answer.append(sum(col))
print(len(set(answer)))

combinations_with_replacement - 중복조합
중복을 허락하면서 뽑기
"""
