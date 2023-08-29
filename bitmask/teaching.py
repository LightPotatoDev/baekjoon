from itertools import combinations
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
words = [set(list(input().rstrip())) for _ in range(n)]

N = [chr(i+97) for i in range(26)]
always = ["a","n","t","i","c"]
for i in always:
    N.remove(i)
comb = combinations(N,k-5)
maxWord = 0

print(words)

for c in comb:
    readable = 0
    for word in words:
        if len(word-set(c)) == 0:
            readable += 1
    maxWord = max(maxWord,readable)

print(maxWord)
